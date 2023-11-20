class ContaBancaria:
    def __init__ (self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if self.saldo + valor >= 0:
            self.saldo += valor
            print(f'Deposito de R$:{valor} realizado na conta de: {self.titular}')

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print (f'Saque de R$: {valor} realizado na sua conta:{self.titular}')
        else:
            print(f'Saldo insuficiente na sua conta nome: {self.titular}')


    def ver_saldo (self):
        print(f"Saldo atual R$:{self.saldo} na conta de: {self.titular}")


conta = ContaBancaria("Maicon")

conta.depositar(100)
conta.ver_saldo()

conta.sacar(50)
conta.ver_saldo()

conta.sacar(70)