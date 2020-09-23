import math

def swap(a, i1, i2):
	a[i1], a[i2] = a[i2], a[i1]

def euclidean_distance(p1, p2):
	x, y = p1
	z, w = p2
	return math.sqrt(((x - z) ** 2) + ((y - w) ** 2))