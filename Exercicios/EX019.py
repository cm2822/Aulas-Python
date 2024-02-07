
#Ex 019
import random , time

print("---/---/---/---/")
print(" RANDOM NUMBERS")
print("---/---/---/---/")
n = random.randint(0,7)

num_util = int(input("Escreva um numero de [ 0 -- 7 ]: "))

time.sleep(1)

print("Analisar se os numeros coincidem...")

time.sleep(1)
print("E agora o momento que mais esperava...")

if num_util == n:
    time.sleep(2)
    print(f"O numero que o computador foi buscar foi {n}\n")
    time.sleep(1)
    print(f"O numero que inseriu é {num_util} . Coincide com o numero do computador. Acaba de ganhar 2 milhoes")

else:
    time.sleep(2)
    print(f"O numero que o computador acaba de pensar e {n}\n")
    time.sleep(1)
    print(f"O numero que inseriu é {num_util} . Nao coincide com o numero do computador! Pouca sorte")
