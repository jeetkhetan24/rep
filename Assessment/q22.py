print("Enter the srting")
a=raw_input()
b=list(a)
digit,alpha=0,0
for i in range(len(b)):
	if (b[i].isdigit()):
		digit=digit+1
	elif (b[i].isalpha()):
		alpha=alpha+1

print("No. of Numbers:",digit)
print("No. of Alphabet:",alpha)