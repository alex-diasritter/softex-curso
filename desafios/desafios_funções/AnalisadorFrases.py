def analisar_frase(frase):
    """
    Analisa uma frase para contar palavras, vogais, consoantes e
    verificar se é um palíndromo.
    """
    # Contagem de palavras
    palavras = frase.split()
    num_palavras = len(palavras)

    # Contagem de vogais e consoantes
    vogais = "aeiou"
    num_vogais = 0
    num_consoantes = 0
    for letra in frase.lower():
        if letra.isalpha(): # Verifica se o caractere é uma letra
            if letra in vogais:
                num_vogais += 1
            else:
                num_consoantes += 1

    # Verificação de palíndromo
    # Junta a frase sem espaços e em minúsculas
    frase_junta = "".join(frase.lower().split())
    # Inverte a string
    frase_invertida = frase_junta[::-1]
    eh_palindromo = "Sim" if frase_junta == frase_invertida else "Não"

    # Exibe os resultados
    print("\n--- Resumo da Análise ---")
    print(f"Palavras: {num_palavras}")
    print(f"Vogais: {num_vogais}")
    print(f"Consoantes: {num_consoantes}")
    print(f"É um palíndromo? {eh_palindromo}")


# --- Programa Principal ---
if __name__ == "__main__":
    frase_usuario = input("Digite uma frase para analisar: ")
    analisar_frase(frase_usuario)

