import unittest
from quicksort import quick_sort

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

if __name__ == "__main__":
	unittest.main()