# Author: Ankit Dhebar

'''
Singly Linked List

Access = O(n)
Search = O(n)
Insertion = O(1)
Deletion = O(1)

'''

class Node():

	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data


	def setData(self,newData):
		self.data = newData


	def getNext(self):
		return self.next


	def setNext(self,newNext):
		self.next = newNext



class SingleLinkedList():

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0

		while current != None:
			count += 1
			current = current.getNext()

		return count


	def search(self,item):
		found = False
		current = self.head

		while current != None and not found:

			if current.getData() == item:
				found = True

			else:
				current = current.getNext()

		return found


	def remove(self,item):
		current = self.head
		prev = None
		found = False

		while not found:
			if current.getData() == item:
				found = True

			else:
				prev = current
				current = current.getNext()

		if prev == None:
			self.head = current.getNext()
		else:
			prev.setNext(current.getNext())


mylist = SingleLinkedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.isEmpty())
print(mylist.size())
print(mylist.search(27))
mylist.remove(26)
print(mylist.size())





