from math import factorial

def fatorial(num, mostrar = False):
    if mostrar == 's':
        n = num
        c = n
        f = 1
        print(f"Fatorial: {n}! = ", end="")
        while c > 0:
            print(f"{c}", end="")
            print(" x " if c > 1 else " = ", end="")
            f *= c
            c -= 1
        print(f)
    elif mostrar == 'n':
        n = num
        f = factorial(n)
        print(f"O fatorial de {n} é {f}.")


num = int(input("Insira um numero:"))
mostrar = input("Deseja observar o processo do fatorial [s/n] ?")
fatorial(num, mostrar)

