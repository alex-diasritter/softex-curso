from modulo2.desafios_poo.avançado.Motor import Motor

class Carro:
    def __init__(self, modelo: str, potencia: Motor):
        self.modelo = modelo
        self.potencia = 100

    def exibir_potencia(self) -> None:
        print(f'Potencia: {self.potencia}')

carro = Carro('Gol', Motor(1000))
carro.exibir_potencia()