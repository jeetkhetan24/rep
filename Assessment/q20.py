string = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'

wordlist = string.split()

freq = []
for w in wordlist:
    freq.append(wordlist.count(w))

print(str(zip(wordlist, freq)))