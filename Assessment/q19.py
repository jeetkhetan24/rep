class operations():


	def input(self):
		print("Enter the string")
		global a
		a=raw_input()

	def display(self):
		print (a)


b=operations()
b.input()
b.display()