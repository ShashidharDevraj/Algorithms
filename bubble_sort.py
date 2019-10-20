# Bubble Sort Algo. Implementation

def bubble_sort(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j+1]:
				alist[j], alist[j+1] = alist[j+1], alist[j] 
	return alist

alist = [10,3,7,4]
sort = bubble_sort(alist)
print(sort)


