import unittest
import sys
import os
from graph import DirectedGraph, WeightedDirectedGraph, WeightedUndirectedGraph
from c02_graph_search_shortest_path import kosaraju, dijkstra, median_maintenance, two_sum
import threading

# ugly hack to work around the max call stack size for scc.txt
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
		filepath = os.path.abspath("./files/scc.txt")
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

class TestDijkstra(unittest.TestCase):
	def test_dijkstra_directed(self):
		g = WeightedDirectedGraph()
		g.add_edge("S", "V", 1)
		g.add_edge("S", "W", 4)
		g.add_edge("V", "W", 2)
		g.add_edge("V", "T", 6)
		g.add_edge("W", "T", 3)

		expected = {"S": 0, "V": 1, "W": 3, "T": 6}
		self.assertEqual(dijkstra(g, "S"), expected)

	def test_dijkstra_undirected(self):
		g = WeightedUndirectedGraph()
		g.add_edge("A", "B", 6)
		g.add_edge("A", "D", 1)
		g.add_edge("D", "B", 2)
		g.add_edge("D", "E", 1)
		g.add_edge("B", "E", 2)
		g.add_edge("B", "C", 5)
		g.add_edge("E", "C", 5)

		expected = {"A": 0, "B": 3, "D": 1, "E": 2, "C": 7}
		self.assertEqual(dijkstra(g, "A"), expected)

	def test_dijkstra_undirected_large(self):
		filepath = os.path.abspath("./files/dijkstra.txt")
		f = open(filepath, "r")
		g = WeightedUndirectedGraph()
		for line in f.readlines():
			arr = line.split("\t")[:-1]
			vertex = arr[0]
			rest = arr[1:]
			for item in rest:
				item_arr = item.split(",")
				other_vertex = item_arr[0]
				weight = int(item_arr[1])
				g.add_edge(vertex, other_vertex, weight)
		f.close()
		# only check specific vertices as per assignment
		vertices_to_check = ["7","37","59","82","99","115","133","165","188","197"]
		path_lengths = dijkstra(g, "1", 1000000)
		expected = [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]
		result = []
		for v in vertices_to_check:
			result.append(path_lengths[v])

		self.assertEqual(result, expected)		

class TestMedian(unittest.TestCase):
	def test_median(self):
		nums = [
			6331,
			2793,
			1640,
			9290,
			225,
			625,
			6195,
			2303,
			5685,
			1354
		]
		medians = median_maintenance(nums)
		result = sum(medians) % 10000
		self.assertEqual(result, 3939.5)

	def test_median_large(self):
		filepath = os.path.abspath("./files/median.txt")
		f = open(filepath, "r")
		nums = []
		for line in f.readlines():
			nums.append(int(line))
		f.close()
		medians = median_maintenance(nums)
		result = sum(medians) % 10000
		self.assertEqual(result, 3171)

class TestTwoSum(unittest.TestCase):
	def test_two_sum(self):
		nums = [
			-3,
			-1,
			1,
			2,
			9,
			11,
			7,
			6,
			2
		]
		self.assertEqual(two_sum(nums, 3, 10), 8)

if __name__ == "__main__":
	thread = threading.Thread(target=unittest.main)
	thread.start()