class Pessoa:

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self) -> str:
        aprentacao = f'Olá! Meu nome é {self.nome} e tenho {self.idade} anos.'
        return aprentacao