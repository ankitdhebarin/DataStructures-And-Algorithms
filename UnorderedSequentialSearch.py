# Author: Ankit Dhebar

'''

Code to perform sequential search on UNORDERED list

'''

def seq_search(arr,item):

	found = False
	i = 0

	while i < len(arr) and not found:

		if arr[i] == item:
			found = True
		else:
			i += 1

	return found

mylist = [5,2,7,4,8,18,12,17]

print(seq_search(mylist,7))  # element found so it returns TRUE
print(seq_search(mylist,15)) # element not found so it returns FALSE

	