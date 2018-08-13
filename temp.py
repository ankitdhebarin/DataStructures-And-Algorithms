# Author: Ankit Dhebar

'''
Stacks data structure
'''

class Stack():

	def __init__(self):
		self.items = []
	
	def isempty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def push(self,item):
		print("Adding {}".format(item))
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]


stack = Stack()

print(stack.isempty())
print(stack.size())
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print(stack.isempty())
print(stack.size())

print(stack.peek())
print(stack.pop())
print(stack.peek())

'''
Time complexity

Push: O(1)
Pop: O(1)
Search: O(n)
