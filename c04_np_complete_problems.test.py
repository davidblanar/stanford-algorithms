import unittest
from c04_np_complete_problems import all_pairs

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
		
if __name__ == "__main__":
	unittest.main()
	