# Divide and Conquer, Sorting and Searching, and Randomized Algorithms
# https://www.coursera.org/learn/algorithms-divide-conquer

from random import randrange, randint
import operator as op
from functools import reduce
from math import log, ceil, floor
import sys
from utils import swap

# week 2
def count_inversions(arr):
	"""
	Returns the number of inversions in an array
		Parameters:
			arr (int[]): An array of integers

		Returns:
			int: Count of inversions
	"""
	global count
	count = 0
	# implement using merge sort, which easily allows to count inversions during the merge phase
	def merge_sort(arr):
		# exit early if array is empty or there is only one element
		if len(arr) < 2:
			return arr

		mid = floor(len(arr) / 2)
		left = merge_sort(arr[0:mid])
		right = merge_sort(arr[mid:])
		return merge(left, right)

	# helper function to merge arrays and count split inversions
	def merge(a1, a2):
		global count
		res = []
		i = 0
		j = 0
		while True:
			# there are no more elements to look at - exit
			if len(a1) == i and len(a2) == j:
				break

			# array1 was fully merged but one element in array2 remains
			# push the remaining element into the result array
			# and advance to the next iteration of the loop
			if len(a1) == i and len(a2) != j:
				res.append(a2[j])
				j += 1
				continue
	 
			# array2 was fully merged but one element in array1 remains
			# push the remaining element into the result array
			# and advance to the next iteration of the loop
			if len(a1) != i and len(a2) == j:
				res.append(a1[i])
				i += 1
				continue

			# if the element in the second array is larger, this is a split inversion for all remaining elements of a1
			# add the remaining length of a1 to count
			if a1[i] > a2[j]:
				res.append(a2[j])
				j += 1
				count += len(a1) - i
			# if the element in the first array is larger or equal, there is no split inversion - simply advance
			else:
				res.append(a1[i])
				i += 1

		return res

	merge_sort(arr)
	return count

def strassen_mult(X, Y):
	"""
	Returns the multiplication of two matrices using Strassen's method
	Currently only works for even matrices due to partitioning, this can be circumvented using padding
		Parameters:
			X (int[][]): A 2D array of integers
			Y (int[][]): A 2D array of integers

		Returns:
			Z (int[][]): A 2D array of integers
	"""

	# helper function to split a matrix into 4 sub-matrices
	def split_matrix(M):
		if len(M) == 1 and len(M[0]) == 1:
			return M
		n = len(M)
		half_size = int(n / 2)
		A = empty_matrix(half_size, half_size)
		B = empty_matrix(half_size, half_size )
		C = empty_matrix(half_size, half_size)
		D = empty_matrix(half_size, half_size)

		for i in range(half_size):
			for j in range(half_size):
				A[i][j] = M[i][j]
				B[i][j] = M[i][j + half_size]
				C[i][j] = M[i + half_size][j]
				D[i][j] = M[i + half_size][j + half_size]
		return (A, B, C, D)

	# helper function to create an empty matrix of dimensions x by y
	def empty_matrix(x, y):
		M = [[]] * x
		for i in range(x):
			M[i] = [0] * y
		return M

	def add_matrices(A, B):
		n = len(A)
		M = empty_matrix(n, n)
		for i in range(n):
			for j in range(n):
				M[i][j] = A[i][j] + B[i][j]
		return M

	def subtract_matrices(A, B):
		n = len(A)
		M = empty_matrix(n, n)
		for i in range(n):
			for j in range(n):
				M[i][j] = A[i][j] - B[i][j]
		return M

	n = len(X)
	if n == 1:
		return [[X[0][0] * Y[0][0]]]
	else:
		A, B, C, D = split_matrix(X)
		E, F, G, H = split_matrix(Y)
		# p1 = A(F - H)
		P1 = strassen_mult(A, subtract_matrices(F, H))
		# p2 = (A + B)H
		P2 = strassen_mult(add_matrices(A, B), H)
		# p3 = (C + D)E
		P3 = strassen_mult(add_matrices(C, D), E)
		# p4 = D(G - E)
		P4 = strassen_mult(D, subtract_matrices(G, E))
		# p5 = (A + D)(E + H)
		P5 = strassen_mult(add_matrices(A, D), add_matrices(E, H))
		# p6 = (B - D)(G + H)
		P6 = strassen_mult(subtract_matrices(B, D), add_matrices(G, H))
		# p7 = (A - C)(E + F)
		P7 = strassen_mult(subtract_matrices(A, C), add_matrices(E, F))

		# top left quadrant of the final matrix = P5 + P4 - P2 + P6
		Q1 = add_matrices(add_matrices(P5, P4), subtract_matrices(P6, P2))
		# top right quadrant = P1 + P2
		Q2 = add_matrices(P1, P2)
		# bottom left quadrant = P3 + P4
		Q3 = add_matrices(P3, P4)
		# bottom right quadrant = P1 + P5 - P3 - P7
		Q4 = subtract_matrices(subtract_matrices(add_matrices(P1, P5), P3), P7)

		m = int(n / 2)
		Z = empty_matrix(n, n)
		for i in range(m):
			for j in range(m):
				Z[i][j] = Q1[i][j]
				Z[i][j + m] = Q2[i][j]
				Z[i + m][j] = Q3[i][j]
				Z[i + m][j + m] = Q4[i][j]
		return Z

# week 3
def quick_sort(arr):
	"""
	Sorts an array using quick sort
		Parameters:
			arr (int[]): An array of integers

		Returns:
			arr (int[]): A sorted array of integers
	"""
	if len(arr) < 2:
		return arr

	def pivot(a):
		pivot_idx = 0
		pivot = a[pivot_idx]

		for i in range(1, len(a)):
			if pivot > a[i]:
				pivot_idx += 1
				swap(a, i , pivot_idx)

		swap(a, 0, pivot_idx)
		return pivot_idx

	pivot_idx = pivot(arr)
	leftArr = arr[0:pivot_idx + 1]
	rightArr = arr[pivot_idx + 1:]
	return quick_sort(leftArr) + quick_sort(rightArr)

# week 4
def min_cut(graph):
	"""
	Calculates the minimal cut of a graph using Karger's randomized contraction algorithm
		Parameters:
			graph (Graph): A graph to be examined

		Returns:
			vertices (dict): A dictionary containing the remaining vertices which represent the minimal cut
	"""
	while len(graph.get_vertices()) > 2:
		v1, v2 = graph.get_random_edge()
		graph.contract_edge(v1, v2)
	return graph.get_vertices()

def min_cut_len(graph, increase_success_rate = False):
	"""
	Calculates the amount of the edges intersecting the minimal cut of a graph
		Parameters:
			graph (Graph): A graph to be examined

		Returns:
			minimum (int): The amount of edges intersecting the minimal cut of a graph
	"""

	# calculate n choose r
	# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
	def ncr(n, r):
		r = min(r, n - r)
		numer = reduce(op.mul, range(n, n - r, -1), 1)
		denom = reduce(op.mul, range(1, r + 1), 1)
		return numer // denom

	# calculate the amount of attempts that should be executed to increase the probability of a correct result roughly to 1/n
	# where n is the amount of vertices
	# https://en.wikipedia.org/wiki/Karger%27s_algorithm#Success_probability_of_the_contraction_algorithm
	# this is optional as it would make the algorithm too slow for larger graphs
	n = len(graph.get_vertices())
	attempts = ceil(ncr(n, 2) * log(n)) if increase_success_rate else n
	minimum = sys.maxsize
	for _ in range(attempts):
		g = graph.deep_copy()
		result = min_cut(g)
		key = list(result.keys())[0]
		minimum = min(minimum, len(result[key]))
	return minimum

def randomized_selection(arr, k):
	"""
	Finds the kth smallest element in an array of integers
		Parameters:
			arr (int[]): An array of integers
			k (int): the position of the element to look for

		Returns:
			x (int): The kth smallest element of the input array
	"""
	assert k > 0, "Second argument must be greater than 0"

	n = len(arr)
	if n == 0:
		return None
	if n == 1:
		return arr[0]

	# generate pivot index at random
	pivot_idx = randrange(0, n)
	pivot = arr[pivot_idx]
	# move pivot to the very end of array
	swap(arr, pivot_idx, n - 1)

	# i represents the tail of the "left side" of the partitioned array (everything that is less than the pivot)
	i = 0
	# j represents the index of the current item being looked at
	j = 0
	while j < n:
		# if at the end of the loop, swap pivot into its rightful place and exit the loop
		if j == n - 1:
			swap(arr, i, j)
			break
		# if the current item is less than the pivot, move it to the left
		if arr[j] < pivot:
			swap(arr, i, j)
			i += 1
			j += 1
		# otherwise simply advance the loop
		else:
			j += 1

	# translate k into computer's idea of index, since we're looking for the kth smallest item, we're looking for (k-1)th index
	search_idx = k - 1
	# if the kth smallest element happens to be the one at ith position, return it
	if i == search_idx:
		return arr[search_idx]
	# if we overshot the element, recurse on the left side of the array
	elif i > search_idx:
		return randomized_selection(arr[0:i + 1], k)
	# if we undershot, recurse on the right side
	else:
		return randomized_selection(arr[i:n], k - i)
