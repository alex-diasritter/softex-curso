nInt = int(input('digite um nmr: '))
if nInt > 0:
    print(f"O número {nInt} é maior que 0!")
else:
    print(f'o numero {nInt} não é maior que 0!')

print('-----------------------------------------------')

precoProdutoFloat = float(input('digite o preço do produto: '))
if precoProdutoFloat >= 100.0:
    precoFinal = precoProdutoFloat - (precoProdutoFloat * 0.10)
    print('preço final com desconto de 10%: ', precoFinal)
else:
    print(f'{precoProdutoFloat} não é maior que 100.0 e não receberá 10% de desconto')

print('------------------------------------------------')

nmrInt = int(input('Digite um número para descobrirmos se é divisível por 5: '))
if nmrInt % 5 == 0:
    print(f'{nmrInt} é divisível por 5!')
else:
    print(f'{nmrInt} não é divisível por 5 :((( ')

print('-------------------------------------------------------')

n1 = int(input('digite um nmr inteiro: '))
n2 = int(input('digite outro nmr inteiro: '))

if n1 == n2:
        print(f'os numeros são iguais')
elif n1 > n2:
        print(f'{n1} é maior que {n2}')
else:
    print(f'{n2} é maior que {n1}')

print('-------------------------------------------------------')

n = int(input('digite um nmr inteiro: '))
if n % 2 == 0:
    print(f'o número {n} é par.')
else:
     print(f'o nmr {n} é ímpar.')

print('-------------------------------------------------------')

age = int(input('digite a sua idade: '))
if age >= 0 and age <= 12:
     print(f'Criança: {age}')
elif age >= 13 and age <= 17:
     print(f'Adolescente: {age}')
else:
     print(f'Adulto: {age}')