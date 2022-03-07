from itertools import combinations

vocales = ['a', 'e', 'i', 'o', 'u']
temp = combinations(vocales, 2)

for i in list(temp):
    print(i)
