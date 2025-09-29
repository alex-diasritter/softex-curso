from modulo2.composicao.faceis.Cafe import Cafe
from modulo2.composicao.faceis.Agua import Agua


class Cafeteira:

    def __init__(self, agua: Agua, cafe: Cafe):
        self.agua = agua
        self.cafe = cafe

    def prepararCafe(self):
        self.cafe.moer()
        self.agua.aquecerAgua()
        print('Café preparado!')