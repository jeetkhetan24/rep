"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original  order reserved.
"""

"""

t=[12,24,35,24,88,120,155,88,120,155]
s = []
for i in t:
	if i not in s:
		s.append(i) 
print (s)