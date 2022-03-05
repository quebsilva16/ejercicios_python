my_diccionario = {
    'numero1': 10,
    'numero2': 10,
}
my_sets = {12, 11, 33}
my_listas = [10,10,10,10]
my_tuplas = (10,10,10,10,10)

print('Suma de numeros')
print('1) Diccionario')
print('2) Set')
print('3) Tupla')
print('4) Lista')
eleccion = int(input('Elige la opcion: '))
suma = 0

if eleccion == 1:
    for i in my_diccionario.values():
        suma += i
elif eleccion == 2:
    for my_set in my_sets:
        suma += my_set
elif eleccion == 3:
    for my_tupla in my_tuplas:
        suma += my_tupla
elif eleccion == 4:
    for my_lista in my_listas:
        suma += my_lista
print(suma)


