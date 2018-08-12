# Author: Ankit Dhebar

'''
Bubble Sort Algorithm
'''

def bubbleSort(alist):

	for i in range(len(alist)-1,0,-1):
		print("First loop",i)
		for j in range(i):
			print("Second loop",j)
			if alist[j] > alist[j+1]:
				temp = alist[j]
				alist[j] = alist[j+1]
				alist[j+1] = temp


bubble = [54,26,93,17,77,31,44,55,20]
bubbleSort(bubble)
print(bubble)

'''
Complexity of BubbleSort 

BestCase	AverageCase		WorstCase
Omega(n)	 O(n^2)			 O(n^2)