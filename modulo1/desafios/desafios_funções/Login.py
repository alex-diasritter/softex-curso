# Dicionário para armazenar os usuários cadastrados (em memória)
usuarios_cadastrados = {}

def validar_senha(senha):
    """
    Valida a senha para ter no mínimo 8 caracteres,
    com pelo menos uma letra e um número.
    """
    tem_letra = any(c.isalpha() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tamanho_ok = len(senha) >= 8
    
    return tem_letra and tem_numero and tamanho_ok

def cadastrar_usuario():
    """Cadastra um novo usuário no sistema."""
    print("\n--- Cadastro de Usuário ---")
    nome = input("Digite o nome de usuário: ")
    
    if nome in usuarios_cadastrados:
        print("Erro: Este nome de usuário já existe!")
        return

    senha = input("Digite a senha: ")

    if validar_senha(senha):
        usuarios_cadastrados[nome] = senha
        print(f"Usuário '{nome}' cadastrado com sucesso!")
    else:
        print("Erro: A senha deve ter no mínimo 8 caracteres e incluir letras e números!")

def fazer_login():
    """Realiza o login de um usuário."""
    print("\n--- Login ---")
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Verifica se o usuário existe e se a senha está correta
    if nome in usuarios_cadastrados and usuarios_cadastrados[nome] == senha:
        print(f"Login bem-sucedido! Bem-vindo, {nome}.")
    else:
        print("Erro: Usuário ou senha incorretos!")

def mostrar_menu():
    """Exibe o menu principal do sistema."""
    print("\n=== SISTEMA DE LOGIN ===")
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Sair")

# --- Programa Principal ---
if __name__ == "__main__":
    while True:
        mostrar_menu()
        try:
            escolha = int(input("Escolha uma opção: "))

            if escolha == 1:
                cadastrar_usuario()
            elif escolha == 2:
                fazer_login()
            elif escolha == 3:
                print("Saindo do sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")
        
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

