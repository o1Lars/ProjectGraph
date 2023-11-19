"""
This program finds a colouring pattern that minimizes the “frustration” of the graph which is either provided by the,
or randomly generated

Requirements
------------
Package matplotlib https://matplotlib.org/ which can be installed via PIP.
Package networkx https://networkx.org/ which can be installed via PIP.
Package random
Module visualiser_rndgraph.py   ### add file path
Module graph.py from            ### add file path
Python 3.7 or higher.


Notes
-----
This program is devoped as a group project as part of the exam DS830 Introduction to Programming fall 2023.
"""
import os
import sys

# Get the directory of the current script
script_path = sys.argv[0] if hasattr(sys, 'frozen') else __file__
current_dir = os.path.dirname(os.path.abspath(script_path))

# Append the parent directory to sys.path to enable relative imports
sys.path.append(os.path.dirname(current_dir))

# Import dependencies
from minimal_frustration_graph import visualiser_rndgraph as vrg
from minimal_frustration_graph import graph as g
import random as random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
import tkinter.filedialog as filedialog

_debug = True  # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = Toplevel1(_top1)
    root.mainloop()


_script = sys.argv[0]
_location = os.path.dirname(_script)

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40'  # X11 color: #666666
_ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
_ana2color = 'beige'  # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'

#############################################################################################################
##################################### CODE BELOW CONTAINS INPUT VARIABLES ###################################
#############################################################################################################

class Toplevel1:
    #Below is all button functions
    #This button function browses file dialog and posts the filepath into entry1
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.Entry1.delete(0, tk.END)
            self.Entry1.insert(0, file_path)

    def generate_graph(self):
        # random check button
        random_is_checked = self.che51.get()
        # get number of sites when random checked
        num_of_sites = self.Entry2.get()
        # get color pattern
        color_pattern = self.Spinbox1.get()
        # get update procedure
        update_procedure = self.Spinbox2.get()
        # get number of iterations
        number_of_iterations = int(self.Entry3.get())


        # Store graph edges in list of tuples
        graph_edges_list = []

        # if random is checked, generate random graph edge list
        if random_is_checked == 1:
            graph_edges_list = generate_random_graph(num_of_sites)
        else:  # get file from program
            file_from_path = self.Entry1.get()
            graph_edges_list = create_graph_from_file(r"" + file_from_path)
        # check that graph is connected

        test_graph = g.Graph(graph_edges_list, color_pattern)

        for num in range(number_of_iterations):
            test_graph.update_ordered()
            print(test_graph.total_frustration)

        test_graph.report_frustration_history(11)

        # create new Graph class with vertices, edges, color and frustration


        # create instance of graph
        # graph_instance = vrg.Visualiser(graph_edges_list, val_map=colors_dict)

        # simulate update procedure
        print("update_procedure is:", update_procedure)
        print("color pattern is", color_pattern)
        
        print(graph_edges_list)
    

#############################################################################################################
############## ALL CODE BELOW THIS POINT IS PURELY VISUAL, PLACEMENT, SHAPE, COLORS, ETC ####################
#############################################################################################################
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("415x413+475+195")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("GUI Graph Frustration")
        top.configure(background="#46aefb")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        self.che51 = tk.IntVar()

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=0.145, relheight=1.281, relwidth=1.082)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.022, rely=0.019, height=26, width=210)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 14")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Graph configurations''')
        self.Checkbutton1 = tk.Checkbutton(self.Frame1)
        self.Checkbutton1.place(relx=0.423, rely=0.189, relheight=0.06
                , relwidth=0.18)
        self.Checkbutton1.configure(activebackground="beige")
        self.Checkbutton1.configure(activeforeground="black")
        self.Checkbutton1.configure(anchor='w')
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(compound='left')
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(font="-family {Segoe UI} -size 10")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#c0c0c0")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(selectcolor="#ffffff")
        self.Checkbutton1.configure(text='''Check''')
        self.Checkbutton1.configure(variable=self.che51)
        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.067, rely=0.189, height=28, width=149)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 10")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Generate random graph:''')
        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.067, rely=0.113, height=26, width=121)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 10")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Enter file directory:''')
        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.668, rely=0.265, height=20, relwidth=0.076)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="-family {Courier New} -size 10")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.067, rely=0.265, height=26, width=267)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Segoe UI} -size 10")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''If random graph checked, enter num of sites:''')
        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.067, rely=0.34, height=27, width=141)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Segoe UI} -size 10")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Choose color pattern:''')
        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.067, rely=0.378, height=52, width=162)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Segoe UI} -size 10")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Choose update procedure:''')
        self.Spinbox1 = tk.Spinbox(self.Frame1, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.445, rely=0.34, relheight=0.045
                , relwidth=0.192)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font="-family {Segoe UI} -size 10")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.value_list = ['All 0','All 1','All random',]
        self.Spinbox1.configure(values=self.value_list)
        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.067, rely=0.548, height=44, width=357)
        self.Button1.configure(command=self.generate_graph)  # Set the command to the generate_graph method
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 12")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Generate Graph''')
        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.78, rely=0.113, height=24, width=47)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=self.browse_file)  # Set the command to the browse_file function
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Browse''')
        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.423, rely=0.113, height=20, relwidth=0.343)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Label8 = tk.Label(self.Frame1)
        self.Label8.place(relx=0.067, rely=0.473, height=21, width=144)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Segoe UI} -size 10")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Enter num of iterations:''')
        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.445, rely=0.473, height=20, relwidth=0.076)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="-family {Courier New} -size 10")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Spinbox2 = tk.Spinbox(self.Frame1, from_=1.0, to=100.0)
        self.Spinbox2.place(relx=0.445, rely=0.416, relheight=0.036
                , relwidth=0.234)
        self.Spinbox2.configure(activebackground="#f9f9f9")
        self.Spinbox2.configure(background="white")
        self.Spinbox2.configure(buttonbackground="#d9d9d9")
        self.Spinbox2.configure(disabledforeground="#a3a3a3")
        self.Spinbox2.configure(font="-family {Segoe UI} -size 10")
        self.Spinbox2.configure(foreground="black")
        self.Spinbox2.configure(highlightbackground="black")
        self.Spinbox2.configure(highlightcolor="black")
        self.Spinbox2.configure(insertbackground="black")
        self.Spinbox2.configure(selectbackground="#c4c4c4")
        self.Spinbox2.configure(selectforeground="black")
        self.value_list = ['Ordered','MaxViolation','MonteCarlo',]
        self.Spinbox2.configure(values=self.value_list)
        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.19, rely=0.024, height=43, width=319)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#46aefb")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 22 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#46aefb")
        self.Label1.configure(highlightcolor="#ffffff")
        self.Label1.configure(text='''Graph Frustration''')
        self.menubar = tk.Menu(top,font="TkMenuFont",bg='#ed6754',fg=_fgcolor)
        top.configure(menu = self.menubar)

    def popup1(self, event, *args, **kwargs):
        self.Popupmenu2 = tk.Menu(self.top, tearoff=0)
        self.Popupmenu2.configure(background=_bgcolor)
        self.Popupmenu2.configure(foreground=_fgcolor)
        self.Popupmenu2.configure(activebackground=_ana2color)
        self.Popupmenu2.configure(activeforeground='black')
        self.Popupmenu2.configure(font="TkMenuFont")
        self.Popupmenu2.post(event.x_root, event.y_root)


def add_edges_from_lines(lines: str) -> list[tuple]:
    """Read lines, check if line represent an edge of a graph.
    Return list of edges

    ## implement tests
    """
    # Store edges in a list
    edges_list = []

    # Iterate through the lines and add edges to the graph
    for line in lines:
        # Ignore lines starting with #
        if line.startswith('#'):
            continue

        # Split the line by comma
        nodes = line.split(',')

        # Remove '()' from nodes
        for i in range(len(nodes)):
            nodes[i] = nodes[i].replace('(', '')
            nodes[i] = nodes[i].replace(')', '')

        # Check if both values are valid integers
        if len(nodes) == 2 and nodes[0].strip().isdigit() and nodes[1].strip().isdigit():
            # Convert nodes to integers and add the edge to the graph
            u, v = map(int, nodes)
            # Add the edge as a tuple to the edges_list
            edges_list.append((u, v))
        else:
            print("Invalid input.")

    return edges_list


def create_graph_from_file(file_path: str) -> list[tuple]:
    """Read a file, checks if its valid and return a list of edges for a graph

    ## implement tests
    """
    # Open the text file in read mode
    try:
        with open(file_path, 'r') as file:
            # Read lines from the file and remove whitespaces
            lines = [line.strip() for line in file.readlines() if line.strip()]
    # Handle errors
    except FileNotFoundError:
        print("Error: The file could not be found.")
    except IOError:
        print("There was an error reading from the file.")

    # add edges from file to edges_list
    graph_edges = add_edges_from_lines(lines)

    return graph_edges



    





# =============================================================================
# For testing purpose to see, how visualiser creates a graph and visualises color update.
# Incomplete code
# 
# 
# test_graph = create_graph_from_file(r"C:\Users\Chris\ProjectGraph\test_graph_1.txt")
# print(test_graph)
# this_test = vrg.Visualiser(test_graph, val_map={1: 0.0, 2: 0.0, 8: 1.0, 12: 1.0})
# 
# for i in range(10):
#     this_dict = {
#         1: random.random(),
#         2: random.random(),
#         8: random.random(),
#         12: random.random(),
#         }
#     vrg.Visualiser.update(this_test, val_map=this_dict)
# =============================================================================

# run simulation according to update protocol
# - Iterate over graph list
# - - Store local metric
# - - store global metric

# Show user live update of graph coloring scheme

# End of program, show final analysis graph of frustration

# Allow user to run new simulation or quit program.
def start_up():
    main()

if __name__ == '__main__':
    main()
# Import doctest module
if __name__ == "__main__":
    import doctest
    doctest.testmod()
