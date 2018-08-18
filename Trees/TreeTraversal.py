class BinaryTree():

	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None


def InOrder(root):

	if root:
		InOrder(root.left)

		print(root.val)

		InOrder(root.right)


def PreOrder(root):

	if root:

		print(root.val)

		PreOrder(root.left)

		PreOrder(root.right)


def PostOrder(root):

	if root:

		PostOrder(root.left)

		PostOrder(root.right)

		print(root.val)



root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

print("PreOrder traversal")
PreOrder(root)

print("InOrder traversal")
InOrder(root)

print("PostOrder traversal")
PostOrder(root)