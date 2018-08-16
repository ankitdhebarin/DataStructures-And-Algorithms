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

		if self is None:
			return None

		''' Deleting only leaf nodes '''

		if data < self.data:
			self.left = self.left.delete(data)

		elif data > self.data:
			self.right = self.right.delete(data)
			
		else:

			''' Deleting node with one child '''

			if self.left is None:
				temp = self.right
				self = None
				return temp

			elif self.right is None:
				temp = self.left
				self = None
				return temp

			''' Deleting nodes with 2 children '''

			temp = self.minValueNode(self.right)
			self.data = temp.data
			self.rightChild = self.rightChild.delete(temp.data)

		return self


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

print(root.find(6))
print(root.delete(4))
print(root.find(4))