import random

def generate_random_graph(n, p=0.6):
    """Generates a random graph with the user input number of vertices."""

    # Randomly assign connection between vertices
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                graph[i][j] = graph[j][i] = 1

    # Create list of edges
    edges = []

    for i in range(len(graph)):
        for j in range(i + 1, len(graph[i])):
            if graph[i][j] == 1:
                edges.append((i, j))

    return edges

print(generate_random_graph(6))