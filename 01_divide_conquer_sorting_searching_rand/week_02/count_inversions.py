import math

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

		mid = math.floor(len(arr) / 2)
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
