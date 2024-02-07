# EX 036 Jogo do Par ou Impar e contar o número de vezes que o jogador ganhou

# importações e variáveis
import random, time

tentativas = 0
opcao = 0
# prints
print("Jogo do Par ou Ímpar")
time.sleep(2)


def resultado(numero):
    return numero % 2 == 0


while opcao != 3:
    num = random.randint(0, 33)
    print(f"Este número é par ou impar: {num}")
    print("[ 1 ] - Par")
    print("[ 2 ] - Impar")
    print("[ 3 ] - Sair")

    opcao = int(input("Insira a opcao (1 . 2 . 3) --> "))

    if opcao == 1 or opcao == 2:
        if (resultado(num) and opcao == 1) or (not resultado(num) and opcao == 2):
            print("Parabéns, acertou!")
            tentativas += 1
        else:
            time.sleep(1)
            print(f"Após {tentativas} vitórias consecutivas perdeu.")
            break
    else:
        print("Por favor, mete a opção correta.")
time.sleep(2)
