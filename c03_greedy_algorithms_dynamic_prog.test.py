import unittest
import os
from c03_greedy_algorithms_dynamic_prog import schedule_jobs, job_score_diff, job_score_ratio, prim_mst, k_clustering, huffman_encoding, max_wis
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

class TestPrim(unittest.TestCase):
	def test_prim(self):
		g = WeightedUndirectedGraph()
		g.add_edge("A", "B", 1)
		g.add_edge("B", "C", 2)
		g.add_edge("C", "D", 5)
		g.add_edge("D", "A", 4)
		g.add_edge("A", "C", 3)
		self.assertEqual(prim_mst(g), 7)

	def test_prim_large(self):
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
		self.assertEqual(prim_mst(g), -3612829)

class TestClustering(unittest.TestCase):
	def test_clustering_small(self):
		g = WeightedUndirectedGraph()
		g.add_edge("A", "B", 7)
		g.add_edge("B", "C", 6)
		g.add_edge("B", "E", 5)
		g.add_edge("C", "E", 3)
		g.add_edge("C", "D", 2)
		g.add_edge("D", "E", 4)
		g.add_edge("E", "A", 1)
		self.assertEqual(k_clustering(g, 5), 1)
		self.assertEqual(k_clustering(g, 4), 2)
		self.assertEqual(k_clustering(g, 3), 3)
		self.assertEqual(k_clustering(g, 2), 5)

	def test_clustering_medium(self):
		data = [
			(1, 2, 1),
			(1, 3, 2),
			(1, 4, 4),
			(1, 5, 5),
			(2, 3, 4),
			(2, 4, 3),
			(2, 5, 6),
			(3, 4, 1),
			(3, 5, 7),
			(4, 5, 8)
		]
		g = WeightedUndirectedGraph()
		for item in data:
			n1, n2, d = item
			g.add_edge(str(n1), str(n2), d)

		self.assertEqual(k_clustering(g, 2), 5)
		self.assertEqual(k_clustering(g, 3), 2)
		self.assertEqual(k_clustering(g, 4), 1)

	def test_clustering_large(self):
		filepath = os.path.abspath("./files/clustering1.txt")
		f = open(filepath, "r")
		# skip first line
		next(f)
		g = WeightedUndirectedGraph()
		for line in f.readlines():
			line = line.rstrip('\n')
			a = line.split(" ")
			g.add_edge(a[0], a[1], int(a[2]))
		f.close()
		# TODO this returns an incorrect result, yet the smallest test cases pass - find out why
		self.assertEqual(k_clustering(g, 4), 106)

class TestHuffman(unittest.TestCase):
	def test_huffman_small(self):
		frequencies = [60, 25, 10, 5]
		minimum, maximum = huffman_encoding(frequencies)
		self.assertEqual(minimum, 1)
		self.assertEqual(maximum, 3)

	def test_huffman_medium(self):
		frequencies = [
			895,
			121,
			188,
			953,
			378,
			849,
			153,
			579,
			144,
			727,
			589,
			301,
			442,
			327,
			930
		]
		minimum, maximum = huffman_encoding(frequencies)
		self.assertEqual(minimum, 3)
		self.assertEqual(maximum, 6)

	def test_huffman_large(self):
		filepath = os.path.abspath("./files/huffman.txt")
		f = open(filepath, "r")
		# skip first line
		next(f)
		frequencies = []
		for line in f.readlines():
			line = line.rstrip('\n')
			frequencies.append(int(line))
		f.close()
		minimum, maximum = huffman_encoding(frequencies)
		self.assertEqual(minimum, 9)
		self.assertEqual(maximum, 19)

def WIS(weights):
	"""Given the weights, return the A: optimal value, S: optimal path.
	"""
	A = [0]*(len(weights))
	A[0] = 0
	A[1] = weights[1]
	
	# Find the optimal value
	for i in range(2, len(weights)):
		A[i] = max(A[i-1], A[i-2]+weights[i])
	
	return A
	# Trace back to find the optimal solution.
	S= []
	i = len(weights)-1 
	while i >= 1:
		if A[i-1] >= A[i-2]+weights[i]:
			i = i-1
		else:
			S.append(i)
			i = i-2
	
	return A, S

class TestMaxWis(unittest.TestCase):
	def test_max_wis_1(self):
		vertices = [1,4,5,4]
		mwis = max_wis(vertices)
		result = ""
		for idx in vertices:
			if idx in mwis:
				result += "1"
			else:
				result += "0"
		self.assertEqual(result, "0101")

	def test_max_wis_2(self):
		vertices = [
			280,
			618,
			762,
			908,
			409,
			34,
			59,
			277,
			246,
			779
		]
		mwis = max_wis(vertices)
		check = [2, 4, 6, 8, 10]
		result = ""
		for idx in check:
			if idx in mwis:
				result += "1"
			else:
				result += "0"
		self.assertEqual(result, "11111")

	def test_max_wis_3(self):
		vertices = [
			460,
			250,
			730,
			63,
			379,
			638,
			122,
			435,
			705,
			84
		]
		mwis = max_wis(vertices)
		check = [1, 3, 6, 9]
		result = ""
		for idx in check:
			if idx in mwis:
				result += "1"
			else:
				result += "0"
		self.assertEqual(result, "1111")

	def test_max_wis_large(self):
		filepath = os.path.abspath("./files/mwis.txt")
		f = open(filepath, "r")
		# skip first line
		next(f)
		vertices = []
		for line in f.readlines():
			line = line.rstrip('\n')
			vertices.append(int(line))
		f.close()
		mwis = max_wis(vertices)
		check = [1, 2, 3, 4, 17, 117, 517, 997]
		result = ""
		for idx in check:
			if idx in mwis:
				result += "1"
			else:
				result += "0"

		self.assertEqual(result, "10100110")


if __name__ == "__main__":
	unittest.main()