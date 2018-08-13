# Author: Ankit Dhebar

'''
Queue Data Structure

Time Complexity

1) enqueue - O(1)
2) dequeue - O(1)
3) search  - O(n)
'''

class Queue():

	def __init__(self):
		self.items = []

	def isempty(self):
		return self.items == []

	def printqueue(self):
		print(self.items)

	def size(self):
		return len(self.items)

	def enqueue(self,item):
		print("Adding {}".format(item))
		self.items.insert(0,item)

	def dequeue(self):
		print("removing ",self.items[0])
		return self.items.pop()


queue = Queue()

print(queue.isempty())
print(queue.size())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

queue.printqueue()
queue.dequeue()
queue.printqueue()




