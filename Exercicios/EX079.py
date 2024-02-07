from typing import Any


class ContaBancaria:
    def __init__(self, titular, saldo, limite, nib):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.nib = nib

    def get_nib(self):
        return self.nib

    def set_nib(self, nib):
        if len(str(nib)) != 8:
            print("O NIB deve ter 8 dígitos.")
        self.nib = nib

    def get_titular(self):
        return self.titular
    
    def set_titular(self, titular):
        return self.titular 
    
    def get_saldo(self):
        return self.saldo   
    
    def set_saldo(self, saldo):
        if saldo <0:
            print("O saldo não pode ser negativo")
        self.saldo = saldo

    def get_limite(self):
        return self.limite
    
    def set_limite(self, limite):
        if limite < 0:
            print("O limite da conta bancária não pode ser negativo.")
        self.limite = limite

    def levantar(self, valor):
        if valor > self.limite + self.saldo:
            print("Saldo insuficiente")
        else:
            if self.saldo > valor:
                self.saldo -= valor

    def depositar(self, valor):
        if valor < 0:
            print("O valor do depósito não pode ser negativo")
        self.saldo += valor

    def extrato(self):
        print(f"Conta {self.titular} --> {self.saldo}")

conta = ContaBancaria(12345678, "João da Silva")
print(conta.get_nib()) 
print(conta.get_titular()) 
print(conta.get_saldo())
print(conta.get_limite()) 

conta.set_saldo(1000)
print(conta.get_saldo()) 

conta.sacar(500)
print(conta.get_saldo())

conta.depositar(200)
print(conta.get_saldo())


