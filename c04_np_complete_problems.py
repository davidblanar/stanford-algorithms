# Shortest Paths Revisited, NP-Complete Problems and What To Do About Them
# https://www.coursera.org/learn/algorithms-npcomplete

import sys

# week 1
def all_pairs(graph):
	"""
	Computes the shortest distance between all pairs of vertices in a graph using the Floyd-Warshall algorithm
		Parameters:
			graph (dict): A dictionary representing a graph
		Returns:
			(int | None): the shortest distance among all points or None if the graph has negative cycles
	"""
	def has_cycle(a):
		size = len(a)
		r = range(0, size)
		for i in r:
			for j in r:
				if a[i][i][j] < 0:
					return True
		return False

	arr = []
	size = len(graph)
	r = range(0, size)
	for i in r:
		arr.append([])
		for j in r:
			arr[i].append([])
			for k in r:
				if k == 0:
					if i == j:
						arr[i][j].append(0)
					elif (i, j) in graph:
						arr[i][j].append(graph[i, j])
					else:
						arr[i][j].append(sys.maxsize)
				else:
					arr[i][j].append(sys.maxsize)

	r = range(1, size)
	for k in r:
		for i in r:
			for j in r:
				arr[i][j][k] = min(arr[i][j][k - 1], arr[i][k][k - 1] + arr[k][j][k - 1])

	if has_cycle(arr):
		return None

	minimum = sys.maxsize
	for k in r:
		for i in r:
			for j in r:
				minimum = min(minimum, arr[i][j][k])
	return minimum
