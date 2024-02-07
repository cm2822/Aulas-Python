# EX 029 - Adivinha 2.0


import random, time

print("---/---/---/---/")
print(" RANDOM NUMBERS")
print("---/---/---/---/")
n = random.randint(0, 7)
tentativas = 1
num_util = int(input("Escreva um numero de [ 0 -- 7 ]: "))

time.sleep(1)

print("Analisar se os numeros coincidem...")

time.sleep(1)

while num_util != n:
    print("Tenta mais uma vez!\n")
    num_util = int(input("Escreva um numero de [ 0 -- 7 ]: "))
    tentativas = tentativas + 1

    if num_util == n:
        time.sleep(2)
        print(f"O numero que o computador foi buscar foi {n}\n")
        time.sleep(1)
        print(f"Após {tentativas} tentativa(s)...\n")
        print(f"O numero que inseriu é {num_util} . Coincide com o numero do computador. Acaba de ganhar 2 milhoes\n")

    else:
        time.sleep(2)
        print(f"O numero que o computador acaba de pensar e {n}\n")
        time.sleep(1)
        print(f"O numero que inseriu é {num_util} . Nao coincide com o numero do computador! Pouca sorte\n")
        break
