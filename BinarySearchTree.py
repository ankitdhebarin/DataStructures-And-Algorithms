class Node():

	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


	def insert(self,data):
		''' Inserting Data into BST '''

		if self.data == data:
			return False		# BST cannot contain duplicate data

		elif data < self.data:
			''' Data less than root so it should be inserted to the left of root node '''
			if self.left == None:
				self.left = Node(data)
			else:
				self.left.insert(data)

		else:
			''' Data greater than root so it should be inserted to the right of root node '''
			if self.right == None:
				self.right = Node(data)
			else:
				self.right.insert(data)


	def minValueNode(self,node):
		''' Find node with min value '''

		current = node

		while current.left is not None:
			current = current.left

		return current


	def find(self,data):
		''' This function checks whether data is in Tree or not '''

		if self.data == data:
			return data

		elif data < self.data:
			if self.left:
				return self.left.find(data)
			else:
				return False

		else:
			if self.right:
				return self.right.find(data)
			else:
				return False


	def delete(self,data):
		''' This function is used to delete data from the Tree '''

		
		


root = Node(8)
root.insert(3)
print(root.find(6))