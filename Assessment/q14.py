"""
Write a Python program to check if a given positive integer is a power of two

"""


print("Enter The Integer")
a=int(raw_input())
print(a)
x=True
while(a!=1):
	if(a%2==0):
		a=a/2
		x=True
	else:
		x=False

if(x==True):
	print("Power of 2")
else:
	print("Not a Power of 2")