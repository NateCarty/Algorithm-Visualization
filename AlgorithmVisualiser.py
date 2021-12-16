import tkinter as tk
from tkinter import OptionMenu
from tkinter import StringVar

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ArrayTracker():

    # initialize by making an array copy and resetting values
    def __init__(self, array):
        self.array = np.copy(array)
        self.reset()

    def reset(self):
        self.index = []
        self.values = []
        self.accessType = []
        self.fullCopies = []

    # this will be called whenever an item is set or retrieved
    # it will store a full copy of the current state
    def track(self, key, access_type):
        self.index.append(key)
        self.values.append(self.array[key])
        self.accessType.append(access_type)
        self.fullCopies.append(np.copy(self.array))

    # method when an array value is accessed
    def __getitem__(self, key):
        self.track(key, "get")
        return self.array.__getitem__(key)

    # method when an array value is set
    def __setitem__(self, key, value):
        self.array.__setitem__(key, value)
        self.track(key, "set")   

    # method to return length
    def __len__(self):
        return self.array.__len__()

class Window(tk.Frame):
    def __init__(self, master = None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        self.config(bg="white")
        
        # variables
        self.elementNumber = 25
        self.currentAlgorithm = "Insertion"
        self.animation = None
        self.currentColor = "Green"

        # create an array of elements evenly spaced out from 1 to 1000, rounded
        intArray = np.round(np.linspace(4, 1000, self.elementNumber))

        # randomly shuffle array in place
        np.random.shuffle(intArray)

        # need a class to track our array being sorted
        self.intArray = ArrayTracker(intArray)

        # tkinter frame for our button menu
        buttonFrame = tk.Frame(self)
        buttonFrame.config(bg="white")
        buttonFrame.pack()


        # OptionMenus (Drop-down Menus)
        self.colorSelectorVar = StringVar()
        self.colorSelectorVar.set("Green")
        self.colorSelector = OptionMenu(buttonFrame, self.colorSelectorVar, "Green", "Yellow", "Purple", "Orange", "Blue", "Red")
        self.colorSelector.pack(side=tk.LEFT)
        self.colorSelector.config(bg="#add8e6", activebackground="#6fbbd3", highlightbackground="white")

        self.algoSelectorVar = StringVar()
        self.algoSelectorVar.set("Insertion")
        self.algoSelector = OptionMenu(buttonFrame, self.algoSelectorVar, "Insertion", "Selection", "Bubble", "Quick Sort", "Heap")
        self.algoSelector.pack(side=tk.LEFT)
        self.algoSelector.config(bg="#add8e6", activebackground="#6fbbd3", highlightbackground="white")

        # Labels and User Entry
        label = tk.Label(buttonFrame, text="Number of Values:")
        label.config(bg="white")
        label.pack(side=tk.LEFT)

        self.valueLength = tk.Entry(buttonFrame, width=3)
        self.valueLength.insert(0, '25')
        self.valueLength.pack(side=tk.LEFT)

        label = tk.Label(buttonFrame, text="Update Speed (ms):")
        label.pack(side=tk.LEFT)
        label.config(bg="white")

        self.speed = tk.Entry(buttonFrame, width=2)
        self.speed.insert(0, '5')
        self.speed.pack(side=tk.LEFT)

        # Buttons
        self.button = tk.Button(buttonFrame, text="Start", command = self.on_start)
        self.button.pack(side=tk.LEFT, padx=10)
        self.button.config(bg="#add8e6", activebackground="#6fbbd3")

        self.resetButton = tk.Button(buttonFrame, text="Reset", command=self.on_reset)
        self.resetButton.pack(side=tk.LEFT)
        self.resetButton.config(bg="#add8e6", activebackground="#6fbbd3")

        # create our matplotlib figure
        self.fig = plt.Figure(figsize=(10, 6))
        
        # add bar chart with our data
        self.axis = self.fig.add_subplot(111)
        self.rectangles = self.axis.bar(np.arange(0, self.elementNumber, 1), self.intArray, align = "edge")

        # configure bar chart looks
        self.axis.set_xlim([0, self.elementNumber])
        self.axis.set(title = f"{self.currentAlgorithm}")
        self.axis.set_xticks([])
        self.axis.set_ylim(0,1000)
        for rectangle in self.rectangles.patches:
            rectangle.set_color("#%02x%02x%02x" % self.element_to_rgb(rectangle.get_height(), self.getRGB()))

        # add and draw FigureCanvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    # function that takes a height element and returns correct color 
    # to spread color over interval based on height
    def element_to_rgb(self, element, rgb):
        minRVal = int(rgb[0] % 10)
        maxRVal = rgb[0]
        red = int((element) / 1000 * (maxRVal - minRVal) + minRVal)
        minGVal = int(rgb[1] % 10)
        maxGVal = rgb[1]
        green = int((element) / 1000 * (maxGVal - minGVal) + minGVal)
        minBVal = int(rgb[2] % 10)
        maxBVal = rgb[2]
        blue = int((element) / 1000 * (maxBVal - minBVal) + minBVal)
        return red, green, blue

    # function that checks current color and returns rgb value
    def getRGB(self):
        # "Green", "Yellow", "Purple", "Orange", "Blue", "Red"
        color = self.currentColor
        if color == "Green":
            return [92, 205, 120]
        elif color == "Yellow":
            return [239, 255, 0]
        elif color == "Purple":
            return [92, 35, 178]
        elif color == "Orange":
            return [255, 162, 0]
        elif color == "Blue":
            return [0, 43, 255]
        elif color == "Red":
            return [255, 0 , 0]

    # function that checks the current algorithm and sorts array accordingly
    def arraySorter(self):
        if self.currentAlgorithm == "Insertion":

            i = 1
            while i < len(self.intArray):
                j = i
                while j > 0 and self.intArray[j - 1] > self.intArray[j]:
                    self.intArray[j], self.intArray[j - 1] = self.intArray[j - 1], self.intArray[j]
                    j -= 1
                i += 1

        elif self.currentAlgorithm == "Selection":
            for i in range(len(self.intArray)):
                minIndex = i
                for j in range(i+1, len(self.intArray)):
                    if self.intArray[minIndex] > self.intArray[j]:
                        minIndex = j   
                self.intArray[i], self.intArray[minIndex] = self.intArray[minIndex], self.intArray[i]

    # function when start button is pressed
    def on_start(self):

        # we want to sort the array with the current algorithm
        self.arraySorter()
        
        # if animation is not running, start it
        if self.animation is None:
            return self.start()

        # if animation is running, pause it
        if self.running:
            self.animation.event_source.stop()
            self.button.config(text="Un-Pause")
        
        # else, animation is pause, unpause it
        else:
            self.animation.event_source.start()
            self.button.config(text="Pause")

        self.running = not self.running
    # funtion when reset button is pressed
    def on_reset(self):

        # clear all values and animation
        self.axis.cla()
        self.intArray.reset()
        self.animation = None

        # get settings values
        self.elementNumber = int(self.valueLength.get())
        self.currentAlgorithm = self.algoSelectorVar.get()
        self.currentColor = self.colorSelectorVar.get()

        # recreate random data and intArray
        intArray = np.round(np.linspace(4, 1000, self.elementNumber))
        
        np.random.shuffle(intArray)

        self.intArray = ArrayTracker(intArray)

        # recreate bar chart
        self.rectangles = self.axis.bar(np.arange(0, self.elementNumber, 1), self.intArray, align = "edge", width = .8)
        self.axis.set_xlim([0, self.elementNumber])
        self.axis.set(title = f"{self.currentAlgorithm}")
        self.axis.set_xticks([])

        for rectangle in self.rectangles.patches:
            rectangle.set_color("#%02x%02x%02x" % self.element_to_rgb(rectangle.get_height(), self.getRGB()))

        # redraw canvas
        self.canvas.draw()
        self.running = False
        self.button.config(text = "Start")

        return

    # function called when start is pressed and there is no current animation
    def start(self):
        try:
            self.animation = animation.FuncAnimation(
                self.fig,
                self.update_graph,
                frames = range(len(self.intArray.fullCopies)),
                interval = int(self.speed.get()),
                blit = True,
                repeat = False)
        except:
            print("Start animation failed.")
        self.running = True
        self.button.config(text = "Pause")
        self.animation._start()
    
    # function called on every frame update
    def update_graph(self, frame):
        
        # look at the state at each frame and update entire graph
        try:
            for rectangle, height in zip(self.rectangles.patches, self.intArray.fullCopies[frame]):
                rectangle.set_height(height)
                rectangle.set_color("#%02x%02x%02x" % self.element_to_rgb(height, self.getRGB()))
            return (*self.rectangles,)
        except:
            print("Animation interrupted.")

def main():

    # create tkinter interface
    root = tk.Tk()
    root.title("Sorting Algorithm Visualiser")

    # create main window
    window = Window(root)
    window.pack()

    root.mainloop()

if __name__ == "__main__":
    main()