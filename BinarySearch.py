# Author: Ankit Dhebar

''' 

Please Note: For Binary Search to work, the array/list should be oredered

'''

def BinarySearch(arr,item):

	'''
	Binary Search using iterative method
	'''

	found = False
	i = 0
	first = 0
	last = len(arr) - 1

	while first < last and not found:

		mid = (first + last) / 2

		if arr[mid] == item:
			found = True

		else:
			if item < arr[mid]:
				last = mid - 1

			else:
				first = mid + 1

	return found


mylist = [10,20,30,40,50,60,70,80,90]

print(BinarySearch(mylist,70)) # returns True
print(BinarySearch(mylist,100)) # returns False