"""
Please write a program which prints all permutations of [1,2,3]
"""


from itertools import permutations
lists = list(permutations(range(1, 4))) # PRINTS ALL THE PERMUTATION OF THE NUMBERS INCLUDING THE FIRST ONE AND EXCLUDING THE LAST
print lists