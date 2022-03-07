import collections
import pprint
nombre_archivo = 'text/lorem.txt'
with open(nombre_archivo, 'r') as f:
    conteo_caracteres = collections.Counter(f.read().upper())
    salida = pprint.pformat(conteo_caracteres)
print(conteo_caracteres)
