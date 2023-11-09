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


def global_metric(Graph: list):
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


def ordered(graph: list) -> list:
    """
    Visit each site of the graph and change (swap) the colour if the local action of the site is negative

    Parameters
    ----------
    graph : list
        DESCRIPTION. # TODO

    # add tests
    """
    # TOOD
    print("the colors of the sites have been swapped")


def max_violation(graph: list) -> list:
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


def monte_carlo(graph: list) -> list:
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

# TODO
# Store total frustration after each simulation


# Import doctest module
if __name__ == "__main__":
    import doctest
    doctest.testmod()
