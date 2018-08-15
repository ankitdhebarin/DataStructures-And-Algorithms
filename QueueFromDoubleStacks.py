# Author: Ankit Dhebar

'''
This algorithm shows how to implement a queue using 2 stacks.
'''

class DoubleStacks():

	def __init__(self):

		self.instack = []
		self.outstack = []

	def enqueue(self,item):
		self.instack.append(item)

	def dequeue(self):

		if not self.outstack:

			while self.instack:

				self.outstack.append(self.instack.pop())

		return self.outstack.pop()


double = DoubleStacks()

double.enqueue(10)
double.enqueue(20)
double.enqueue(30)
double.enqueue(40)
double.enqueue(50)

print("Outstack",double.outstack)
print("Instack",double.instack)

double.dequeue()

print("Outstack",double.outstack)
print("Instack",double.instack)


