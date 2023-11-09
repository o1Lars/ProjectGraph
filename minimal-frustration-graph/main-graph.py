"""
This program finds a colouring pattern that minimizes the “frustration” of the graph which is either provided by the,
or randomly generated

Requirements
------------
Package matplotlib https://matplotlib.org/ which can be installed via PIP.
Package networkx https://networkx.org/ which can be installed via PIP.
Python 3.7 or higher.


Notes
-----
This program is devoped as a group project as part of the exam DS830 Introduction to Programming fall 2023.
"""
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
