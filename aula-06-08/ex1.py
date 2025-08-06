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