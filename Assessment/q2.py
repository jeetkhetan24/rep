"""Write a program to demonstrate printing pattern of alphabets

A 
B C 
D E F 
G H I J 
K L M N O"""

#ord() is used to get the ASCII valuse of the string

import logging
logging.basicConfig(filename='pattern.log',level=logging.DEBUG)

stri=ord('A')
# FOR LOOP FOR PRINTING THE PATTERN
for i in range(0, 6):
    for j in range(i):
        print(chr(stri)),
        stri=stri+1
    print ""