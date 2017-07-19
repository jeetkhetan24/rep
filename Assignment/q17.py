"""
Please write a program which accepts a string from console and print the characters that have even indexes

H1e2l3l4o5w6o7r8l9d-
"""

a=raw_input()
b=list(a)
i=0
while(i<len(b)):
	print b[i],
	i=i+2			# PRINTS ALTERNATE CHARACTERS OF THE LIST

