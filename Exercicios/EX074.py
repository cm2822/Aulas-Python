class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


livro = Livro("Ulisses", "Maria de Menezes")

print(livro.titulo)
print(livro.autor)