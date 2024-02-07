class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_livro(self):
        print(f"O livro com o titulo {self.titulo} foi escrito pelo autor(a) {self.autor}")

    print(mostrar_livro())

