monto = int(input('Ingresa el monto: '))
tasa_intereses = float(input('Tasa de interes: '))
year = int(input('Años a calcular: '))
multiplicar_tasa_interes = tasa_intereses / 100 + 1
i = 0
while i != year:
    calcular = monto * multiplicar_tasa_interes
    monto = calcular
    i += 1
print("{0:.2f}".format(calcular))
