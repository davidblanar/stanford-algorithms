class UnionFind:
	def __init__(self):
		self.data = {}

	def insert(self, parent, child):
		self.data[child] = parent

	# return the parent of the child
	def find(self, child):
		return self.data[child]
	
	# merge two groups, group g2 becomes part of g1
	def union(self, g1, g2):
		key = self.data[g2]
		for child in self.data:
			if self.data[child] == key:
				self.data[child] = g1

	# determines if two children belong to the same parent
	def connected(self, c1, c2):
		return self.data[c1] == self.data[c2]

	def get_data(self):
		return self.data
