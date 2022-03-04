'''Escriba un programa Python que acepte una secuencia de números separados por comas del usuario y genere una lista y una tupla con esos números
Datos de muestra: 3, 5, 7, 23
Salida:
Lista: ['3', ' 5' , ' 7', ' 23']
Tupla: ('3', ' 5', ' 7', ' 23')'''

peticion_de_numero = input('Digite la secuencia de numeros')
list = list(peticion_de_numero)
tuple = tuple(peticion_de_numero)
print(list)
print(tuple)
