class Produto:
    def __init__(self, nome_produto, quantidade_stock):
        self._nome_produto = nome_produto
        self._quantidade_stock = quantidade_stock

    @property
    def nome_produto(self):
        return self._nome_produto

    @property
    def quantidade_stock(self):
        return self._quantidade_stock

    @quantidade_stock.setter
    def quantidade_stock(self, valor):
        if valor < 0:
            print("A quantidade de stock não pode ser negativo. Por favor insira outro dado.")
        else:
            self._quantidade_stock = valor

    def mostrar_stock(self):
        return f'Quantidade em stock disponível de {self._nome_produto} --> {self._quantidade_stock}'

    def adicionar_stock(self, quantidade):
        if quantidade < 0:
            print("A quantidade a adicionar não pode ser negativa.")
        else:
            self._quantidade_stock = quantidade
            print(f"Foram adicionadas {quantidade} unidades ao stock de {self._nome_produto}")


nome_produto = input("Digite o nome do produto: ")
quantidade_inicial = int(input("Digite a quantidade inicial em stock: "))

produto_exemplo = Produto(nome_produto, quantidade_inicial)
produto_exemplo.mostrar_stock()

quantidade_a_adicionar = int(input("Digite a quantidade a ser adicionada ao stock: "))
produto_exemplo.adicionar_stock(quantidade_a_adicionar)
produto_exemplo.mostrar_stock()

nova_quantidade = int(input("Digite a nova quantidade em stock: "))
produto_exemplo.quantidade_stock = nova_quantidade
produto_exemplo.mostrar_stock()


