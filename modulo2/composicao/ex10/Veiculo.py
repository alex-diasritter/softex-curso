from modulo2.composicao.ex10.Motor import Motor
from modulo2.composicao.ex10.Roda import Roda


class Veiculo:

    def __init__(self, qtd_rodas: list[int]):
        self.motor = Motor()
        self.rodas: list[Roda] = self.criar_rodas(qtd_rodas)

    def criar_rodas(self, qtd: int) -> list[Roda]:

        for i in range(qtd):
            roda = Roda
            self.rodas.append(roda)

        return self.rodas

    def ligar(self) -> None:
        self.motor.ligar()
        for roda in self.rodas:
            roda.girar()
