with open('text.txt') as f:
    print sum(1 for lines in f)