import unittest
from count_inversions import count_inversions

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

if __name__ == "__main__":
	unittest.main()