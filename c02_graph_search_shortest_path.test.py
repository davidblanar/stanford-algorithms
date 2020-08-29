import unittest
import sys
import os
from graph import DirectedGraph
from c02_graph_search_shortest_path import kosaraju
import threading

sys.setrecursionlimit(800000)
threading.stack_size(67108864)

class TestSCC(unittest.TestCase):
	def test_scc(self):
		g = DirectedGraph()
		g.add_edge("1", "4")
		g.add_edge("4", "7")
		g.add_edge("7", "1")

		g.add_edge("6", "9")
		g.add_edge("9", "3")
		g.add_edge("3", "6")

		g.add_edge("8", "5")
		g.add_edge("5", "2")
		g.add_edge("2", "8")

		g.add_edge("9", "7")
		g.add_edge("8", "6")

		expected = {
			"7": ["7", "1", "4"],
			"9": ["9", "3", "6"],
			"8": ["8", "5", "2"]
		}
		self.assertEqual(kosaraju(g), expected)

	def test_scc_large(self):
		filepath = os.path.abspath("./scc.txt")
		f = open(filepath, "r")
		g = DirectedGraph()
		for line in f.readlines():
			arr = line.split(" ")[:-1]
			v1 = arr[0]
			v2 = arr[1]
			g.add_edge(v1, v2)
		f.close()

		sccs = kosaraju(g)
		# only check the length of 5 largest SCCs
		edge_lengths = []
		for _, value in sccs.items():
			edge_lengths.append(len(value))
		sorted_lengths = sorted(edge_lengths, reverse=True)
		self.assertEqual(sorted_lengths[:5], [434821, 968, 459, 313, 211])

if __name__ == "__main__":
	# ugly hack to work around the max call stack size for scc.txt
	thread = threading.Thread(target=unittest.main)
	thread.start()