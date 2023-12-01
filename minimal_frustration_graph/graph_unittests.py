import unittest
from graph import GraphCreater, GraphSimulator, create_graph_from_file

# tests the function that creates graph from an external file
class TestCreateGraphFromFile(unittest.TestCase):
    # First test - valid test
    def test_valid_file(self):
        # Load a temporary file with mock data
        mock_file_path = 'mock_file.txt'
        mock_data = "1, 2\n2, 3\n3, 1\n"
        with open(mock_file_path, 'w') as file:
            file.write(mock_data)

        # Store result of the function
        result = create_graph_from_file(mock_file_path)

        # Determine result from loading mock data
        expected_result = [(1, 2), (2, 3), (3, 1)]

        # Confirm result = expected_result
        self.assertEqual(result, expected_result, "Graph edges mismatch")

    # Second test - invalid test
    def test_invalid_file(self):
        # Store result of the function for a non-existent file
        result = create_graph_from_file('nonexistent_file.txt')

        # Confirm the result is empty since file is invalid
        self.assertEqual(result, [], "Invalid file should return an empty list")

if __name__ == '__main__':
    unittest.main()

# tests the update_graph_connection function
class TestUpdateGraphConnection(unittest.TestCase):

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

# tests the update frustration of graph method from class GraphSimulator
class TestUpdateVertexFrustration(unittest.TestCase):

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

# Tests the local metric from GraphSimulator
class TestLocalMetric(unittest.TestCase):
    def test_local_metric(self):
        # Setup for test
        graph_simulation = GraphCreater([(1, 2), (2, 3), (3, 1)], color_pattern=0)
        c_i = 0
        n_j = [0, 1, 0]
        expected_result_frustration = 0.0
        for c_j in n_j:
            expected_result_frustration += (1 - 2 * c_i) * (1 - 2 * c_j)

        # Calling and comparing results with actual local_metric
        result_test_frustration = graph_simulation.local_metric(c_i, n_j)
        self.assertEqual(result_test_frustration, expected_result_frustration, "Local metric results differ")

# test class GraphSimulator and methods
class TestGraphSimulator(unittest.TestCase):

    def setUp_test_graph(self):
        # Create an instance of the GraphSimulator for testing
        test_graph = GraphCreater([(0, 1), (0, 3), (0, 4), (0, 5), (1, 2), (1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)], 'All 0')

        return test_graph

    def test_update_ordered(self):
        test = self.setUp_test_graph()
        test.update_ordered()

        # check list of all vertex colors
        expected_valmap = {0: 1.0, 1: 1.0, 3: 1.0, 4: 0, 5: 0, 2: 1.0}
        self.assertEqual(test.val_map, expected_valmap, ' Not equal')

        # check list of all frustrations
        expected_frustration = {0: 0.0, 1: 0.0, 3: -1.0, 4: -3.0, 5: -3.0, 2: -1.0}
        self.assertEqual(test.vertices_frustration, expected_frustration, ' Not equal')
        
    def test_update_max_violation(self):
        test = self.setUp_test_graph()
        test.update_max_violation()


        # check list of all vertex colors
        expected_valmap = {0: 0, 1: 0, 3: 0, 4: 1.0, 5: 0, 2: 0}
        self.assertEqual(test.val_map, expected_valmap, ' Not equal')

        # check list of all frustrations
        expected_frustration = {0: 2.0, 1: 2.0, 3: 1.0, 4: -5.0, 5: 3.0, 2: 1.0}
        self.assertEqual(test.vertices_frustration, expected_frustration, ' Not equal')

    def test_update_monte_carlo(self):
        test = self.setUp_test_graph()
        test.update_monte_carlo()


        # check list of all vertex colors
        expected_valmap = {0: 1.0, 1: 1.0, 3: 1.0, 4: 0, 5: 0, 2: 1.0}
        self.assertEqual(test.val_map, expected_valmap, ' Not equal')

        # check list of all frustrations
        expected_frustration = {0: 0.0, 1: 0.0, 3: -1.0, 4: -3.0, 5: -3.0, 2: -1.0}
        self.assertEqual(test.vertices_frustration, expected_frustration, ' Not equal')

    def test_run_simulation(self):
        # test graphs
        test_ordered = self.setUp_test_graph()
        test_max_violation = self.setUp_test_graph()
        test_monte_carlo = self.setUp_test_graph()

        # update Orderred
        test_ordered.run_simulation('ordered', 1)

        # store expected results
        expected_valmap = {0: 1.0, 1: 1.0, 3: 1.0, 4: 0, 5: 0, 2: 1.0}
        expected_total_frustration = [12.0, -4.0]

        # compare
        self.assertEqual(test_ordered.val_map, expected_valmap, 'Not equal')
        self.assertEqual(test_ordered.total_frustration, expected_total_frustration, 'Not equal')

        # update MaxViolation
        test_max_violation.run_simulation('maxviolation', 1)

        # store expected results
        expected_valmap = {0: 0, 1: 0, 3: 0, 4: 1.0, 5: 0, 2: 0}
        expected_total_frustration = [12.0, 2.0]

        # compare
        self.assertEqual(test_max_violation.val_map, expected_valmap, 'Not equal')
        self.assertEqual(test_max_violation.total_frustration, expected_total_frustration, 'Not equal')

        # update MonteCarlo
        test_monte_carlo.run_simulation('montecarlo', 1)

        # store expected results
        expected_valmap = {0: 1.0, 1: 1.0, 3: 1.0, 4: 0, 5: 0, 2: 1.0}
        expected_total_frustration = [12.0, -4.0]

        # compare
        self.assertEqual(test_monte_carlo.val_map, expected_valmap, 'Not equal')
        self.assertEqual(test_monte_carlo.total_frustration, expected_total_frustration, 'Not equal')



if __name__ == '__main__':
    unittest.main()
