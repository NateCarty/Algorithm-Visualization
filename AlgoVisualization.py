import matplotlib

# We need to change the default backend to "TkAgg"
matplotlib.use("TkAgg")

# import the figure canvas for tkagg and a navigation bar
from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2TkAgg

# import regular Figure
from matplotlib.figure import Figure