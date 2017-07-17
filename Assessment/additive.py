"""
Write a Python program to find whether it contains an additive sequence or not.
The additive sequence is a sequence of numbers where the sum of the first two numbers is equal to the third one.
Sample additive sequence: 6, 6, 12, 18, 30
In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
Also, you can split a number into one or more digits to create an additive sequence.
Sample additive sequence: 66121830
In the above sequence 6 + 6 =12, 6 + 12 = 18, 12 + 18 = 30....
Note : Numbers in the additive sequence cannot have leading zeros.

"""



a = [6,6,12,18,30]
i=1
for i in range(0,len(a)-3):
	if(a[i]+a[i+1]==a[i+2]):
		x=1
	else:
		x=0
		break

if(x==1):
	print("The sequence is additive")
else:
	print("The sequence is not additive")