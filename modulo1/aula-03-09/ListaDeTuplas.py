listaDeTuplas = [("Teclado", 50, 2), ("Mouse", 25.50, 4), ("Monitor", 300, 1), ("Webcam", 75.2, 2), ("Outro",10,2),("Outro2",100,2)]

listaFiltrada = []
nomes_unicos = set()

for produto, preco, qnt in listaDeTuplas:
    if float(preco) * float(qnt) >= 100:
        listaFiltrada.append((produto, preco, qnt))
    nomes_unicos.add(produto)

print(listaFiltrada)
print(nomes_unicos)