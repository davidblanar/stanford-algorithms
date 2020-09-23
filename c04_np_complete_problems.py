# Shortest Paths Revisited, NP-Complete Problems and What To Do About Them
# https://www.coursera.org/learn/algorithms-npcomplete

import sys
import heapq
from utils import euclidean_distance

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

# week 2
def travelling_salesman(coords):
	"""
	Computes the shortest path for the Traveling Salesman Problem
		Parameters:
			coords (tuple[]): A list of cities to visit, each city being represented by a tuple (x, y)
							  with x and y being the coordinates
		Returns:
			(int): the shortest distance in which all the cities can be visited
	"""
	# TODO currently this is slow, need to optimize
	def ts(root, current, s):
		if len(s) == 0:
			return euclidean_distance(current, root)
		if len(s) == 1:
			k = s[0]
			return ts(root, k, []) + euclidean_distance(current, k)
		
		minimum = sys.maxsize
		for item in s:
			c = s[:]
			c.remove(item)
			minimum = min(minimum, ts(root, item, c) + euclidean_distance(current, item))
		return minimum

	root = coords[0]
	return ts(root, root, coords[1:])

# week 3
def travelling_salesman_approx(coords):
	"""
	Computes an approximate solution to the Traveling Salesman Problem
		Parameters:
			coords (tuple[]): A list of cities to visit, each city being represented by a tuple (idx, x, y)
							  with x and y being the coordinates
		Returns:
			(float): the approximated shortest distance in which all the cities can be visited
	"""
	def get_closest(heap, visited):
		while True:
			closest = heapq.heappop(heap)
			_, _, city = closest
			if city not in visited:
				break
		return closest

	distances = {}
	for city in coords:
		_, x, y = city
		heap = []
		for c in coords:
			if c != city:
				idx, z, w = c
				distance = euclidean_distance((x, y), (z, w))
				heapq.heappush(heap, (distance, idx, c))
		distances[city] = heap

	minimum = sys.maxsize

	for i, _ in enumerate(coords):
		city = coords[i]
		visited = set()
		first = city
		total = 0

		visited.add(city)
		while len(visited) != len(coords):
			heap = distances[city].copy()
			distance, _, city = get_closest(heap, visited)
			visited.add(city)
			total += distance
			if len(visited) == len(coords):
				last = city

		_, x, y = first
		_, z, w = last
		total += euclidean_distance((x, y), (z, w))
		minimum = min(minimum, total)
	
	return minimum
