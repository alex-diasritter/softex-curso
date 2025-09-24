class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return 2 * (self.base + self.altura)

retangulo = Retangulo(10.20, 20.42)

print(f'{retangulo.calcular_area()}')
print(f'{retangulo.calcular_perimetro()}')


