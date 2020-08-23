import unittest
import sys
from min_cut import min_cut_len, Graph

class TestMinCut(unittest.TestCase):
	def test_min_cut1(self):
		g = Graph()
		g.add_edge("A", "B")
		g.add_edge("B", "C")
		g.add_edge("C", "D")
		g.add_edge("D", "A")
		g.add_edge("D", "B")
		self.assertEqual(min_cut_len(g), 2)

if __name__ == "__main__":
	unittest.main()