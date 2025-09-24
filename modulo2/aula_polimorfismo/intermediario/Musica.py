from modulo2.aula_polimorfismo.intermediario.Midia import Midia


class Musica(Midia):
    def __init__(self, nome: str, duracao_seg: float, artista: str):
        super().__init__(nome, duracao_seg)
        self.artista = artista

    def exibir(self) -> None:
        print(f'Nome: {self.nome}. Duração: {self.duracao_seg:.2f}. Artista: {self.artista}')

    def __str__(self):
        return f"{self.nome}, {self.artista}"