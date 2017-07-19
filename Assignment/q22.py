"""
By using list comprehension, please write a program to print the list after removing the v0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].-+
"""
a=[12,24,35,70,88,120,155]
for i in range(1,len(a)):
	if(i%2!=0):
		print a[i]

