import unittest
from randomized_selection import randomized_selection

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