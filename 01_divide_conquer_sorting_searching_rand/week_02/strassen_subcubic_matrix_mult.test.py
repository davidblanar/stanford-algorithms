import unittest
from strassen_subcubic_matrix_mult import strassen_mult

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

if __name__ == "__main__":
	unittest.main()