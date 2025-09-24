def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """
    Retorna a divisão de dois números.
    Retorna uma mensagem de erro se houver divisão por zero.
    """
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

def mostrar_menu():
    """Exibe o menu da calculadora."""
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

# --- Programa Principal ---
if __name__ == "__main__":
    while True:
        mostrar_menu()
        try:
            escolha = int(input("Escolha a operação: "))

            if escolha == 5:
                print("Saindo da calculadora. Até logo!")
                break
            
            if escolha not in [1, 2, 3, 4]:
                print("Opção inválida! Tente novamente.")
                continue

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == 1:
                resultado = somar(num1, num2)
            elif escolha == 2:
                resultado = subtrair(num1, num2)
            elif escolha == 3:
                resultado = multiplicar(num1, num2)
            elif escolha == 4:
                resultado = dividir(num1, num2)
            
            print(f"Resultado: {resultado}")

        except ValueError:
            print("Erro: Por favor, digite apenas números.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

