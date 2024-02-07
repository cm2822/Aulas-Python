#Ex 034 Medias das notas de várias disciplinas
import time

#Pequena introducao
print("Boas! Bem-vindo aos calculos de media.\n")

opcao = 0

time.sleep(2)
while opcao != 6:
    print("[ 1 ] - Matemática")
    print("[ 2 ] - Português")
    print("[ 3 ] - História")
    print("[ 4 ] - Geografia")
    print("[ 5 ] - Ed. Fisica")
    print("[ 6 ] - Sair")

    print("Qual a sua opção: ")
    opcao = int(input("--->>"))

    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
        nota1 = float(input("Insere a primeira nota: "))
        nota2 = float(input("Insere a segunda nota: "))
        nota3 = float(input("Insere a terceira nota: "))
        nota4 = float(input("Insere a quarta nota: "))
        nota5 = float(input("Insere a quinta e ultima nota: "))

        media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
        time.sleep(3)
        print("\n")
        print("A fazer o cálculo...")
        time.sleep(4)
        if media >= 9.5:
            print(f"A media no final e de {media}. Passou!\n")
        elif media > 8 and 9.5:
            print(f"A media no final e de {media}. Parece que vamos ter de recuperar a nota de alguma forma \n")
        else:
            print(f"A media no final e de {media}. Parece que reprovou :(\n")
        break


