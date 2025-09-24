acessos = [("Maria", "sucesso"), ("Ana", "falha"), ("Pedro", "falha"), ("Ana", "falha"), ("Pedro", "sucesso")]

sucesso = set()
falha = set()

for nome, login in acessos:
    if "sucesso" in login:
        sucesso.add(nome)
    else:
        falha.add(nome)

apenasFalha= falha.difference(sucesso)

print("\nUm ou mais sucessos: ")
print(sucesso)
print("\nSomente falhas: ")
print(apenasFalha)
