import matplotlib.pyplot as plt
import networkx as nx
import random
from visualiser_rndgraph import Visualiser

# Open the text file in read mode
try:
    with open('graph2.dat', 'r') as file:
        # Read lines from the file and remove whitespaces
        lines = [line.strip() for line in file.readlines() if line.strip()]
except FileNotFoundError:
    print("Error: The file could not be found.")
except IOError:
    print("There was an error reading from the file.")

# Create an empty directed graph
G = nx.Graph()

# Iterate through the lines and add edges to the graph
edges_list = []
for line in lines:
    # Ignore lines starting with #
    if line.startswith('#'):
        continue
    # Split the line by comma
    nodes = line.split(',')
    # Check if both values are valid integers
    if len(nodes) == 2 and nodes[0].strip().isdigit() and nodes[1].strip().isdigit():
        # Convert nodes to integers and add the edge to the graph
        u, v = map(int, nodes)
        G.add_edge(u, v)
        # Add the edge as a tuple to the edges_list
        edges_list.append((u, v))
    else:
        print("Invalid input.")


# Create three graphs from the graph G
G_0 = G.copy()
G_1 = G.copy()
G_random = G.copy()

# Assign colour 0 to all vertices in G_0
colour_pattern0 = {vertex: 0 for vertex in G.nodes}
nx.set_node_attributes(G_0, colour_pattern0, 'color')

# Assign colour 1 to all vertices in G_1
colour_pattern1 = {vertex: 1 for vertex in G.nodes}
nx.set_node_attributes(G_1, colour_pattern1, 'color')

# Assign random floats in the range [0, 1] to all vertices in G_random
random.seed(10)
colour_pattern_random = {vertex: random.uniform(0, 1) for vertex in G.nodes}
nx.set_node_attributes(G_random, colour_pattern_random, 'color')

# Creating a list of vertices
vertices_list_G0 = list(G_0.nodes())
vertices_list_G1 = list(G_1.nodes())
vertices_list_random = list(G_random.nodes())

# Getting adjacency dictionary
adjacency_dict_G0 = dict(G_0.adjacency())
adjacency_dict_G1 = dict(G_1.adjacency())
adjacency_dict_G_random = dict(G_random.adjacency())

# Identifying neighbours for each vertex
neighbours_dict_G0 = {vertex: list(neighbours.keys()) for vertex, neighbours in adjacency_dict_G0.items()}
neighbours_dict_G1 = {vertex: list(neighbours.keys()) for vertex, neighbours in adjacency_dict_G1.items()}
neighbours_dict_G_random = {vertex: list(neighbours.keys()) for vertex, neighbours in adjacency_dict_G_random.items()}


# Check if graph is connected
def is_graph_connected(graph):
    """This function checks if a given graph is connected, returns True or False accordingly."""
    return nx.is_connected(graph)

is_connected = is_graph_connected(G)

if is_connected:
    print("The graph is connected.")
else:
    print("The graph is not connected.")


#
# Simulation

def local_metric(c_i, N_j):
    """This function calculates the frustration of a site using the colour of the site and the sum of the colours of all its neighbours."""
    total_frustration = 0.0
    for c_j in N_j:
        total_frustration += (1 - 2 * c_i) * (1 - 2 * c_j)
    return total_frustration

# Store frustration of all vertices from local_metric function in a list
frustration_list = []

for node in G_random.nodes():
    c_i = G_random.nodes[node]['color']
    N_J = [G_random.nodes[neighbour]['color'] for neighbour in neighbours_dict_G_random[node]]
    frustration = local_metric(c_i, N_J)
    frustration_list.append(frustration)
    print(f"Frustration for Node {node}: {frustration}")


def global_metric(sum_of_local_metrics):
    """This function calculates the global metric from a list of local metrics."""
    H = 0.5 * sum(sum_of_local_metrics)
    return H

H = global_metric(frustration_list)

print(H)

print(G_0.number_of_nodes())
print(vertices_list_G0)

nx.draw_networkx(G_1, node_size=700)

plt.show()