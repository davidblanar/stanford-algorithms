# Graph Search, Shortest Paths, and Data Structures
# https://www.coursera.org/learn/algorithms-graphs-data-structures

import sys
from graph import WeightedUndirectedGraph

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
			distances (dict): A dictionary of path lengths from source vertex to every other vertex
	"""
	vertices = graph.get_vertices()
	assert source_vertex in vertices

	def find_closest(unvisited_vertices, dist_map):
		minimum = max_value
		res = None
		for item in unvisited_vertices:
			if dist_map[item] < minimum:
				minimum = dist_map[item]
				res = item
		return res

	weights = graph.get_weights()
	unvisited = set()
	distances = {}

	for v in vertices:
		unvisited.add(v)
		distances[v] = max_value
	distances[source_vertex] = 0

	while len(unvisited) > 0:
		closest = find_closest(unvisited, distances)
		edges = vertices[closest]
		for w in edges:
			if w in unvisited:
				weight_key = graph.get_weight_key(closest, w)
				distance = weights[weight_key] + distances[closest]
				if distance < distances[w]:
					distances[w] = distance
		unvisited.remove(closest)

	return distances
