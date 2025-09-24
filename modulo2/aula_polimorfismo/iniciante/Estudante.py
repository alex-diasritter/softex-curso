from modulo2.aula_polimorfismo.iniciante.Pessoa import Pessoa

class Estudante(Pessoa):

    def __init__(self, nome: str, idade: int, curso: str):
        super().__init__(nome, idade)
        self.curso = curso

    # metodo sobrescrito
    def apresentar(self) -> str:
        apresentacao = f'Olá! Meu nome é {self.nome}, tenho {self.idade} e faço o curso de {self.curso}.'
        return apresentacao

estudante = Estudante("Alex", 25, "Engenharia de Software")
pessoa = Pessoa("Fulano", 56)

# fazer a tipagem da lista nos dá o poder de acessar os metodos dos objetos na lista
lista:list[Pessoa] = [pessoa, estudante]

for p in lista:
    print(p.apresentar())
