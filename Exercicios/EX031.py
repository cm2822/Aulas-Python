
# Ex 031 fatorial
"""
print("---/---/---/---/")
print(" FATORIAL ")
print("---/---/---/---/")

print("Olá, vamos descobrir o fatorial de um número")
num = int(input("Por favor insere o número: "))

resultado = 1
fatorial = 1
while fatorial <= num:
    resultado *= fatorial
    fatorial += 1
    print(f"O fatorial de {num} é {resultado}")
    
                    OU
"""
"""
num = int(input("Insira um numero:"))

for i in range(1, num):
    fatorial = (i*num)
    num = fatorial
    print(f"O fatorial é {fatorial}")
"""

"""                OU
from math import factorial
n = int(input("Insira o número a ser fatorizado: "))
f = factorial(n)
print(f"O fatorial de {n} é {f}.")"""

"""n = int(input("Insira o número a ser fatorizado: "))
c = n
f = 1
print(f"Fatorial: {n}! = ", end="")
while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f"{f}")"""