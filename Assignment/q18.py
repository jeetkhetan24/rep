"""
Please write a program which accepts a string from console and print it in reverse order
"""


a=raw_input()
b=list(a)
i=len(b)
while(i>0):
	print b[i-1],	#PRINTS THE LIST IN REVERSE ORDER
	i=i-1
	