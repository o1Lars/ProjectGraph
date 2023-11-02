import unittest
import Configuration

class ConfigurationTests(unittest.TestCase):
	def setUp(self):
		#Some code
		self.test_text_file_path = "test_graph_1.txt"

	#def test_GenerateGraph(self):
	#	pass

	def test_read_text_file_into_list_of_tuples(self):
		#Arrange
		expected_list = [(1,2),(2,8),(8,1),(1,12)] 
		#Act
		actual_list = Configuration.Read_text_file_into_list_of_tuples("test_graph_1.txt")
		#Assert
		self.assertEqual(expected_list, actual_list)
	

if __name__ == "__main__":
	unittest.main()
