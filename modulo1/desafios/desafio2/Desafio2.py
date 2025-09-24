registros_acessos = []
acessoUsersTrue = set()
tempoTotal = 0

parar = False
while not parar:
    user = input("Digite o nome de usuário (ou 'parar' para sair): ")
    if user.lower() == "parar":
        break

    status = input("Status da sessão:\n1 - Sucesso\n2 Falha\nOpção: ")
    if status == "1":
        status = True
    else:
        status = False

    tempo = input("Digite a duração da sessão em minutos: ")
    if status == True:
        registros_acessos.append((user, status, tempo))
        acessoUsersTrue.add(user)
        tempoTotal += int(tempo)
    
print(f"Registro de acessos: {registros_acessos}\n")
print(f"Usuários com acesso bem-sucedido: {acessoUsersTrue}")
print(f"Tempo total sessões bem sucedidas: {tempoTotal} minutos")



