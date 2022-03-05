nombre_archivo = input('Ingrese el nombre de su archivo: ')
ubicando_punto =(nombre_archivo.find('.'))
borrandopunto = nombre_archivo.replace('.', ' ')
nombre = nombre_archivo[ubicando_punto:len(nombre_archivo)]
print(nombre[1:len(nombre)])
