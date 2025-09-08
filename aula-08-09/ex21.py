contatos = {}

while True:

    print("\n1 - Add Contato\n" \
    "2 - Buscar Contato\n" \
    "3 - Sair\n")

    n = input("Opção: ")

    if n == "3":
        break
    elif n == "1":
        nome = input("Nome do contato: ")
        numero = input("Número: ")
        contatos[nome] = numero
    elif n == "2":
        nomeBuscado = input("\nNome do contato: ")
        r = nomeBuscado in contatos
        if r:
            print(f"\nContato: {nomeBuscado}, encontrado.")
            print(f"Número: {contatos[nomeBuscado]}")
        else:
            print("Contato não encontrado.")