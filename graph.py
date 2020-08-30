from abc import ABC, abstractmethod
from random import randrange
from queue import Queue

class Graph(ABC):
	def __init__(self, vertices = None):
		self.vertices = {} if vertices is None else vertices

	def get_vertices(self):
		return self.vertices

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

	# removes looping edges, i.e. edges that connect a vertex to itself
	def remove_loops(self):
		for key, value in self.vertices.items():
			self.vertices[key] = [item for item in value if item != key]

	def has_edge(self, v1, v2):
		return v1 in self.vertices and v2 in self.vertices[v1]

	def copy_vertices(self):
		vertices = {}
		for key, value in self.vertices.items():
			vertices[key] = value[:]
		return vertices

	# perform breadth-first search
	def bfs(self, start_vertex):
		assert start_vertex in self.vertices
		visited = set()
		q = Queue()
		q.put(start_vertex)
		visited.add(start_vertex)
		while not q.empty():
			v = q.get()
			edges = self.vertices[v]
			for w in edges:
				if w not in visited:
					visited.add(w)
					q.put(w)

	# perform depth-first search
	def dfs(self, start_vertex, explored = None):
		assert start_vertex in self.vertices
		visited = set() if explored == None else explored
		visited.add(start_vertex)
		edges = self.vertices[start_vertex]
		for w in edges:
			if w not in visited:
				self.dfs(w, visited)
		
	@abstractmethod
	def add_edge(self, v1, v2):
		raise NotImplementedError

	@abstractmethod
	def deep_copy(self):
		raise NotImplementedError

class UndirectedGraph(Graph):
	# adds a bi-directional edge between two vertices
	def add_edge(self, v1, v2):
		if v1 not in self.vertices:
			self.vertices[v1] = []
		if v2 not in self.vertices:
			self.vertices[v2] = []

		self.vertices[v1].append(v2)
		self.vertices[v2].append(v1)
		
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

	def deep_copy(self):
		vertices = self.copy_vertices()
		return UndirectedGraph(vertices)

class DirectedGraph(Graph):
	# adds a uni-directional edge between two vertices
	def add_edge(self, v1, v2):
		if v1 not in self.vertices:
			self.vertices[v1] = []
		if v2 not in self.vertices:
			self.vertices[v2] = []

		self.vertices[v1].append(v2)

	# reverses the direction of all the edges
	def reverse(self):
		g = DirectedGraph()
		for v, e in self.vertices.items():
			for edge in e:
				g.add_edge(edge, v)
		return g

	def deep_copy(self):
		vertices = self.copy_vertices()
		return DirectedGraph(vertices)

class WeightedGraph(Graph):
	def __init__(self, vertices = None, weights = None):
		super().__init__(vertices)
		self.weights = weights if weights != None else {}

	def get_weights(self):
		return self.weights

	def get_weight_key(self, v1, v2):
		return "{}-{}".format(v1, v2)

	def get_weight(self, v1, v2):
		key = self.get_weight_key(v1, v2)
		return self.weights[key]

class WeightedUndirectedGraph(UndirectedGraph, WeightedGraph):
	def add_edge(self, v1, v2, weight):
		assert weight >= 0
		super().add_edge(v1, v2)
		key1 = self.get_weight_key(v1, v2)
		self.weights[key1] = weight
		key2 = self.get_weight_key(v1, v2)
		self.weights[key2] = weight

	def deep_copy(self):
		vertices = self.copy_vertices()
		return WeightedUndirectedGraph(vertices, self.weights)

class WeightedDirectedGraph(DirectedGraph, WeightedGraph):
	def add_edge(self, v1, v2, weight):
		assert weight >= 0
		super().add_edge(v1, v2)
		key = self.get_weight_key(v1, v2)
		self.weights[key] = weight

	def deep_copy(self):
		vertices = self.copy_vertices()
		return WeightedDirectedGraph(vertices, self.weights)

