# Dicionário para armazenar os contatos (em memória)
agenda = {}

def adicionar_contato():
    """Adiciona um novo contato à agenda."""
    print("\n--- Adicionar Contato ---")
    nome = input("Digite o nome: ").strip() # .strip() remove espaços extras
    
    if not nome:
        print("Erro: O nome não pode ser vazio.")
        return
        
    if nome in agenda:
        print("Erro: Contato com este nome já existe.")
        return

    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    
    agenda[nome] = {"telefone": telefone, "email": email}
    print(f"Contato '{nome}' adicionado com sucesso!")

def remover_contato():
    """Remove um contato da agenda pelo nome."""
    print("\n--- Remover Contato ---")
    nome = input("Digite o nome do contato a ser removido: ").strip()
    
    if nome in agenda:
        del agenda[nome]
        print(f"Contato '{nome}' removido com sucesso!")
    else:
        print("Erro: Contato não encontrado.")

def procurar_contato():
    """Procura e exibe os detalhes de um contato."""
    print("\n--- Procurar Contato ---")
    nome = input("Digite o nome do contato: ").strip()
    
    if nome in agenda:
        contato = agenda[nome]
        print(f"Nome: {nome} | Telefone: {contato['telefone']} | E-mail: {contato['email']}")
    else:
        print("Erro: Contato não encontrado.")

def listar_todos():
    """Lista todos os contatos salvos na agenda."""
    print("\n--- Contatos Salvos ---")
    if not agenda:
        print("Nenhum contato na agenda.")
    else:
        for i, (nome, dados) in enumerate(agenda.items(), 1):
            print(f"{i}. {nome} - {dados['telefone']} - {dados['email']}")

def mostrar_menu():
    """Exibe o menu principal da agenda."""
    print("\n=== AGENDA DE CONTATOS ===")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Procurar contato")
    print("4 - Listar todos")
    print("5 - Sair")

# --- Programa Principal ---
if __name__ == "__main__":
    while True:
        mostrar_menu()
        try:
            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                adicionar_contato()
            elif escolha == 2:
                remover_contato()
            elif escolha == 3:
                procurar_contato()
            elif escolha == 4:
                listar_todos()
            elif escolha == 5:
                print("Saindo da agenda.")
                break
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Erro: Por favor, digite um número válido.")

