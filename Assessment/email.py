"""
Assuming that we have some email addresses in the "username@companyname.com" format,
 please write program to print the user name of a given email addres
s. Both user names and company names are composed of letters only.
"""

a=raw_input("Enter The string")

result=a.find('@')		#TAKE THE GIVEN CHARACTER AS INPUT
for i in range(result):
	print(a[i]),