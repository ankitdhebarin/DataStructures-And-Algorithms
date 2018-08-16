# Author: Ankit Dhebar

''' 
This is a Binary search algorithm with recursion
'''

def BinarySearchRecursion(arr,item):

	if len(arr) == 0:
		return False

	else:
		mid = len(arr) / 2

		if arr[mid] == item:
			return True

		else:
			if item < arr[mid]:
				return BinarySearchRecursion(arr[:mid],item)
			else:
				return BinarySearchRecursion(arr[mid+1:], item)

mylist = [10,20,30,40,50,60,70,80,90]

print(BinarySearchRecursion(mylist,70)) 
print(BinarySearchRecursion(mylist,100))