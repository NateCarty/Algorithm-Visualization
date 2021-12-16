import tkinter as tk
from tkinter import OptionMenu
from tkinter import StringVar

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