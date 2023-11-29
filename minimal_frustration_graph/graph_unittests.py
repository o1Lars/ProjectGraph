import unittest
from graph import GraphCreater

# tests the update_graph_connection function
class test_update_graph_connection(unittest.TestCase):

    def test_connected_graph(self):
        graph_creator = GraphCreater(edges=[(1, 2), (2, 3), (3, 1)], color_pattern=0)
        result = graph_creator.update_graph_connection()
        self.assertTrue(result, "Fail: is not True")

    def test_disconnected_graph(self):
        graph_creator = GraphCreater(edges=[(1, 2), (3, 4)], color_pattern=0)
        result = graph_creator.update_graph_connection()
        self.assertFalse(result, "Fail: is not False")


    def test_empty_graph(self):
        graph_creator = GraphCreater(edges=[], color_pattern=0)
        result = graph_creator.update_graph_connection()
        self.assertIsNone(result, "Fail: is not None")

class test_update_vertex_frustration(unittest.TestCase):

    def mock_local_metric_input(self, c_i, n_j):
        # mock of total local_metric method for testing
        total_frustration = 0.0
        for c_j in n_j:
            total_frustration += (1 - 2 * c_i) * (1 - 2 * c_j)
        return total_frustration

    def test_update_vertex_frustration(self):
        # Arranging variables
        vertices_list = [1, 2, 3, 4]
        vertices_neighbours = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [3, 2]}
        vertices_color = {1: 'red', 2: 'blue', 3: 'green'}

        # Mock the local_metric function for testing purposes
        def test_local_metric():
            graph_creator = GraphCreater(edges=[(1, 2), (2, 3), (3, 1)], color_pattern=0)
            vertex_color = 1
            neighbor_colors = [0, 1, 0]

            #compares results to actual expected_results
            result = self.mock_local_metric_input(vertex_color, neighbor_colors)
            expected_result = graph_creator.local_metric(vertex_color, neighbor_colors)
            self.assertEqual(result, expected_result, "Mock and actual local_metric results differ")

        test_local_metric()
if __name__ == '__main__':
    unittest.main()