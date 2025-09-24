class Robo:

    def __init__(self):
        self.robo_position = 0

    def avancar(self):
        self.robo_position += 1

    def recuar(self):
        self.robo_position -= 1

    def status(self):
        print(f"\nPOSIÇÃO ATUAL: {self.robo_position}\n")
    

robo = Robo()

ligado = True
while ligado:
    print("Avançar - 1\n"
          "Recuar - 2\n"
          "Status - 3\n"
          "Desligar - 0")
    comand = input("Digite a opção desejada: [1-2-3-0]\n")
    comandInt = int(comand)

    if comandInt == 1:
        robo.avancar()
    elif comandInt == 2:
        robo.recuar()
    elif comandInt == 3:
        robo.status()
    elif comandInt == 0:
        ligado = False
    else:
        print("Digite apenas uma das opções.\n")
 
print("Robô desligado.")
