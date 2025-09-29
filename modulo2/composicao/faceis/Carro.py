from modulo2.composicao.faceis.Motor import Motor

class Carro:

    def __init__(self, motor: Motor):
        self.motor = motor

    def ligarCarro(self):
        self.motor.ligar()

motor = Motor()
carro = Carro(motor)
carro.ligarCarro()