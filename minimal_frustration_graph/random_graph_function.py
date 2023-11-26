import random

def generate_random_graph(n, p):
    """Generates a random graph with the user input number of vertices."""

    graph = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                graph[i][j] = graph[j][i] = 1

    return graph

valid_input = False

while not valid_input:
    num_vertices = int(input("Enter a desired number of vertices between 2 and 75 for your random graph: "))
    probability = 0.6

    if num_vertices < 2 or num_vertices > 75:
        print("The number of vertices must be between 2 and 75.")
    else:
        valid_input = True

random_graph = generate_random_graph(n=num_vertices, p=probability)

print(random_graph)
