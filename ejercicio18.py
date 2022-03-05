import string
datos = input('Ingrese su nombre: ')
for dato in datos:
    letra = dato.isupper()
    if letra == True:
        break

if letra == True:
    print('Esta palabra tiene mayusculas')
else:
    print('Esta palabra no tiene mayusculas')
