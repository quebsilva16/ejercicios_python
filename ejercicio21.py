from itertools import permutations

vocales = ['a', 'e', 'i', 'o', 'u']
combinaciones = permutations(vocales, 5)
for combinacion in combinaciones:
    print(combinacion)
