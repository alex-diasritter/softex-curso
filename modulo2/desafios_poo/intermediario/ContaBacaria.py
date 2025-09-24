class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor) -> int:
        if self.saldo > valor:
            self.saldo -= valor
        print(f"Saque no valor de R$50 realizado.")
        print(f"Saldo restante: R${self.saldo}")



conta1 = ContaBancaria("Alex", 200.00)
conta2 = ContaBancaria("Alexandre", 2000.00)

print(conta1.titular, conta1.saldo)
print(conta2.titular, conta2.saldo)

saque = conta1.sacar(50)

