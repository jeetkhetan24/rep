def add(a,b):
	print a+b

def sub(a,b):
	print a-b

def mul(a,b):
	print a*b
def div(a,b):
	if(b==0 ):
		print "Cannot be Divided"
	else:
		print float(a/b)

def mod(a,b):
	if(b==0):
		print "Cannot be Divided"
	else:
		print float(a%b)
c=1
while(c!=0):
	print "Enter the 1st Number:"
	a=float(raw_input())
	print "Enter the 2nd Number:"
	b=float(raw_input())
	print "Enter 1.addition 2.subtraction 3.Multiplication 4.Division 5.modulus"
	c=int(raw_input())

	if(c==1):
		add(a,b)
	elif(c==2):
		sub(a,b)
	elif(c==3):
		mul(a,b)
	elif(c==4):
		div(a,b)
	elif(c==5):
		mod(a,b)
	elif(c==0):
		exit()
	print "press 0 to exit and 1 to continue"
	d=int(raw_input())
	c=d




