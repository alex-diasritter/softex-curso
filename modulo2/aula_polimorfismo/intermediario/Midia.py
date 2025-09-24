class Midia:
    def __init__(self, nome: str, duracao_seg: float):
        self.nome = nome
        self.duracao_seg = duracao_seg

    def exibir(self) -> str:
        return f'Nome: {self.nome}. Duração: {self.duracao_seg:.2f}'

    def __str__(self):
        return f"{self.nome}"