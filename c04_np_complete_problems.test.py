import unittest
import math
from c04_np_complete_problems import all_pairs, travelling_salesman

class TestAllPairs(unittest.TestCase):
	def test_all_pairs(self):
		g1 = {
			(1, 2): 1,
			(1, 3): 4,
			(2, 4): 2,
			(3, 4): 3,
			(4, 1): -4
		}
		g2 = {
			(1, 2): 1,
			(1, 3): 4,
			(2, 4): 2,
			(3, 4): 3,
			(4, 1): -2
		}
		# note: not going to test the provided files as it takes forever
		self.assertEqual(all_pairs(g1), None)
		self.assertEqual(all_pairs(g2), -2)

class TestSalesman(unittest.TestCase):
	def test_tsp(self):
		coords = [
			(0, 0),
			(1, 1)
		]
		x = travelling_salesman(coords)
		self.assertEqual(round(x, 2), 2.83)

		coords = [
			(0, 0),
			(0, 3),
			(3, 3)
		]
		x = travelling_salesman(coords)
		self.assertEqual(round(x, 2), 10.24)

		coords = [
			(0, 2.05),
			(3.414213562373095, 3.4642135623730947),
			(0.5857864376269049, 0.6357864376269047),
			(0.5857864376269049, 3.4642135623730947),
			(2, 0),
			(4.05, 2.05),
			(2, 4.10),
			(3.414213562373095, 0.6357864376269047)
		]
		x = travelling_salesman(coords)
		self.assertEqual(round(x, 2), 12.36)

		coords = [
			(0, 0),
			(4, 3),
			(4, 0),
			(0, 3)
		]
		x = travelling_salesman(coords)
		self.assertEqual(round(x, 2), 14.0)
		
if __name__ == "__main__":
	unittest.main()
