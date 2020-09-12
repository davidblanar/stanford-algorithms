# Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
# https://www.coursera.org/learn/algorithms-greedy

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
