class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

prod1 = Produto("Caderno", 15.50)
prod2 = Produto("Caneta", 3.00)

print(prod1.nome, prod1.valor)
print(prod2.nome, prod2.valor)