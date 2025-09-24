class Pessoa:

    # metodo construtor
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    # getter
    @property
    def nome(self) -> str:
        return self._nome

    # getter
    @property
    def idade(self) -> int:
        return self._idade

    @nome.setter
    def nome(self, nome: str) -> None:
        if isinstance(nome, str) and nome: # string vazia é false
            self._nome = nome

    @idade.setter
    def idade(self, idade: int):
        if isinstance(idade, int) and idade > 0:
            self._idade = idade

pessoa = Pessoa("Al", 2)
print(pessoa.nome, pessoa.idade)

# testando setters
pessoa.nome = "Alex"
pessoa.idade = 25

print(pessoa.nome, pessoa.idade)




