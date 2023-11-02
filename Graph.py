def UpdateGraph(input_graph, updating_procedure):
	if updating_procedure == 1:
		updated_graph, update_history = Ordered_update(input_graph)
	if updating_procedure == 2:
		updated_graph, update_history = Maxviolation_update(input_graph)
	if updating_procedure == 3:
		updated_graph, update_history = Montecarlo_update(input_graph)
	return updated_graph, update_history

def Display(input_graph):
	#Insert code for displaying single graph using visualiser_rndgraph.py
	return

def Simulate_and_display(input_graph):
	ordered_graph, ordered_update_history = Ordered_update(input_graph)
	maxviolation_graph, maxviolation_update_history = Maxviolation_update(input_graph)
	montecarlo_graph, montecarlo_update_history = Montecarlo_update(input_graph)
	#insert codo for plotting all update_histories (probably using pyplot or similiar library)
	return

def Ordered_update(input_graph):
	# do simulation, and return final graph + update_history
	# final graph contains colours, and edges of final graph.
	# update_history contains list of the global metric of frustration (H)
	return final_graph, update_history
def Maxviolation_update(input_graph):
	# do simulation, and return final graph + update_history
	# final graph contains colours, and edges of final graph.
	# update_history contains list of the global metric of frustration (H)
	return final_graph, update_history
def Montecarlo_update(input_graph):
	# do simulation, and return final graph + update_history
	# final graph contains colours, and edges of final graph.
	# update_history contains list of the global metric of frustration (H)
	return final_graph, update_history

		