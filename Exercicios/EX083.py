class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self.saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            print("O saldo não pode ser negativo.")
        else:
            self._saldo = novo_saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def levantar(self, valor):
        if valor <= 0:
            print("O valor a ser sacado deve ser maior que zero.")
        elif valor > (self.saldo + self.limite):
            print("Limite de saque excedido.")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")

    @property
    def limite(self):
        return self.limite

    @limite.setter
    def limite(self, novo_limite):
        if novo_limite < 0:
            print("O valor que inseriu sobrepõe o limite da sua conta.")
        else:
            self.limite = novo_limite

    def extrato(self):
        print(f"Conta {self.titular} --> {self.saldo}, Limite --> {self.limite}")


conta_exemplo = ContaBancaria("João", 1000, 500)
conta_exemplo.extrato()

conta_exemplo.depositar(200)
conta_exemplo.extrato()

conta_exemplo.levantar(300)
conta_exemplo.extrato()

conta_exemplo.limite = 600
conta_exemplo.extrato()
