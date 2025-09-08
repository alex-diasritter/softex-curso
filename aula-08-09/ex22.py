jogadores = {"alex": 0, "jaqueline": 0}
print("Placar inicial: ")
print(jogadores)
cont = 0
while True:

    if cont < 1:
        jogadores.update({"alex": 1})
        cont += 1

    print("\nPlacar atual:")
    print(jogadores)


    print("\n1 - adicionar pontos." \
    "\n2 - remover pontos." \
    "\n3 - adicionar jogador." \
    "\n4 - parar\n")

    escolhaMenu = input("Digite sua escolha: ")

    if escolhaMenu == "4":
        break

    elif escolhaMenu == "1":

        jogadorEscolhido = input("\nQual jogador pontuar? ")
        pontosInt = int(input("Digite os pontos: [int] "))

        for jogador, pontos in jogadores.items():
            if jogador == jogadorEscolhido:
                jogadores.update({jogadorEscolhido: pontosInt})
                break
            else:
                break

    elif escolhaMenu == "2":

        jogadorEscolhido = input("\nQual jogador decrementar? ")
        pontosInt = int(input("Digite os pontos: [int] "))

        for jogador, pontos in jogadores.items():
            if jogador == jogadorEscolhido:
                jogadores.update({jogadorEscolhido: pontosInt})
                break

    elif escolhaMenu == "3":

        jogadorNovo = input("\nQual o nome do jogador? ")
        pontos = int(input("Digite os pontos: [int] "))

        jogadores.update({jogadorNovo: pontos})


# adicionar validação e try catch
# resolver lógica para decrementar pontos