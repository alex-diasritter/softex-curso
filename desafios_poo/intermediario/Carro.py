class Carro:
    def __init__(self, modelo: str, combustivel: float):
        self.modelo = modelo
        self.combustivel = combustivel
        self.consumo = 10.00

    def abastecer(self, combustivel: float) -> None:
        self.combustivel += combustivel
        print(f"Carro abastecido com: {combustivel:.2f} litros.")

    def dirigir(self, distancia: int) -> None:
        if self.combustivel <= 0:
            print("Não é possível dirigir - tanque vazio!")
            return

        combustivel_necessario = distancia / self.consumo

        if combustivel_necessario <= self.combustivel:
            self.combustivel -= combustivel_necessario
            print(f"Dirigiu {distancia:.2f} km. Combustível restante: {self.combustivel:.2f} litros")
        else:
            print("Não há combustível restante.")

carro = Carro("Corolla", 0.00)
carro.abastecer(1.00)
carro.dirigir(10)
carro.dirigir(11)
carro.abastecer(200000)
carro.dirigir(100000)