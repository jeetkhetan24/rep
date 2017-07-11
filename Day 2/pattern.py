print "Enter the max number"
a=int(raw_input())
i=0;j=0
while(i<=a):
	while (j<a):
		print ("* "), 
		j=j+1
	i=i+1
j=a
i=0
while(i<a):
	while (j>0):
		print ("* "),
		j=j-1
	i=i+1