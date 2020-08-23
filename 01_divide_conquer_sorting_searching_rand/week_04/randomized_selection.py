from random import randrange, randint

def randomized_selection(arr, k):
	"""
	Finds the kth smallest element in an array of integers
		Parameters:
			arr (int[]): An array of integers
			k (int): the position of the element to look for

		Returns:
			x (int): The kth smallest element of the input array
	"""

	def swap(a, i1, i2):
		a[i1], a[i2] = a[i2], a[i1]

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
