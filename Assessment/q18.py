class operations():

	def append(self,b):
		print("Enter value to append:")
		a=raw_input()
		b.append(a)
		print(b)



	def delete(self,b):
		print("Enter value to delete:")
		a=raw_input()
		b.remove(a)
		print(b)


	def Display(self,b):
		print (b)



print("Enter the string:")
a=raw_input()
b=list(a)

o=operations()
o.Display(b)
o.append(b)
o.delete(b)