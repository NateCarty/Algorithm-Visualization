from tkinter import font
import matplotlib
import numpy as np
# We need to change the default backend to "TkAgg"
matplotlib.use("TkAgg")

# import the figure canvas for tkagg and a navigation bar
from matplotlib.backends.backend_tkagg import FigureCanvasAgg, FigureCanvasTkAgg, NavigationToolbar2Tk

# import regular Figure
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import tkinter as tk
from tkinter import ttk



class AlgoVisualization(tk.Tk):

    # initialize main app
    def __init__(self, *args, **kwargs):

        # initialize tkinter with given args
        tk.Tk.__init__(self, *args, **kwargs)

        fig = Figure()
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().grid(column=0, row=0)
        self.ax = fig.add_subplot(1,1,1)

        tk.Tk.wm_title(self, "Algorithm Visualization")

        # create variable for tk frame
        container = tk.Frame(self)


        # configure spacing and grid 
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # variable to store frames
        self.frames = {}

        # add all pages to storage
        for page in (homePage, graphPage):

            frame = page(container, self)

            self.frames[page] = frame

            frame.grid(row=0, column = 0, sticky="nsew")

        # show the first page
        self.show_frame(homePage)
    
    # function to change frame
    def show_frame(self, curr):

        frame = self.frames[curr]
        frame.tkraise()
class ArrayTracker():

    def __init__(self, array):
        self.array = np.copy(array)
        self.reset()

    def reset(self):
        self.indicies = []
        self.values = []
        self.access_type = []
        self.full_copies = []

    
    def track(self, key, access_type):
        self.indicies.append(key)
        self.values.append(self.array[key])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.array))

    def getActivity(self, index = None):
        if isinstance(id, type(None)):
            return [(i, op) for (i, op) in zip(self.indicies, self.access_type)]
        else:
            return (self.indicies[index], self.access_type[index])


    def __getitem__(self, key):
        self.track(key, "get")
        return self.array.__getitem__(key)

    def __setitem__(self, key, value):
        self.array.__setitem__(key, value)
        self.track(key, "set")

    def __len__(self):
        return self.array.__len__()
            
class homePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home Page")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text ="Sort",
                            command=lambda: controller.show_frame(graphPage))
        button.pack()


class graphPage(tk.Frame):

    def __init__(self, parent, controller):
        
        # inititialize frame
        tk.Frame.__init__(self, parent)

        # create label for current algorithm
        exampleAlgo = "Insertion"
        label = tk.Label(self, text= f"{exampleAlgo} Algorithm!")
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text = "Change Settings",
                            command = lambda: controller.show_frame(homePage))
        button.pack()

        # insert live matplotlib graph here

        #graph = plt.figure(figsize=(12,8), dpi=100)
        plt.rcParams["figure.figsize"] = [12, 8]
        plt.rcParams["font.size"] = 16

        elementNumber = 35

        def element_to_rgb(element):
            minRVal = 32
            maxRVal = 98
            red = int((element) / 1000 * (maxRVal - minRVal) + minRVal)
            minGVal = 6
            maxGVal = 195
            green = int((element) / 1000 * (maxGVal - minGVal) + minGVal)
            minBVal = 59
            maxBVal = 112
            blue = int((element) / 1000 * (maxBVal - minBVal) + minBVal)
            return red, green, blue

        # returns array of elementNumber elements, with values evenly
        # spaced out from 0 to 1000, rounded.
        intArray = np.round(np.linspace(4, 1000, elementNumber))

        # shuffle the array in place
        np.random.shuffle(intArray)

        intArray = ArrayTracker(intArray)

        currentAlgorithm = "Insertion"

        # test insertion sort
        def insertionSorter(intArray, currentAlgo):
            if currentAlgo == "Insertion":
                i = 1
                while i < len(intArray):
                    j = i
                    while j > 0 and intArray[j - 1] > intArray[j]:
                        intArray[j], intArray[j - 1] = intArray[j - 1], intArray[j]
                        j -= 1
                    i += 1
        insertionSorter(intArray, currentAlgorithm)
        figure, ax= plt.subplots()
        rectangles = ax.bar(np.arange(0, elementNumber, 1), intArray, align = "edge", width = .8)
        ax.set_xlim([0, elementNumber])
        ax.set(xlabel = "Index", ylabel = "Value", title = f"Sorted by {currentAlgorithm} algorithm")

        def updateFunc(frame):
            for rectangle, height in zip(rectangles.patches, intArray.full_copies[frame]):
                rectangle.set_height(height)
                rectangle.set_color("#%02x%02x%02x" % element_to_rgb(height))
                

            return (*rectangles,)
        animation = FuncAnimation(figure, updateFunc, frames = range(len(intArray.full_copies)),
                                    blit = True, interval = 1, repeat = False)
        canvas = FigureCanvasTkAgg(fig, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        #plt.show()



app = AlgoVisualization()
app.mainloop()
