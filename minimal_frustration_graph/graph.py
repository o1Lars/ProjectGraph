"""
This module provides Graph, a class for creating a graph of edges and sites forming the graph

Requirements
------------
Package matplotlib https://matplotlib.org/ which can be installed via PIP.
Package networkx https://networkx.org/ which can be installed via PIP.
Python 3.7 or higher.

Notes
-----
Module is created as part of the group project for the final exam of DS830 Introduction to programming.
"""


import matplotlib.pyplot as plt
from __future__ import annotations  # to use a class in type hints of its members
from typing import List, Optional, Dict
import random as random

# Create class Graph


class Graph:
    """Each instance of this class creates a Graph with edges, vertices and a coloring pattern. Furthermore,
    each instance has methods for calculating local site frustration, global frustration and updating color patterns
    according to three different update methods: Ordered, MaxViolation and MonteCarlo
    """

    def __init__(self,
                 edges: list,
                 color_pattern: int,
                 vertices: Optional[dict] = {}) -> None:
        """
        Parameters
        ----------
        edges: List[(int,int)]
          List containing the edges (Tuples of 2 vertices) forming the 2D surface for the simulation.
        val_map: Dict[int:float]
          Dictionary containing the color of each vertex (expressed as a float)
        def_col:
          Color of the vertices not reported in val_map
        node_size: int, default 500
          Control the size of the drawn nodes
        window_title : Optional[str], default = None
          The title of the window.
        """
        self.edges = edges
        self.color_pattern = color_pattern
        self.vertices = self.create_graph_dict(self.edges, self.color_pattern)


    # class methods
    def create_color_dict_from_edges(self, edges: list[tuple], color_pattern) -> dict:
        """ Return dictionairy edges with colors
        """
        # TODO
        print("Dictionairy of colors created")


    def create_graph_dict(self, edges: list[tuple], color_pattern: int) -> dict:
        """Creates a dictionairy of vertices from edges and a color pattern.
        """
        # Create dict and vertices
        graph_dict = {}
        graph_vertices = []

        # Iterate over edges_list and append vertex
        for edge_tuple in edges:
            x, y = edge_tuple  # Unpack the tuple into x and y
            # check if vertices already in graph_dict
            if x not in graph_vertices:
                graph_vertices.append(x)
            if y not in graph_vertices:
                graph_vertices.append(y)

        # Add vertex to graph_dict
        for vertex in graph_vertices:
            graph_dict[vertex] = {}

        # Add color pattern to vertex
        for vertex in graph_dict:
            # add color pattern to vertex
            if color_pattern == 0 or color_pattern == 1:
                graph_dict[vertex]["color"] = color_pattern
            else:  # if color pattern not 0 or 1, randomly assign color value
                color = random.randint(0, 1)
                graph_dict[vertex]["color"] = color

        return graph_dict



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
