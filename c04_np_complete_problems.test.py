import unittest
import os
from c04_np_complete_problems import all_pairs, travelling_salesman, travelling_salesman_approx, two_sat

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

	def test_tsp_approx(self):
		coords = [
			(1, 2, 1),
			(2, 4, 0),
			(3, 2, 0),
			(4, 0, 0),
			(5, 4, 3),
			(6, 0, 3)
		]
		x = travelling_salesman_approx(coords)
		self.assertEqual(round(x, 2), 15.24)

		coords = [
			(1, 3.9141143042353885, 2.762714352214207),
			(2, 4.9859239915123705, 0.8125842127816254),
			(3, 6.461157697851659, 4.944000729919298),
			(4, 4.436155941747397, 6.388356442724854),
			(5, 2.2110506892607775, 7.847428438430043),
			(6, 2.434048999209285, 1.940598412080333),
			(7, 5.5331650074496, 6.253753477703925),
			(8, 0.5579846947970601, 0.8788688913220861)
		]
		x = travelling_salesman_approx(coords)
		self.assertEqual(round(x, 2), 22.99)

		coords = [
			(1, 11.992868554597958, 16.582374182268197),
			(2, 11.914781120232131, 1.4825369577899306),
			(3, 6.590197044653509, 16.857466002566785),
			(4, 15.353390560853668, 1.725235385430255),
			(5, 2.455456697407583, 16.912762303314093),
			(6, 3.6111538897995477, 11.106921166403339),
			(7, 9.191437785262899, 4.608800403608775),
			(8, 19.180411187961333, 17.5618961806263),
			(9, 10.676614606257768, 3.2097678100169325),
			(10, 7.008542289662676, 11.023745793399815),
			(11, 9.560411313284266, 10.061748723290663),
			(12, 1.1290360108800734, 17.728961447123805),
			(13, 4.37481537914792, 9.176213181628476),
			(14, 16.364931836205184, 8.751130555382037),
			(15, 4.509468952052802, 15.726190987167598),
			(16, 19.51157210554256, 12.219774753209673),
			(17, 12.071753510242845, 9.361201740664972),
			(18, 16.8663562816133, 16.802590991019542),
			(19, 4.315783605533254, 1.262228738728861),
			(20, 13.561272956513545, 5.4228276997635465)
		]
		# note: not going to test the provided test file as it takes forever
		x = travelling_salesman_approx(coords)
		self.assertEqual(round(x, 2), 87.70)

class TestTwoSat(unittest.TestCase):
	def test_two_sat(self):
		a = [
			(-1, -2),
			(2, 2)
		]
		self.assertEqual(two_sat(a), True)
		b = [
			(1, 2),
			(2, 2)
		]
		self.assertEqual(two_sat(b), True)
		c = [
			(2, 2),
			(-2, -2)
		]
		self.assertEqual(two_sat(c), False)
		d = [
			(8, -8),
			(-3, 4),
			(2, -8),
			(3, 3),
			(2, 6),
			(-2, -6),
			(1, 6),
			(4, 8)
		]
		self.assertEqual(two_sat(d), True)
		e = [
			(-3, -10),
			(-9, -20),
			(-5, 4),
			(-9, -9),
			(-12, 2),
			(-13, -17),
			(19, 2),
			(-6, -5),
			(-10, 16),
			(5, 19),
			(12, -10),
			(-12, 8),
			(12, 12),
			(-16, -16),
			(3, -19),
			(10, -8),
			(-18, -19),
			(17, -5),
			(3, 20),
			(-15, -10)
		]
		self.assertEqual(two_sat(e), False)

	def test_two_sat_large(self):
		path_template = "./files/2sat{}.txt"
		paths = []
		for i in range(1, 7):
			paths.append(path_template.format(i))

		tests = []
		for path in paths:
			data = self.read_file_into_arr(path)
			tests.append(data)

		result = ""
		for test in tests:
			res = two_sat(test)
			if res is True:
				result += "1"
			else:
				result += "0"

		self.assertEqual(result, "101100")


	def read_file_into_arr(self, file_path):
		filepath = os.path.abspath(file_path)
		f = open(filepath, "r")
		# skip first line
		next(f)
		data = []
		for line in f.readlines():
			line = line.rstrip('\n')
			a = line.split(" ")
			data.append((int(a[0]), int(a[1])))
		f.close()
		return data

if __name__ == "__main__":
	unittest.main()
