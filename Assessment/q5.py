"""Write a Python program to find a missing number from a list
Input : [1,2,3,4,6,7,8]
Output : 5
"""


a=[1,2,3,4,6,7,8]
x=1
for i in range(len(a)):
	if(x==a[i]):
		x=x+1
	else:
		print x
		break
