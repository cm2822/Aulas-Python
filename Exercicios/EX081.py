import datetime

class Livro:
    def __init__(self, titulo, autor, anopub):
        self._titulo = titulo.strip()
        self._autor = autor.strip()
        self._anopub = anopub  # Adicione os parênteses para invocar a função

    def __str__(self):
        return (f'---- LIVRO ---- \n'
                f'Titulo --> {self._titulo}\n'
                f'Autor --> {self._autor}\n'
                f'Ano de Publicação --> {self._anopub}\n')

    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        if len(str(titulo)) == 0:
            print("O titulo não foi inserido")
        self._titulo = titulo

    def get_autor(self):
        return self._autor

    def set_autor(self, autor):
        if len(str(autor)) == 0:
            print("O autor não foi inserido")
        self._autor = autor

    def get_anopub(self):
        return self._anopub

    def set_anopub(self, anopub):
        if int(anopub) < 1900 or int(anopub) > datetime.date.today().year:  # Corrigindo a condição
            print("Ano de publicação inválido.")
        else:
            self._anopub = anopub


# Exemplo de uso:
livro_exemplo = Livro("Título do Livro", "Autor do Livro", 2000)
print(livro_exemplo)
