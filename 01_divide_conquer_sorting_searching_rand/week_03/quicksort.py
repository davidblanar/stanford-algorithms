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

	def swap(a, i1, i2):
		a[i1], a[i2] = a[i2], a[i1]

	def pivot(a):
		pivot_idx = 0;
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
