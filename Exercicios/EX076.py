class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def mostrar_stock(self):
        print(f"O produto {self.nome} tem {self.quantidade} unidades em stock")

    def aumentar_stock(self, valor):
        self.quantidade += valor
        print(f"O produto {self.nome} tem {self.quantidade} unidades em stock")


produto = Produto("Atum", "3500")
