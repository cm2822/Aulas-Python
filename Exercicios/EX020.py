#EX 020

import random, time

time.sleep(2)

print("---/---/---/---/---/")
print(" PEDRA PAPEL TESOURA")
print("---/---/---/---/---/")

time.sleep(2)

print("Bem vindo ao jogo de pedra papel tesoura contra o CPU!")

time.sleep(2)

nome = str(input("Insere o teu nome: "))

meu = str(input("Escolhe uma jogada (escreve a palavra): "))
mao = meu.lower().capitalize()

if meu == 'pedra' or meu == 'papel' or meu == 'tesoura':
    escolha = ["Pedra", "Papel", "Tesoura"]

    cescolha = random.choice(escolha)

    time.sleep(2)

    print("O pc analisa a jogada...\n ")

    if cescolha == mao:
        time.sleep(2)

        print(f"O computador jogou {cescolha}, e o {nome} jogou {mao}\n")
        print("Empate")

    elif cescolha == 'Pedra' and mao == 'Tesoura':
        time.sleep(2)

        print(f"O computador jogou {cescolha}, e o {nome} jogou {mao}\n")
        print("O computador ganhou \n")

    elif cescolha == 'Papel' and mao == 'Pedra':
        time.sleep(2)

        print(f"O computador jogou {cescolha}, e o {nome} jogou {mao}\n")
        print("O computador ganhou \n")

    else:
        time.sleep(2)

        print(f"Muitos parabéns {nome}")
        print(f"O computador jogou {cescolha}, e o {nome} jogou {mao}\n")
else:
    print("Epa não brinques com a minha cara e escolhe a jogada certa, PAH \n")

