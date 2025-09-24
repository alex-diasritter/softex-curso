from math import pi

class Circulo:

    def __init__(self, raio: float):
        self._raio = raio

    @property
    def raio(self) -> float:
        return self._raio

    @raio.setter
    def raio(self, raio: float) -> None:
        if isinstance(raio, float) and raio > 0:
            self._raio = raio

    def calcular_area(self) -> float:
        result = pi * float(self.raio) ** 2
        print(f"Area do raio: {result:.2f}")
        return result

circulo = Circulo(4.0)

circulo.calcular_area()

