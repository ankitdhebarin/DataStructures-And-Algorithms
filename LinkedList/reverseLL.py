class Node():

	def __init__(self,initdata):
		self.data = initdata
		self.next = None
		self.prev = None

	def reverseLL(head):
		current = head
		prev = None
		Next = None

		while current:

			Next = current.next
			
			current.next = prev

			prev = current
			current = Next

		return prev

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

print(a.next.data)
print(b.next.data)
print(c.next.data)
#print(d.next.data)

Node.reverseLL(a)

print(d.next.data)
print(c.next.data)
print(b.next.data)



