# Ex 028 3 perguntas v/f


import time

resposta_correta = ['V', 'V', 'F']
perguntas = 0
print("Bem vindo a um quiz de perguntas. Se acertares as 3 ganhas 20.000 euros. \n")

nome = str(input("Primeiro, diz me, como te chamas: "))
time.sleep(2)

print(f"Certo {nome}, vamos começar as perguntas: ")
time.sleep(2)

pergunta1 = str(input("Lisboa é capital de Portugal.\n"
                      "V\n"
                      "F\n"
                      "Não responder\n"))
resposta1 = input("---> ").strip().upper()
time.sleep(2)
print("Muito bem...Vamos continuar...")

while resposta1 != 'VF':
    print("Insere um V ou F")
    resposta1 = input("---> ").strip().upper()

if resposta1 == 'V':
    print("Está correto")
else:
    print("Está errado")

pergunta2 = str(input("O ser humano é feito de 70% água.\n"
                      "V\n"
                      "F\n"
                      "Não responder\n"))
resposta2 = input("---> ").strip().upper()
time.sleep(2)

print("Muito bem...Vamos continuar...")

while resposta2 != 'VF':
    print("Insere um V ou F")
    resposta2 = input("---> ").strip().upper()

if resposta2 == 'V':
    print("Está correto")
else:
    print("Está errado")

print("Vamos agora para a última")

pergunta3 = str(input("O ser humano precisa de 8 horas de sono.\n"
                      "V\n"
                      "F\n"
                      "Não responder\n"))
resposta3 = input("---> ").strip().upper()
time.sleep(2)

while resposta1 != 'VF':
    print("Insere um V ou F")
    resposta1 = input("---> ").strip().upper()

if resposta1 == 'V':
    print("Está correto")
else:
    print("Está errado")

print("E agora...")
time.sleep(2)
if pergunta1 != resposta1 or pergunta2 != resposta2 or pergunta3 != resposta3:
    print("Tentaste!")

else:
    print("Acabas de ganhar 20.000 euros!")

