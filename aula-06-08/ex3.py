n = int(input('digite um nmr inteiro: '))

resultado = 0
multiplicador = 1
while multiplicador <= 10:
    resultado = n * multiplicador
    print(f'{n} x {multiplicador} = {resultado}')
    multiplicador += 1
