telefone = "21971099472"
valido = True
repetidos = []

if len(telefone) == 11 and telefone.isdigit():
    print("11 dígitos, ok.")
else:
    valido = False

for i in telefone:
    contIguais = 0
    for x in telefone:
        if x == i:
            contIguais += 1
            repetidos.append(i)
    if contIguais == 3:
        print(f"Número inválido. {contIguais} números repetidos.")
        print(repetidos)
        valido = False
        break
