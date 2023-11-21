import random
import math

def monte_carlo(self) -> None:
    """Visit each site of the graph and swap colour if the exponential of the local action > a random float between 0,1.
    Parameters
    ----------
    graph : list
        DESCRIPTION. # TODO

    # add tests
    """
    vertices_list = self.vertices_list
    vertices_frustration = self.vertices_frustration
    val_map = self.val_map

    # iterate over vertices in vertices_dictionary
    for vertex in vertices_list:
        # set local action for each vertex
        local_action = vertices_frustration[vertex]
        if local_action > 0:
            current_color = val_map[vertex]  # set current color
            random_number = random.uniform(0, 1)  # generate random float between 0 and 1
            exp_local_action = math.exp(local_action)

            if exp_local_action > random_number: #compare exponent to random number
                new_color = 1.0 if current_color != 1.0 else 0.0 # swap current colour
                val_map[vertex] = new_color
                self.update_vertex_frustration()  # update vertices frustration
                print("The colours of the sites have been swapped.")


