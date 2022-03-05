print('Conector de cadenas')
primera_base = input('Escriba la primera cadena: ')
segunda_cadena = input('Escriba la segunda cadena: ')
cadena_base = primera_base + ' ' + segunda_cadena
while True:
    print('Quieres agregar otra cadea? ')
    print('1) Yes')
    print('2) No')
    respusta = int(input('ingresa tu respuesta: '))

    if respusta == 1:
        cadena_extra = input('Escriba la otra cadena: ')
        suma_de_cadena = cadena_base + ' ' + cadena_extra
        cadena_base = suma_de_cadena


    elif respusta == 2:
        print(cadena_base)
        break



