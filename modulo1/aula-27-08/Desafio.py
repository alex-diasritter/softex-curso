lA = input("lado A: ")
lB = input("lado B: ")
lC = input("lado C: ")

if lA.isdigit() and lB.isdigit() and lC.isdigit():
    lA = int(lA)
    lB = int(lB)
    lC = int(lC)
    if lA <= 0 or lB <= 0 or lC <= 0:
        print("Entradas inválidas. Os lados devem ser números positivos.")
else:
    print("Entradas inválidas. Por favor, insira números inteiros positivos.")

soma = True
if lA > lB + lC:
    soma = False
if lB > lA + lC:
    soma = False
if lC > lA + lB:
    soma = False

dif = True
if lA < abs(lB - lC):
    dif = False
if lB < abs(lA - lC):
    dif = False
if lC < abs(lA - lB):
    dif = False

if soma and dif:
    print(f"Os lados {lA}, {lB} e {lC} PODEM formar um triângulo.")
else:
    print(f"Os lados {lA}, {lB} e {lC} NÃO PODEM formar um triângulo.")