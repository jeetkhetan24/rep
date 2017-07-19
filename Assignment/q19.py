"""
Please write a program which count and print the numbers of each character in a string input by console.
"""

i = raw_input("Enter the string ")

s = set(i)

for x in s:

    print x + "," + str(i.count(x))