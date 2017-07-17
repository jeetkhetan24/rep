"""Write a program to Find the Sum of Digits in a Number"""

import logging
logging.basicConfig(filename='sum.log',level=logging.DEBUG)

logging.info("Start of code")
n=int(input("Enter a number:"))
tot=0

#WHILE LOOP FOR PRINTING SUM OF DIGITS 
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n/10
print("Sum of digits is:",tot)