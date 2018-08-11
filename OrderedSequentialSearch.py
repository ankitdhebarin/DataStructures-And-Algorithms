# Author: Ankit Dhebar

'''

This is an Ordered Sequential search time complexity is different for this algorithm

'''

def OrderedSeqSearch(arr,item):

	i = 0
	found = False
	stopped = False

	while i < len(arr) and not found and not stopped:

		if arr[i] == item:
			found = True

		else:
			if arr[i] > item:
				stopped = True
			i += 1
		

	return found

mylist = [10,20,30,40,50,60,70]

print(OrderedSeqSearch(mylist,30)) # Item found so returns True

print(OrderedSeqSearch(mylist,35)) # Item not found so returns False BUT the pointer will not search after 40 and thus time
								   # cont.. complexity would be better than an Unordered search algorithm.

