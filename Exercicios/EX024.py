#EX 024

import time

num = int(input("Digite um numero: \n"))


for c in range(2, num):
    time.sleep(2)

    print("Deixe o pc analisar...Ele é meio lento\n")

    time.sleep(2)

    if num == 2 or num == 3:
        print(f"O {num} é considerado um número primo")
        break

    elif num % c == 0:
        print(f"O {num} não é considerado um número primo")
        break

    else:
        print(f"O {num} é considerado um número primo")
        break

