class Pessoa:

    # não é necessário declarar os atributos antes, fazemos isso direto no construtor.
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aprensentar(self) -> None:
        print(f'Olá meu nome é {self.nome} e tenho {self.idade} anos.')


pessoa1 = Pessoa("joão", 25)
pessoa2 = Pessoa("maria", 30)

Pessoa.aprensentar(pessoa1)
Pessoa.aprensentar(pessoa2)