notas = [("Ana", 9.5), ("João", 8.0), ("Maria", 10.0), ("Pedro", 7.5), ("Ana", 10.0), ("Carlos", 6.5)]

alunosMaiorNota = set()
alunosNotaMenorQueSete = set()
maiorNota = 0.0

for aluno, nota in notas:
    if nota > maiorNota:
        maiorNota = nota

for aluno, nota in notas:
    if nota <= 7.0:
        alunosNotaMenorQueSete.add(aluno)
    elif nota == maiorNota:
        alunosMaiorNota.add(aluno)

print("\nMaior nota: ")
print(maiorNota)

print("\nAlunos nota dez:")
print(alunosMaiorNota)

print("\nNota menor que 7:")
print(alunosNotaMenorQueSete)