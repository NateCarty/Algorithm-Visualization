import matplotlib

# We need to change the default backend to "TkAgg"
matplotlib.use("TkAgg")

# import the figure canvas for tkagg and a navigation bar
from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2Tk

# import regular Figure
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

class graphPage(tk.Frame):

    def __init__(self, parent, controller):
        
        # inititialize frame
        tk.Frame.__init__(self, parent)

        # create label for current algorithm
        exampleAlgo = "Insertion"
        label = tk.Label(self, text= f"{exampleAlgo} Algorithm!")
        label.pack(pady=10, padx=10)

        # insert live matplotlib graph here

