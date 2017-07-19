"""
.Write a program that computes the net amount of a bank account based a transaction log from console input.
"""
print "enter the command and the amount D or W "
final = 0
while True:
    s = raw_input()
    if not s:
        break
    a = s.split(" ")
    trans = a[0]
    amt = int(a[1])
    if trans=="D":
        final=final+amt
    elif trans=="W":
        final=final-amt
    else:
        pass
print final