from modulo2.composicao.ex10.Veiculo import Veiculo


class Carro(Veiculo):

    def __init__(self, qtd_rodas: int):
        super().__init__(qtd_rodas)

palio: Carro = Carro(4)
palio.ligar()