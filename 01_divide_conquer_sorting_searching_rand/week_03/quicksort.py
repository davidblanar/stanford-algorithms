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
		temp = a[i1]
		a[i1] = a[i2]
		a[i2] = temp

	def pivot(a):
		pivotIdx = 0;
		pivot = a[pivotIdx]

		for i in range(1, len(a)):
			if pivot > a[i]:
				pivotIdx += 1
				swap(a, i , pivotIdx)

		swap(a, 0, pivotIdx)
		return pivotIdx

	pivotIdx = pivot(arr)
	leftArr = arr[0:pivotIdx + 1]
	rightArr = arr[pivotIdx + 1:]
	return quick_sort(leftArr) + quick_sort(rightArr)
