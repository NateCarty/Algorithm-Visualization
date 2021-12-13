import matplotlib

# We need to change the default backend to "TkAgg"
matplotlib.use("TkAgg")

# import the figure canvas for tkagg and a navigation bar
from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2Tk

# import regular Figure
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk

class AlgoVisualization(tk.Tk):

    # initialize main app
    def __init__(self, *args, **kwargs):

        # initialize tkinter with given args
        tk.Tk.__init__(self, *args, **kwargs)

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
            

class graphPage(tk.Frame):

    def __init__(self, parent, controller):
        
        # inititialize frame
        tk.Frame.__init__(self, parent)

        # create label for current algorithm
        exampleAlgo = "Insertion"
        label = tk.Label(self, text= f"{exampleAlgo} Algorithm!")
        label.pack(pady=10, padx=10)

        # insert live matplotlib graph here


app = AlgoVisualization()
app.mainloop()
