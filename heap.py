from heapq import heappush, heappop

class Heap():
	def __init__(self, comparator = lambda x: x):
		self.heap = []
		self.comparator = comparator

	def __str__(self):
		return str(self.heap)

	def peek(self):
		return self.comparator(self.heap[0])

	def size(self):
		return len(self.heap)

	def insert(self, val):
		value = self.comparator(val)
		heappush(self.heap, value)

	def extract(self):
		value = heappop(self.heap)
		return self.comparator(value)
