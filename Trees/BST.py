class Node():

	def __init__(self,key):
		self.val = key
		self.left = None
		self.right = None


def inOrder(root):

	if root is not None:
		inOrder(root.left)
		print(root.val)
		inOrder(root.right)


def insert(root,node):

	# Base case
	if root is None:
		root = node

	else:
		if node.val < root.val:
			if root.left is None:
				root.left = node

			else:
				insert(root.left, node)
			
		else:
			if root.right is None:
				root.right = node

			else:
				insert(root.right, node)


def search(root,key):

	if root.val == key:
		return True

	elif key < root.val:
		if root.left:
			return search(root.left,key)

		else:
			return False
	else:
		if root.right:
			return search(root.right,key)
		else:
			return False


def minNode(node):
	current = node

	while current.left is not None:
		current = current.left

	return current


def delete(root,key):

	# Base Case
    if root is None:
        return root 
 
    # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if key < root.val:    	
		root.left = delete(root.left, key)

 
    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif(key > root.val):
        root.right = delete(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
         
        # Node with only one child or no child
        if root.left is None :
            temp = root.right 
            root = None
            return temp 
             
        elif root.right is None :
            temp = root.left 
            root = None
            return temp
 
        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minNode(root.right)
 
        # Copy the inorder successor's content to this node
        root.val = temp.val
 
        # Delete the inorder successor
        root.right = delete(root.right , temp.val)
    
    return root

r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

inOrder(r)

#print(search(r,90))
#print(search(r,25))

delete(r,70)
