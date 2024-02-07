"""num = 7


for c in range(0,10):
    print(num, "  x  ", c + 1, " = ", num * (c + 1))
"""
import time

"""i = 1
f = 10
salto = 2

for mj in range(i,f, salto):
    print(mj)
    """
"""
tentativas = 0
mensagem = "Bem-vindo"
password = "password"

for c in range(0, 3):
    entrada = input("Insira a password: ")
    if entrada == password:
        print(mensagem)
        break
    else:
        tentativas = tentativas + 1
        print("Tente novamente.... \n")

    if tentativas == 3:
        print("Utilizador bloqueado!")"""

"""from playsound import playsound
import time
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)


playsound("new-year-fireworks-sound4-180205.mp4")"""

""""#EX 022 i = 0
f = 100
salto = 2

for mj in range(i,f, salto):
    print(mj)

for c in range(i, f):
    if c == 0:
        continue
    elif c % 2 == 0:
        print(c)"""

""""#EX 023

print("TABUADAZINHA RAPIDAAAAAAA")
num = int(input("Insira o numero que quer utilizar para fazer a tabuada: \n"))


for c in range(0,10):
    print(num, "  x  ", c + 1, " = ", num * (c + 1))"""

"""import time

num = int(input("Digite um numero: \n"))


for c in range(2, num):
    time.sleep(2)

    print("Deixe o cota pc analisar...Ele é meio lento\n")

    time.sleep(2)

    if num == 2 or num == 3:
        print(f"O {num} é considerado um número primo")
        break

    elif num % c == 0:
        print(f"O {num} não é considerado um número primo")
        break

    else:
        print(f"O {num} é considerado um número primo")
        break"""

# while

"""
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
"""
"""
opcao = 0

while opcao != 4:
    print("[ 1 ] - Registar pessoas")
    print("[ 2 ] - NUmero de pessoas registadas")
    print("[ 3 ] - Apagar um registo")
    print("[ 4 ] - Sair")

    print("Qual a sua opcao")
    opcao = int(input("--->>"))

    if opcao == 1:
        nome = input("Digite o nome da pessoa: ")
        idade = input("Idade da pessoa: ")
        print(f"{nome} registado com sucesso\n")
    elif opcao == 2:
        print("Há X pessoas reigstadas")
    elif opcao == 3:
        print("Um registo foi apagado")
    elif opcao < 1 or opcao > 4:
        print("Vai dormir")
        break

print("Xau")


"""

"""resposta_correta = ['V', 'V', 'F']
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

"""
