"""
.Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address.
Both user names and company names are composed of letters only.
"""

a=raw_input()
b=a.find("@")
c=a.find(".")
while(b<(c-1)):
	print a[b+1],
	b=b+1