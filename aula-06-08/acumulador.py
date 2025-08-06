array = []

for i in range(5):
    numero = int(input(f'Digite um número inteiro: '))
    array.append(numero)

print(f"\nLista de números digitados: {array}")

soma_total = 0
for numero in array:
    soma_total += numero

print(f"A soma de todos os números na lista é: {soma_total}")

