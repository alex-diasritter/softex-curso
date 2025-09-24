numeros = [2,3,5,5,6,7,4,5]
target = 5
cont = 0

#cont = numeros.count(target)
#print(f"Número: {target}. Aparece {cont} vezes.")

for n in numeros:
    if n == target:
        cont += 1
print(f"Número: {target}. Aparece {cont} vezes.")