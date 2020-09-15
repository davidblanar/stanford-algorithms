# Graph Search, Shortest Paths, and Data Structures
# https://www.coursera.org/learn/algorithms-graphs-data-structures

import sys
from heap import Heap

# week 1
def kosaraju(graph):
	"""
	Computes strongly connected components of a given graph using Kosaraju's algorithm
		Parameters:
			graph (DirectedGraph): A directed graph
		Returns:
			(dict): A dictionary containing all the SCCs of the graph
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
			(dict): A dictionary of path lengths from source vertex to every other vertex
	"""
	# note: this is currently O(m * n) because of the naive implementation
	# this could be brought down to O(m * log(n)) using a heap
	vertices = graph.get_vertices()
	assert source_vertex in vertices

	# find the unvisited vertex with lowest distance score
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

	# by default all vertices are unvisited and all distances are maximal
	for v in vertices:
		unvisited.add(v)
		distances[v] = max_value
	# distance of the source vertex to itself is 0
	distances[source_vertex] = 0

	while len(unvisited) > 0:
		# find the closest unvisited vertex
		# this will automatically select the source vertex on the first iteration
		closest = find_closest(unvisited, distances)
		edges = vertices[closest]
		for w in edges:
			if w in unvisited:
				# if the edge is unvisited, retrieve its distance
				weight_key = graph.get_weight_key(closest, w)
				distance = weights[weight_key] + distances[closest]
				# if the distance is smaller that the currently recorded distance for that vertex, update it with the lower value
				if distance < distances[w]:
					distances[w] = distance
		# remove the processed vertex from the set of unvisited vertices
		unvisited.remove(closest)

	return distances

# week 3
def median_maintenance(nums):
	"""
	Computes the medians of a list of numbers
		Parameters:
			nums (int[]): A list of numbers
		Returns:
			(int[]): The medians for the provided list
	"""

	# low is a max-heap because it uses a comparator which multiplies the number by -1
	low = Heap(lambda x: -x)
	# high is a min-heap (uses default comparator)
	high = Heap()
	# array of results to be returned
	medians = []

	def push(num):
		if low.size() == 0 or num < low.peek():
			low.insert(num)
		else:
			high.insert(num)

	def balance_heaps():
		# determine which of the heaps is larger
		larger_heap = low if low.size() > high.size() else high
		smaller_heap = high if low.size() > high.size() else low
		if larger_heap.size() - smaller_heap.size() >= 2:
			# if the difference is larger than 1 extract an item from the larger heap
			# and store it in the smaller heap
			smaller_heap.insert(larger_heap.extract())

	def calc_median(num):
		# determine which of the heaps is larger
		larger_heap = low if low.size() > high.size() else high
		smaller_heap = high if low.size() > high.size() else low
		# if both heaps are the same size an even amount of numbers was supplied
		# calculate the average of the two "middle" numbers
		if smaller_heap.size() == larger_heap.size():
			return (smaller_heap.peek() + larger_heap.peek()) / 2
		# otherwise return the root of the larger of the heaps
		else:
			return larger_heap.peek()

	for num in nums:
		push(num)
		balance_heaps()
		median = calc_median(num)
		medians.append(median)

	return medians

# week 4
# note: not going to test this with the provided testing file
# as it contains 1 000 000 integers, which would take forever
def two_sum(nums, start, end):
	"""
	Computes the count of distinct numbers x, y in a list of values T that statisfy the condition
	that x + y = t where t is a number in the list T, over the interval [start, end]
		Parameters:
			nums (int[]): A list of numbers
			start (int): The start of the interval
			end (int): The end of the interval
		Returns:
			(int): The count of distinct numbers x, y that satisfy the condition above
	"""
	count = 0
	table = {}
	
	for num in nums:
		if num not in table:
			table[num] = True

	def _two_sum(y):
		result = []
		for num in nums:
			key = y - num
			if key in table and num != key - num:
				result.append((key, num))
		return result

	for i in range(start, end + 1):
		result = _two_sum(i)
		if len(result) > 0:
			count += 1
	
	return count
