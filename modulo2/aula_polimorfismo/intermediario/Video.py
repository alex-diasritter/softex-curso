from modulo2.aula_polimorfismo.intermediario.Midia import Midia

class Video(Midia):

    def __init__(self, nome: str, duracao_seg: float, resolucao: str):
        super().__init__(nome, duracao_seg)
        self.resolucao = resolucao

    def exibir(self) -> None:
        print(f'Nome: {self.nome}. Duração: {self.duracao_seg:.2f}. Resolução: {self.resolucao}')

    def __str__(self):
        return f"{self.nome}, {self.resolucao}"