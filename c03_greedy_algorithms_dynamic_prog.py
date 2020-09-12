# Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
# https://www.coursera.org/learn/algorithms-greedy

import sys
import heapq

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
			completion_time (int): The completion item of all the jobs combined
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

def primm_mst(graph):
	"""
	Computes the cost of the MST of a weighted undirected graph
		Parameters:
			graph (WeightedUndirectedGraph): A weighted undirected graph
		Returns:
			cost (int): The cost of the MST
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
