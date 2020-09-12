import unittest
import os
from c03_greedy_algorithms_dynamic_prog import schedule_jobs, job_score_diff, job_score_ratio, primm_mst
from graph import WeightedUndirectedGraph

class TestJobScheduling(unittest.TestCase):
	def test_job_scheduling(self):
		jobs = [
			(8, 50),
			(74, 59),
			(31, 73),
			(45, 79),
			(24, 10),
			(41, 66),
			(93, 43),
			(88, 4),
			(28, 30),
			(41, 13),
			(4, 70),
			(10, 58)
		]
		self.assertEqual(schedule_jobs(jobs, job_score_diff), 68615)
		self.assertEqual(schedule_jobs(jobs, job_score_ratio), 67247)

	def test_job_scheduling_large(self):
		filepath = os.path.abspath("./files/jobs.txt")
		f = open(filepath, "r")
		# skip first line
		next(f)
		jobs = []
		for line in f.readlines():
			line = line.rstrip('\n')
			a = line.split(" ")
			job = (int(a[0]), int(a[1]))
			jobs.append(job)
		f.close()

		self.assertEqual(schedule_jobs(jobs, job_score_diff), 69119377652)
		self.assertEqual(schedule_jobs(jobs, job_score_ratio), 67311454237)

class TestPrimm(unittest.TestCase):
	def test_primm(self):
		g = WeightedUndirectedGraph()
		g.add_edge("A", "B", 1)
		g.add_edge("B", "C", 2)
		g.add_edge("C", "D", 5)
		g.add_edge("D", "A", 4)
		g.add_edge("A", "C", 3)
		self.assertEqual(primm_mst(g), 7)

	def test_primm_large(self):
		filepath = os.path.abspath("./files/edges.txt")
		f = open(filepath, "r")
		# skip first line
		next(f)
		g = WeightedUndirectedGraph()
		for line in f.readlines():
			line = line.rstrip('\n')
			a = line.split(" ")
			g.add_edge(a[0], a[1], int(a[2]))
		f.close()
		self.assertEqual(primm_mst(g), -3612829)

if __name__ == "__main__":
	unittest.main()