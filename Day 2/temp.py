print "Enter Celcius(C) or Fahrenheit(F):"
a=raw_input()
print "enter the value:"
b=float(raw_input())
x=0
if(a=="C"):
	x= b*1.8 + 32
	print x
elif(a=="F"):
	x= (b-32)/1.8
	print x
else:
	print "Wrong input"

