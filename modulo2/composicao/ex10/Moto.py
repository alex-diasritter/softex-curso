from modulo2.composicao.ex10.Veiculo import Veiculo


class Moto(Veiculo):

    def __init__(self, qtd_rodas: int):
        super().__init__(qtd_rodas)

motoca = Moto(2)
motoca.ligar()