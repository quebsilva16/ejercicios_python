#dato = int(input('Ingrese un numero: '))
dato = input('Ingrese un numero: ')
tipo_dato = dato.isdigit()
if tipo_dato == True:
    print('Tu dato es valido')
else:
    print('El dato que ingreso no es un numero')