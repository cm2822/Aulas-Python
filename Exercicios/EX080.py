import math

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError("Nome deve ser uma string")
        self.nome = nome
        
    def calcular_media(self):
        if len(self.notas) < 2:
            raise ValueError('Não foram inseridas notas para calcular a média.')
        return sum(self.notas) / len(self.notas)


nome = input("Insira o seu nome --> ")
notas = []

while True:
    nota_str = input("Insira a nota do aluno (ou digite 'fim' para encerrar a entrada): ")
    if nota_str == "fim":
        break
    notas.append(float(nota_str))

if len(notas) < 2:
    raise ValueError("Precisa de no mínimo 2 notas para calcular a média.")

aluno = Aluno(nome, notas)
print(aluno.calcular_media())
