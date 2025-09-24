lista1 = ["red", "blue", "white", "black", "green"]
lista2 = ["blue", "black", "blue", "green", "orange"]
lista3 = []

for e in lista1:
    if e in lista2 and e not in lista3:
        lista3.append(e)
print(lista3)