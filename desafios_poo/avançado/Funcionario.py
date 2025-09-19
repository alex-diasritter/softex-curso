class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario
        self.percentual_bonus = 1.10

    def aplicar_bonus(self) -> None:
        print(f'Salário antes do bonus: R${self.salario}')
        print(f'Salário depois do bonus: R${self.salario * self.percentual_bonus:0.2f}')

funcionario = Funcionario('Alex', 1500.00)
funcionario.aplicar_bonus()