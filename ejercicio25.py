primos = list()
def es_primo(numero):

    if numero == 2:
        primos.append(numero)
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        primos.append(numero)

dato =  int(input('Ingresa el numero: '))
for i in range(2, dato+1):
    es_primo(i)
print(primos)