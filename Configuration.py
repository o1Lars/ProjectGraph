
def Read_text_file_into_list_of_tuples(path_to_text_file):
	#data = []
	#with open(path_to_text_file, 'r') as file:
	#	for line in file:
	#		values = line.strip()[1:-1].split(',')
	#		data.append((int(values[0]), int(values[1])))
	return data

def Verify_that_graph_is_connected(tuple_of_edges):
	# Check if any edges are unconnected
	# set boolean is_connected to true if connected
	# Else set is_connected to false
	# return is_connected
	return is_connected

def Get_sites_from_list_of_tuples(list_of_tuples):
	# code to get unique sites
	return list_of_sites

def Get_sites_from_list_of_tuples(list_of_tuples):
	# code to get unique sites
	return list_of_sites


def Colour_sites(tuple_of_edges, sites, initial_colouring_pattern):
	# Colour
	if initial_colouring_pattern==1:
		coloured_graph = Colour_all_zero(tuple_of_edges, sites)
	if initial_colouring_pattern==2:
		coloured_graph = Colour_all_one(tuple_of_edges, sites)
	if initial_colouring_pattern==3:
		coloured_graph = Colour_random(tuple_of_edges, sites)
	return coloured_graph

def Colour_all_zero(tuple_of_edges, sites):
	return coloured_graph

def Colour_all_one(tuple_of_edges, sites):
	return coloured_graph

def Colour_all_random(tuple_of_edges, sites):
	return coloured_graph
