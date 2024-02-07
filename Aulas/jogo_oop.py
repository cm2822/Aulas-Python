class Jogo:
    def __init__(self, titulo, consola, preco):
        self.titulo = titulo
        self.consola = consola
        self.preco = preco


jogo = Jogo("PalWorld", "PC", "30")

print(jogo.titulo)
print(jogo.preco)
print(jogo.consola)
