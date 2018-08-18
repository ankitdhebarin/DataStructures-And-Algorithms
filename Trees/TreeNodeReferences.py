class BinaryTree():
	
	def __init__(self, rootobj):
		self.key = rootobj
		self.leftchild = None
		self.rightchild = None


	def insertLeft(self, newNode):

		if self.leftchild == None:
			self.leftchild = BinaryTree(newNode)

		else:
			t = BinaryTree(newNode)
			t.leftchild = self.leftchild
			self.leftchild = t


	def insertRight(self, newNone):

		if self.rightchild == None:
			self.rightchild = BinaryTree(newNode)

		else:
			t = BinaryTree(newNode)
			t.rightchild = self.rightchild
			self.rightchild = t


	def getLeftChild(self):
		return self.leftchild


	def getrightChild(self):
		return self.rightchild


	def getrootVal(self):
		return self.key


	def setrootVal(self,newroot):
		self.key = newroot



r = BinaryTree('a')
print(r.getrootVal())

r.insertLeft('b')
print(r.getLeftChild().getrootVal())

