from random import randrange
import operator as op
from functools import reduce
from math import log, ceil
import sys

class Graph:
	def __init__(self):
		self.vertices = {}

	def get_vertices(self):
		return self.vertices

	# adds an edge between two vertices
	def add_edge(self, v1, v2):
		if v1 not in self.vertices:
			self.vertices[v1] = []
		if v2 not in self.vertices:
			self.vertices[v2] = []

		self.vertices[v1].append(v2)
		self.vertices[v2].append(v1)

	# returns two vertices that are connected by an edge
	def get_random_edge(self):
		vertices = list(self.vertices.keys())
		idx = randrange(len(vertices))
		# choose a random vertex
		vertex = vertices[idx]
		edges = self.vertices[vertex]
		idx = randrange(len(edges))
		# choose another random vertex that is connected to the first one
		other_vertex = edges[idx]
		return vertex, other_vertex
		
	# contract and edge and merge the two vertices together
	def contract_edge(self, v1, v2):
		vertex1 = self.vertices[v1]
		vertex2 = self.vertices[v2]
		for item in vertex2:
			vertex1.append(item)
		del self.vertices[v2]
		for key, value in self.vertices.items():
			new_edges = []
			for item in value:
				if item == v2:
					new_edges.append(v1)
				else:
					new_edges.append(item)
			self.vertices[key] = new_edges
		self.remove_loops()

	# removes looping edges, i.e. edges that connect a vertex to itself
	def remove_loops(self):
		for key, value in self.vertices.items():
			self.vertices[key] = [item for item in value if item != key]


def min_cut(graph):
	"""
	Calculates the minimal cut of a graph using Karger's randomized contraction algorithm
		Parameters:
			graph (Graph): A graph to be examined

		Returns:
			vertices (dict): A dictionary containing the remaining vertices which represent the minimal cut
	"""
	while len(graph.get_vertices()) > 2:
		v1, v2 = graph.get_random_edge()
		graph.contract_edge(v1, v2)
	return graph.get_vertices()

def min_cut_len(graph):
	"""
	Calculates the amount of the edges intersecting the minimal cut of a graph
		Parameters:
			graph (Graph): A graph to be examined

		Returns:
			minimum (int): The amount of edges intersecting the minimal cut of a graph
	"""

	# calculate n choose r
	# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
	def ncr(n, r):
		r = min(r, n - r)
		numer = reduce(op.mul, range(n, n - r, -1), 1)
		denom = reduce(op.mul, range(1, r + 1), 1)
		return numer // denom

	n = len(graph.get_vertices())
	# calculate the amount of attempts that should be executed to increase the probability of a correct result roughly to 1/n
	# where n is the amount of vertices
	# https://en.wikipedia.org/wiki/Karger%27s_algorithm#Success_probability_of_the_contraction_algorithm
	attempts = ceil(ncr(n, 2) * log(n))
	minimum = sys.maxsize
	for _ in range(attempts):
		result = min_cut(graph)
		minimum = min(minimum, len(result))
	return minimum
