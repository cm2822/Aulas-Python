import time


def aluno(nome, notas):
    media = sum(notas) / len(notas)
    time.sleep(3)
    print("A fazer o cálculo...")
    time.sleep(0.2)
    print(f"Nome do aluno -> {nome}")
    time.sleep(0.2)
    if media >= 9.5:
        print(f"A media no final e de {media}. Passou!\n")
    elif 8 < media <= 9.5:
        print(f"A media no final e de {media}. Parece que vamos ter de recuperar a nota de alguma forma \n")
    else:
        print(f"A media no final e de {media}. Parece que reprovou :(\n")


nome = input("Insira o nome do aluno: ")
notas = []
for c in range(1, 6):
    nota = float(input(f"Insira a nota de cada {c}--> "))
    notas.append(nota)
    aluno(nome, notas)


