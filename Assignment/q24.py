"""
.Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
"""
a=raw_input()
b=list(a)
i=0
for i in range(1,len(b)):
	if(a[i]==str(0) or a[i]==str(1) or a[i]==str(2) or a[i]==str(3) or a[i]==str(4) or a[i]==str(5) or a[i]==str(6) or a[i]==str(7) or a[i]==str(8) or a[i]==str(9)):
		print a[i],