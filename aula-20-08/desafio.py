conta_corente = "13123"
senha_usuario = "senha"
saldo_atual = int(0)
limite_saldo_negativo = -500
username = "alex"

while True:
    for i in range(3):
        conta = input("Digite a sua conta: ")
        senha = input("Digite a sua senha: ")
        if conta == conta_corente and senha == senha_usuario:
            print(f"Bem vindo {username}!")
            acesso_permitido = True
            break
        else:
            print("Conta ou senha incoreta")
            acesso_permitido = False
    if not acesso_permitido:
        break

    while True:
        opcao = input("Escolha uma opção:\n" \
        "1- Ver saldo\n" \
        "2- Sacar valor\n" \
        "3- Depositar valor\n" \
        "4- Pagar boleto\n" \
        "5- Alterar senha\n" \
        "6- Sair\n")

        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        elif opcao == 6:
            print("Atendimento finalizado")
            break
        else:
            print("Opção inválida")
        
