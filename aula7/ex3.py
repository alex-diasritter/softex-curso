position = 0
comand = ""
ligado = True
while ligado:
    print("Avançar - 1\n"
          "Recuar - 2\n"
          "Status - 3\n"
          "Desligar - 0")
    comand = input("Digite a opção desejada: [1-2-3-0]")
    comandInt = int(comand)

    if comandInt == 1:
        position += 1
    elif comandInt == 2:
        position -= 1
    elif comandInt == 3:
        print(f"A posição atual é: {position}\n")
    elif comandInt == 0:
        ligado = False
    else:
        print("Digite apenas uma das opções.\n")
 
print("Robô desligado.")