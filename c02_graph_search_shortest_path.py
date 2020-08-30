# Graph Search, Shortest Paths, and Data Structures
# https://www.coursera.org/learn/algorithms-graphs-data-structures

import sys

# week 1
def kosaraju(graph):
	"""
	Computes strongly connected components of a given graph using Kosaraju's algorithm
		Parameters:
			graph (DirectedGraph): A directed graph
		Returns:
			scss (dict): A dictionary containing all the SCCs of the graph
						 The keys of the graph are the leaders of every SCC
						 The values are the vertices belonging to that SCC
	"""
	global t
	global s
	t = 0
	s = None
	ordering = {}
	rev = graph.reverse()

	def dfs(g, start_vertex, visited, sccs = None):
		global t
		visited.add(start_vertex)
		# collect the resulting SCCs into a dictionary
		if sccs != None:
			if s not in scss:
				scss[s] = []	
			scss[s].append(start_vertex)
		vertices = g.get_vertices()
		edges = vertices[start_vertex]
		for w in edges:
			if w not in visited:
				dfs(g, w, visited, sccs)
		t += 1
		ordering[t] = start_vertex
	
	# populate the ordering table with the finishing time of each vertex
	visited = set()
	vertices = rev.get_vertices()
	reverse_sorted_vertices = sorted(vertices.keys(), reverse=True)
	for v in reverse_sorted_vertices:
		if v not in visited:
			dfs(rev, v, visited)

	visited = set()
	scss = {}
	# iterate over vertices sorted according to finishing values
	for key in sorted(ordering.keys(), reverse=True):
		value = ordering[key]
		if value not in visited:
			s = value
			dfs(graph, value, visited, scss)

	return scss

# week 2
def dijkstra(graph, source_vertex, max_value = sys.maxsize):
	"""
	Computes the shortest path for the source vertex
	Assumes non-negative edge-lengths
		Parameters:
			graph (WeightedGraph): A weighted graph
			source_vertex (str): The source vertex for which to compute the shortest path to every other vertex
			max_value (int): The value to use as the base distance between two vertices
		Returns:
			path_lengths (dict): A dictionary of path lengths from source vertex to every other vertex
	"""
	assert source_vertex in graph.get_vertices()

	path_lengths = {}
	vertices = graph.get_vertices()
	weights = graph.get_weights()
	path_lengths[source_vertex] = 0

	for key in vertices:
		minimum = max_value
		edges = vertices[key]
		for edge in edges:
			weight_key = graph.get_weight_key(key, edge)
			weight = weights[weight_key]
			if weight < minimum:
				score = path_lengths[key] if key in path_lengths else 0
				path_lengths[edge] = score + weight
			minimum = min(minimum, weight)
		
	return path_lengths
