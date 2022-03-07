import sys

nombre_script = sys.argv[0]
cantidad_argumentos = len(sys.argv)
argumentos = str(sys.argv)

print('Nombre del programa: {}'.format(nombre_script))
print('Cantidad de argumentos: {}'.format(cantidad_argumentos))
print('Lista de argumentos: {}'.format(argumentos))