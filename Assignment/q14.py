"""
Write a Python program to get next day of a given date. 

Expected Output:
Input a year: 2016                                                      
Input a month [1-12]: 08                                                
Input a day [1-31]: 23                                                  
The next date is [yyyy-mm-dd] 2016-8-24 
"""


print "Enter the year"
y=int(raw_input())
print "enter the month(1-12)"
m=int(raw_input())
print "Enter the date(1-31)"
d=int(raw_input())

if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):		#CHECKS IF THE MONTHS IS A 31 DAY MONTH
	if(d<31):
		d=d+1
		print " The next date is "+str(y)+"-"+str(m)+"-"+str(d)
	else:
		if(m!=12):
			d=1
			m=m+1
			print " The next date is "+str(y)+"-"+str(m)+"-"+str(d)
		else:
			d=1
			m=1
			y=y+1
			print " The next date is "+str(y)+"-"+str(m)+"-"+str(d)
elif(m==6 or m==4 or m==9 or m==11):		# CHECKS FOR A #) DAY MONTH
	if(d<30):
		d=d+1
		print " The next date is "+str(y)+"-"+str(m)+"-"+str(d)
	else:
		d=1
		m=m+1
		print " The next date is "+str(y)+"-"+str(m)+"-"+str(d)
else:
	if(d<28):
		d=d+1
		print " The next date is "+str(y)+"-"+str(m)+"-"+str(d)
	else:
		d=1
		m=m+1
		print " The next date is "+str(y)+"-"+str(m)+"-"+str(d)
	