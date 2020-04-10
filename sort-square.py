############
#Given a list of sorted numbers (can be both negative or positive), return the list of numbers squared in sorted order.
############


def square_Function(nums):
	positive_Array = [] #0 1 4 5

	negative_Array = [] #-1 -3 -5 -6

	for i in nums:
		if i < 0:
			negative_Array.append(i)
		else:
			positive_Array.append(i)
	
	negative_Array.reverse()

	new_Array = [j**2 for j in positive_Array]
	new_Array_two = [k**2 for k in negative_Array]

	square_sorted = merge(new_Array, new_Array_two)

	return square_sorted
	
def merge(l, r):
	square_sorted = []
	while len(l) > 0 and len(r)>0:
		if l[0] < r[0]:
			square_sorted.append(l[0])
			l.pop(0)
		else:
			square_sorted.append(r[0])
			r.pop(0)
	for i in l:
		square_sorted.append(i)
	for i in r:
		square_sorted.append(i)
	
	
	return square_sorted

#driver_function
print(square_Function([-5, -3, -1, 0, 1, 4, 5]))

# [0, 1, 1, 9, 16, 25, 25]
# O(n)
