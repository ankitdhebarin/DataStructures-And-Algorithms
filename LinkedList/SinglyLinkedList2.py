class Node():

	def __init__(self,initdata):

		self.data = initdata
		self.next = None

class SinglyLinkedList():

	def __init__(self):

		self.head = None


	def isempty(self):
		return self.head == None


	def size(self):
		current = self.head
		count = 0

		while current != None:
			count += 1
			current = current.next

		return count

	def add(self,item):
		print("Adding {}".format(item))
		temp = Node(item)
		temp.next = self.head
		self.head = temp


	def search(self,item):
		current= self.head
		found = False

		while current != None:

			if current.data == item:
				found = True

			else:
				current = current.next

		return found


	def remove(self,item):
		current = self.head
		found = False
		prev = None

		while not found:

			if current.data == item:
				found = True

			else:
				prev = current
				current = current.next

		if prev == None:
			self.head = current.next
		else:
			prev.next = current.next

s = SinglyLinkedList()
print(s.isempty())
print(s.size())

s.add(10)
s.add(20)
s.add(30)
s.add(40)
s.add(50)

print(s.size())
print(s.search(70))

s.remove(40)
print(s.size())
print(s.search(40))