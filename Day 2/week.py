def week(a):

	week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
	if a not in week:
		print "Not valid"
	else:
		b = week.index(a)
		print b+1


def month(a):
	month = ['january', 'february', 'march', 'april', 'may', 'june', 'july','august', 'september', 'october', 'november', 'december']
	if a not in month:
		print "Not valid"
	else:
		b = month.index(a)
		print b+1

print "Enter the week:"
x=raw_input()
x=x.lower()
week(x)
print "Enter the month:"
y=raw_input()
y=y.lower()
month(y)
