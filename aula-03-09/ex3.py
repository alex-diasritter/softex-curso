acessos = [("Pedro", "sucesso"), ("Maria", "sucesso"), ("Ana", "falha"), ("Pedro", "falha"), ("Ana", "falha")]

sucesso = set()
falha = set()

for nome, login in acessos:
    if "sucesso" in login:
        sucesso.add(nome)
    else:
        if not nome in sucesso:
            falha.add(nome)

print(sucesso)
print(falha)