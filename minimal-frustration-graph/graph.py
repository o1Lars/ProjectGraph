"""
A module for simulating frustration an a graph.

Module holds various graphing functions for the program minimal frustration of a random graph.

Requirements
------------
Package matplotlib https://matplotlib.org/ which can be installed via PIP.
Package networkx https://networkx.org/ which can be installed via PIP.
Python 3.7 or higher.

Notes
-----
Module is created as part of the group project for the final exam of DS830 Introduction to programming.
"""

# Import requirements
import matplotlib.pyplot as plt
import matplotlib as mpl
import networkx as nx
import numpy as np

# local metric function


def local_metric(c_i: int, N_J: int) -> float:
    """
    Return  the frustration of a site

    TODO:   add tests
            add assumptions

    Parameters
    ----------
    """

    # Store local metric total
    total = 0

    # Iterate
    for j in range(1, N_J + 1):
        total += (1 - 2 * c_i) * (1 - 2 * (1 - j))
    return total
    # TODO -> Add so this function properly adds the total to list for storing the values through the iteration
    # Possibly not part of function but added when calling the function

# global metric function


def global_metric(graph: list):
    """
    Return the sum of the local_metric over every single vertex of the graph.
    The global metric is the measure of the frustration of the graph simulated by the program.

    TODO:   add tests
            add assumptions

    Parameters
    ----------
    """

    # Store total frustration
    total_frustration = 0

    # iterate over list/set of site frustations and add them to total frustration
    # TODO

    # Multiply total_frustration by 1/2 as per the provided formula.
    total_frustration *= 0.5


def calculate_local_action(graph, vertex):
    """ Visit each site of the graph and change (swap) the colour if the local action of the site is negative
    Parameters
    ----------
    graph : TYPE
        DESCRIPTION.
    vertex : TYPE
        DESCRIPTION.

    Returns
    -------
    local_action : TYPE
        DESCRIPTION.

    ### TODO Add tests ###

    """
    # Example: Using degree as the local action
    local_action = graph.degree(vertex)
    return local_action


def ordered(graph: dict, vertex) -> dict:
    """Visit each site of the graph and change (swap) the colour if the local action of the site is negative

    Parameters
    ----------
    graph : list
        DESCRIPTION. # TODO

    # add tests
    """
    local_action = calculate_local_action(graph, vertex)
    if local_action > 0:
        # Swap color - replace this with your actual color swapping logic
        current_color = graph.nodes[vertex]['color']
        new_color = 'red' if current_color != 'red' else 'blue'
        graph.nodes[vertex]['color'] = new_color
    print("the colors of the sites have been swapped")


def max_violation(graph_dict: dict) -> dict:
    """
    Identify the site with the largest value of local action and swap its colour.

    Parameters
    ----------
    graph : list
        DESCRIPTION. # TODO

    # add tests
    """
    # TOOD
    print("the site with the largest value of the local action has had its colours swapped")


def monte_carlo(graph_dict: dict) -> dict:
    """
    Visit each site of the graph and change (swap) the colour if the exponential of the local action is greater 
    than a random number between 0 and 1

    Parameters
    ----------
    graph : list
        DESCRIPTION. # TODO

    # add tests
    """
    # TOOD
    print("the site with the largest value of the local action has had its colours swapped")


# TODO
# Store individual frustrations of a site from running the local_metric function
site_frustration = []

# TODO
# Store total frustration after each simulation
total_site_frustration = []


def global_metric_history(steps: int, frustration: list[int], update_protocol=None) -> None:
    """ Display plot of the evolution of total frustration over a specified number of steps

    Parameters
    ----------
    frustration : int
        DESCRIPTION.
    steps : int
        DESCRIPTION.
    """
    step_list = list(range(1, steps + 1))

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(step_list, frustration)  # Plot some data on the axes

    # set labels
    ax.set_ylabel("Frustration of the graph")
    ax.set_xlabel("Number of update steps")

    # Display
    plt.show()


# Import doctest module
if __name__ == "__main__":
    import doctest
    doctest.testmod()
