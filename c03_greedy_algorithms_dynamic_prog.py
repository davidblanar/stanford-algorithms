# Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
# https://www.coursera.org/learn/algorithms-greedy

import heapq
from union import UnionFind

# week 1
def job_score_diff(job):
	w, l = job
	return (w - l) * -1 # multiply by -1 to achieve decreasing order

def job_score_ratio(job):
	w, l = job
	return (w / l) * -1 # same here

def schedule_jobs(jobs, calc_score):
	"""
	Computes the optimal schedule of a list of jobs
		Parameters:
			jobs (tuple[]): A list of jobs, each job is represented by a tuple
							in the form of (job_weight, job_length)
		Returns:
			(int): The completion item of all the jobs combined
	"""
	completion_time = 0
	queue = []
	for job in jobs:
		w, l = job
		score = calc_score(job)
		# multiply weight by -1 to once again achieve decreasing order (more important jobs first)
		heapq.heappush(queue, (score, w * -1, l))

	time = 0
	while len(queue) > 0:
		job = heapq.heappop(queue)
		score, w, l = job
		time += l
		# multiply by -1 to reverse the manipulation done when populating the queue
		completion_time += w * -1 * time

	return completion_time

def prim_mst(graph):
	"""
	Computes the cost of the MST of a weighted undirected graph
		Parameters:
			graph (WeightedUndirectedGraph): A weighted undirected graph
		Returns:
			(int): The cost of the MST
	"""
	vertices = graph.get_vertices()
	assert len(vertices) > 0

	def get_valid_vertex(spanned_vertices, queue):
		while len(queue) > 0:
			weight, vertex = heapq.heappop(queue)
			if vertex not in spanned_vertices:
				return weight, vertex
		return None

	keys = list(vertices.keys())
	queues = graph.get_weights_heap()
	v = keys[0]
	spanned = set()
	available_edges = []
	cost = 0

	while len(spanned) < len(keys):
		spanned.add(v)
		edges = queues[v]
		available_edges += edges
		heapq.heapify(available_edges)
		next_vertex = get_valid_vertex(spanned, available_edges)
		if next_vertex is None:
			break
		weight, w = next_vertex
		cost += weight
		v = w

	return cost

# week 2
def k_clustering(graph, k):
	"""
	Computes the smallest distance between k clusters of an undirected weighted graph
		Parameters:
			graph (WeightedUndirectedGraph): A weighted undirected graph
		Returns:
			(int): The smallest distance
	"""
	vertices = graph.get_vertices()
	assert len(vertices) > 0
	
	def get_keys_from_vertices(g, v, w):
		key_1 = g.get_weight_key(v, w)
		key_2 = g.get_weight_key(w, v)
		return key_1, key_2

	def get_vertices_from_key(key):
		keys = key.split("-")
		return keys[0], keys[1]

	seen = set()
	weights = graph.get_weights()
	unique_edges = []
	union = UnionFind()
	cluster_count = len(vertices)

	for v in vertices:
		union.insert(v, v)
		edges = vertices[v]
		for w in edges:
			key_1, key_2 = get_keys_from_vertices(graph, v, w)
			if key_1 not in seen and key_2 not in seen:
				seen.add(key_1)
				seen.add(key_2)
				unique_edges.append((weights[key_1], key_1))
	heapq.heapify(unique_edges)

	if cluster_count <= k:
		val, _ = heapq.heappop(unique_edges)
		return val

	while cluster_count != k:
		cluster_count -= 1
		_, key = heapq.heappop(unique_edges)
		key_1, key_2 = get_vertices_from_key(key)
		union.union(key_1, key_2)

	union_data = union.get_data()
	while len(unique_edges) > 0:
		val, key = heapq.heappop(unique_edges)
		key_1, key_2 = get_vertices_from_key(key)
		if union_data[key_1] != union_data[key_2]:
			return val

# week 3
def huffman_encoding(frequencies):
	"""
	Computes the minimum and maximum bit size of symbols based on their frequencies
		Parameters:
			frequencies (int[]): A list of frequencies
		Returns:
			(tuple): The minimum and maximum size
	"""
	def create_node(frequency):
		return {
			"frequency": frequency,
			"left": None,
			"right": None
		}

	def find_min(node):
		if node is None:
			return 0
		if node["left"] is None and node["right"] is None:
			# TODO maybe 1
			return 0
		if node["left"] is None:
			return 1 + find_min(node["right"])
		if node["right"] is None:
			return 1 + find_min(node["left"])
		return 1 + min(find_min(node["left"]), find_min(node["right"]))

	def find_max(node):
		if node is None:
			return 0
		left = find_max(node["left"])
		right = find_max(node["right"])
		return left + 1 if left > right else right + 1

	heap = []
	for frequency in frequencies:
		item = (frequency, create_node(frequency))
		heapq.heappush(heap, item)

	while len(heap) != 1:
		right_freq, right_node = heapq.heappop(heap)
		left_freq, left_node = heapq.heappop(heap)
		frequency = left_freq + right_freq
		node = create_node(frequency)
		node["left"] = left_node
		node["right"] = right_node
		heapq.heappush(heap, (frequency, node))

	_, tree = heap[0]
	return find_min(tree), find_max(tree) - 1

def max_wis(vertices):
	"""
	Determines the maximal weighted independent set of a list of weighted vertices
		Parameters:
			vertices (int[]): A list of vertex weights
		Returns:
			(set): The maximal weighted independent set of vertices
	"""
	s = set()
	weights = [0]
	for v in vertices:
		weights.append(v)

	size = len(weights)
	arr = [0] * size
	arr[1] = weights[1]
	for i in range(2, size):
		arr[i] = max(arr[i - 1], arr[i - 2] + weights[i])

	i = size - 1
	while i >= 1:
		if arr[i - 1] >= arr[i - 2] + weights[i]:
			i -= 1
		else:
			s.add(i)
			i -= 2
	return s

# week 4
def knapsack(max_weight, items):
	"""
	Computes the optimal solution for the knapsack problem
		Parameters:
			max_weight (int): The maximum weight capacity
			items: (tuple[]): A list of tuples, each containing the weight and the value of the item
		Returns:
			(int): The optimal solution
	"""
	arr = []
	size = len(items)
	for _ in range(0, size):
		arr.append([0] * (max_weight + 1))

	for i in range(0, len(arr)):
		weight, val = items[i]
		for w in range(0, max_weight + 1):
			if arr[i][w] != 0:
				continue
			if i == 0 and w == 0:
				continue
			if weight > w:
				arr[i][w] = arr[i - 1][w]
			else:
				arr[i][w] = max(arr[i - 1][w], arr[i - 1][w - weight] + val)

	return arr[-1][-1]

def knapsack_recursive(max_weight, items):
	"""
	A recursive memoized version of the knapsack() function for large inputs
	"""
	memo = {}
	def ks(n, c, mem):
		result = 0
		if n in mem and c in mem[n]:
			return mem[n][c]
		weight, val = items[n]
		if n == 0 or c == 0:
			result = 0
		elif weight > c:
			result = ks(n - 1, c, mem)
		else:
			x = ks(n - 1, c, mem)
			y = val + ks(n - 1, c - weight, mem)
			result = max(x, y)
		if n not in mem:
			mem[n] = {}
		mem[n][c] = result
		return result

	return ks(len(items) - 1, max_weight, memo)