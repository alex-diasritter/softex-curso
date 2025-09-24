lista = [1,2,3,4,5,6,7,8,9,10,11,12]
primos = []

for numero in lista:
    if numero == 2:
        primos.append(numero)
    for n in range(0, numero):
        if numero % 2 == 1 and numero not in primos and numero != 1:
            primos.append(numero)
print(primos)

#errado