"""tupla_um = [2,3,4,5]
tupla_dois = [6, 5, 4, 3]

soma_tuple = tupla_um + tupla_dois

print(soma_tuple)"""
"""
lista = [2, 3, 4, 5]
nova_lista = lista[:]

nova_lista[0] = 7

print(nova_lista)
print(lista)"""

"""lista = [8, 20, 12, 7]

for i, v in enumerate(lista):
    print(f"Posição {i} --> {v}")"""
"""
lista = list()

for cont in range(0, 5):
    num = int(input("Numero: "))
    lista.append(num)
    print(f"{num}")

for valor in lista:
    print(valor, end=" ")

lista.pop(0)"""

"""aluno = list()
aluno.append("Cesar")
aluno.append(31)

turma = list()
turma.append(aluno[])

aluno[0] = "Cesar"
aluno[1] = 30

print(aluno)
print(turma)"""
"""
turma = list()
aluno = list()

for c in range(0, 3):
    aluno.append(input("Insira o nome do aluno: "))
    aluno.append(int(input("Insira a idade: ")))
    turma.append(aluno[:])
    aluno.clear()

print(f"{aluno}")
print(f"{turma}")

for i, a in enumerate(turma):
    print(f"{aluno[0]}tem {aluno[1]}")

for i in range(0, len(turma)):
    for aluno in range(0, len(turma[0])):
        print(f"{i+1}º --> {turma[i][aluno]}")
      """

