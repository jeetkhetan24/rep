import logging
logging.basicConfig(filename='runtime.log',level=logging.DEBUG)

#Run Time Error Examples
try:
	logging.info("Try Statement")
	a=10
	b=15
	c="Hello"
	x=a+b+c
except:
	print("Run Time Error")
