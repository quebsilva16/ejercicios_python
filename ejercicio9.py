from datetime import date
print('Escriba la primera fecha ')
year_fecha_1 = int(input('Escriba el año: '))
month_fecha_1 = int(input('Escriba el mes: '))
day_fecha_1 = int(input('Escriba el dia: '))
fecha_1 = date(year_fecha_1, month_fecha_1, day_fecha_1)
input('Escriba la segunda fecha ')
year_fecha_2 = int(input('Escriba el año: '))
month_fecha_2 = int(input('Escriba el mes: '))
day_fecha_2 = int(input('Escriba el dia: '))
fecha_2 = date(year_fecha_2, month_fecha_2, day_fecha_2)

diferencia = fecha_2 - fecha_1
print(diferencia)
