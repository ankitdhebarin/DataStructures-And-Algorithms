class Node():

    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None


class DoublyLinkedList():

    def __init__(self):
        self.head = None


    def add(self,item):

        temp = Node(item)

        # If the node to be added is the first node
        if self.head == None:
            temp.next = self.head
            temp.prev = None
            self.head = temp

        else:

        # If the node to be added is not the first node

            temp.next = self.head
            self.head.prev = temp
            self.head = temp


    def remove(self,item):

        current = self.head

        while current != None:

            if current.data == item:

                # If its not the first node in the list
                if current.prev is not None:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                else:
                # if its the first node in the list
                    self.head = current.next
                    current.prev = None

            current = current.next


    def printdll(self):

        current = self.head

        while current != None:
            print("Data",current.data)
            print("Current",current)
            print("Next",current.next)
            print("Previous",current.prev)
            current = current.next


dll = DoublyLinkedList()
dll.add(10)
dll.add(20)
dll.add(30)

dll.printdll()

dll.remove(20)
print("-------------------")
dll.printdll()