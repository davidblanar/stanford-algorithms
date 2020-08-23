import unittest
import sys
import os
from min_cut import min_cut_len, Graph

class TestMinCut(unittest.TestCase):
	def test_min_cut(self):
		g = Graph()
		g.add_edge("A", "B")
		g.add_edge("B", "C")
		g.add_edge("C", "D")
		g.add_edge("D", "A")
		g.add_edge("D", "B")
		self.assertEqual(min_cut_len(g), 2)

	def test_min_cut_large(self):
		filepath = os.path.abspath("./min_cut_data.txt")
		f = open(filepath, "r")
		g = Graph()
		for line in f.readlines():
			arr = line.split("\t")[:-1]
			vertex = arr[0]
			edges = arr[1:]
			for item in edges:
				if not g.has_edge(vertex, item):
					g.add_edge(vertex, item)
		f.close()
		self.assertEqual(min_cut_len(g), 17)

if __name__ == "__main__":
	unittest.main()