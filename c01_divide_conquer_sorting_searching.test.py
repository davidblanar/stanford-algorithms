import unittest
import os
from c01_divide_conquer_sorting_searching import count_inversions, strassen_mult, quick_sort, min_cut_len, randomized_selection
from graph import UndirectedGraph

class TestCountInversion(unittest.TestCase):
	def test_count_inversions(self):
		a = [1,3,5,2,4,6]
		b = [8,4,2,1]
		c = [3,1,2]
		d = [2,4,1,3,5]
		e = [1,2,3,4,5]
		self.assertEqual(count_inversions(a), 3)
		self.assertEqual(count_inversions(b), 6)
		self.assertEqual(count_inversions(c), 2)
		self.assertEqual(count_inversions(d), 3)
		self.assertEqual(count_inversions(e), 0)

class TestStrassen(unittest.TestCase):
	def test_strassen_mult(self):
		A = [
			[-1,4],
			[2,3]
		]
		B = [
			[9,-3],
			[6,1]
		]
		AB = [
			[15, 7],
			[36, -3]
		]
		self.assertEqual(strassen_mult(A, B), AB)

		C = [
			[3, 4],
			[2, 1]
		]
		D = [
			[1, 5],
			[3, 7]
		]
		CD = [
			[15, 43],
			[5, 17]
		]
		self.assertEqual(strassen_mult(C, D), CD)

		E = [
			[5, 7, 9, 10],
			[2, 3, 3, 8],
			[8, 10, 2, 3],
			[3, 3, 4, 8]
		]
		F = [
			[3, 10, 12, 18],
			[12, 1, 4, 9],
			[9, 10, 12, 2],
			[3, 12, 4, 10]
		]
		EF = [
			[210, 267, 236, 271],
			[93, 149, 104, 149],
			[171, 146, 172, 268],
			[105, 169, 128, 169]
		]
		self.assertEqual(strassen_mult(E, F), EF)

class TestQuickSort(unittest.TestCase):
	def test_quick_sort(self):
		a = []
		b = [8,4,2,1]
		c = [3,1,2]
		d = [1]
		e = [1,2,3,4,5]
		self.assertEqual(quick_sort(a), [])
		self.assertEqual(quick_sort(b), [1,2,4,8])
		self.assertEqual(quick_sort(c), [1,2,3])
		self.assertEqual(quick_sort(d), [1])
		self.assertEqual(quick_sort(e), [1,2,3,4,5])

class TestMinCut(unittest.TestCase):
	def test_min_cut(self):
		g = UndirectedGraph()
		g.add_edge("A", "B")
		g.add_edge("B", "C")
		g.add_edge("C", "D")
		g.add_edge("D", "A")
		g.add_edge("D", "B")
		self.assertEqual(min_cut_len(g), 2)

	def test_min_cut_large(self):
		filepath = os.path.abspath("./files/min_cut_data.txt")
		f = open(filepath, "r")
		g = UndirectedGraph()
		for line in f.readlines():
			arr = line.split("\t")[:-1]
			vertex = arr[0]
			edges = arr[1:]
			for item in edges:
				if not g.has_edge(vertex, item):
					g.add_edge(vertex, item)
		f.close()
		self.assertEqual(min_cut_len(g), 17)

class TestRandomizedSelection(unittest.TestCase):
	def test_randomized_selection(self):
		a = []
		b = [5,15,8,3,7,1,9,10,6,7,12,14,2,16,19]
		c = [3,2,1,5,6,4]
		d = [2]
		self.assertEqual(randomized_selection(a, 1), None)
		self.assertEqual(randomized_selection(b, 1), 1)
		self.assertEqual(randomized_selection(b, 4), 5)
		self.assertEqual(randomized_selection(c, 6), 6)
		self.assertEqual(randomized_selection(c, 1), 1)
		self.assertEqual(randomized_selection(c, 3), 3)
		self.assertEqual(randomized_selection(d, 1), 2)

if __name__ == "__main__":
	unittest.main()