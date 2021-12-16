import tkinter as tk
from tkinter import OptionMenu
from tkinter import StringVar

import numpy as np

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

        buttonFrame = tk.Frame(self)
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

        # variables
        self.elementNumber = 25
        self.currentAlgorithm = "Insertion"

        # create an array of elements evenly spaced out from 1 to 1000, rounded
        intArray = np.round(np.linspace(4, 1000, self.elementNumber))

        # randomly shuffle array in place
        np.random.shuffle(intArray)

        # need a class to track our array being sorted
        self.intArray = ArrayTracker(intArray)


    # function when start button is pressed
    def on_start(self):
        return

    # funtion when reset button is pressed
    def on_reset(self):
        return



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