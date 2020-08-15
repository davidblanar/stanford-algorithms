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
