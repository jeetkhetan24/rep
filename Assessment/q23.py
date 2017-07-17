
print("Enter the string:")
txt=raw_input()
with open('text.txt',"a") as f:
	f.write(txt)
    