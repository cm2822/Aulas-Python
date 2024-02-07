#criar conta bancaria
#identidade, titular, saldo, limite
#levantar dinheiro, depositar e extrato bancario

class Conta:
    def __init__(self, identidade, titular, saldo, limite):
        self.identidade = identidade
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def levantar(self, valor):
        if valor > self.limite:
            print(f"Limite diário : 400")
        else:
            if self.saldo > valor:
                self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def extrato(self):
        print(f"Conta {self.identidade} --> {self.saldo}$")


