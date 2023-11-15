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

# Import modules
from minimal_frustration_graph import visualiser_rndgraph as vrg
from project_graph import GUI_Graph_Frustration as GUI
import random as random


# test


# Create GUI for the user to operate the program

# GUI Setup:
# - Input graph from file
# - - specify file path
# - - try/except error handling - > incomplete lines etc.
# - - File must conform to following standard:
# - - - Non-empty line represents edge of the graph (site) -> identified by two integers seperated by a comma
# - - - The two integers represents the relationship between two vertices
# - Pseudo random graph generation
# - - User input number of site, rest random generated
# - - - Verify graph if fully connected
# - Initial color pattern
# - - All 1
# - - All 0
# - - All random
# - Update procedure picked by user
# - - number of iterations
# - - procedure:
# - - - Ordered
# - - - MaxViolation
# - - - MonteCarlo
# - Run program/simulation for frustration
# - - If everything went OK -> proceed to update ELSE -> ask for new input
# - Quit/exit program


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
#
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
#
# =============================================================================
# run simulation according to update protocol
# - Iterate over graph list
# - - Store local metric
# - - store global metric

# Show user live update of graph coloring scheme

# End of program, show final analysis graph of frustration

# Allow user to run new simulation or quit program.

# Import doctest module
if __name__ == "__main__":
    import doctest
    doctest.testmod()
