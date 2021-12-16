import tkinter as tk
from tkinter import OptionMenu
from tkinter import StringVar

class Window(tk.Frame):
    def __init__(self, master = None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        buttonFrame = tk.Frame(self)
        buttonFrame.pack()

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