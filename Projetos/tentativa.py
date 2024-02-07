"""
#EX 1 -- Produto

num1 = int(input("Insere um número: "))
num2 = int(input("Insere outro número: "))

produto = num1 * num2

if produto <= 1000:
    print(produto)
else:
    produto = num1 + num2
    print(produto)

"""
"""
#EX 2 -- Numero anterior, seguinte e soma 
num = int(input("Insira um numero"))
seguinte = 0

for number in range(0, 10):
    seguinte = num + number
    print(f"Número inserido {num} , Numero anterior {seguinte}", "Soma" ,num + number)"""
"""
#Ex 3 -- Área de um circulo
import math

def calcular_area_circulo(raio):
    return math.pi * (raio * raio)

raio = float(input("Insira o raio do círculo: "))

area = calcular_area_circulo(raio)

print(f"A área do retângulo é {area}")"""
"""
import math


def volume_da_esfera(raio):
    return 4 / 3 * math.pi * raio ** 3

raio = float(input("Insira o raio da esfera: "))

volume = volume_da_esfera(raio)

print(f"O raio da esfera é de {raio} logo o seu volume é de {volume}")"""

"""
#Ex 4 Write a Python program to calculate the difference between a given number and 17.
# If the number is greater than 17, return twice the absolute difference.
import time

num = float(input("Insira um número: "))

diff = num - 17
if num > 17:
    seg_dif = diff - 17
    time.sleep(2)
    print(f"O número {num} é maior que 17 logo o dobro da sua diferença é de {seg_dif}")
else:
    time.sleep(2)
    print(f"A diferença entre o {num} e 17 é de {diff}.")

"""

"""# Ex 5 Write a Python program to test whether a number is within 100 of 1000 or 2000.
import time


cem = 100
mil = 1000
dois_mil = 2000
num = float(input("Insira um número: "))


while num < cem:
    time.sleep(2)
    print("Este número não está dentro dos parâmetros do exercício. Tenta novamente \n")
    num = float(input("Insira um número: "))


if cem <= num <= mil:
    print(f"Este número está entre {cem} e {mil}")

elif mil <= num <= dois_mil:
    print(f"Este número está entre {mil} e {dois_mil}")
else:
    print("Este número não está dentro dos parametros")"""

# Write a Python program to calculate the sum of three given numbers.
# If the values are equal, return three times their sum.
"""import time

num1 = float(input("Insira o 1º número: "))
time.sleep(1)
num2 = float(input("Insira o 2º número: "))
time.sleep(1)
num3 = float(input("Insira o 3º número: "))
time.sleep(1)

soma1 = num1 + num2
soma2 = num2 + num3


if soma1 == soma2:
    time.sleep(2)
    print(f"Primeira soma : {num1} + {num2} = {soma1}")
    time.sleep(2)
    print(f"Segunda soma : {num2} + {num3} = {soma2}")
    time.sleep(2)
    print(f"As somas deram resultados iguais logo teremos de triplicar a sua soma")
    soma3 = 3 * soma1
    time.sleep(1)
    print(f"3 * {soma1} = {soma3}")

else:
    print(f"Primeira soma: ")
    time.sleep(2)
    print(f"{num1} + {num2} = {soma1}")

    print(f"Segunda Soma: ")
    time.sleep(2)
    print(f"{num2} + {num3} = {soma2}")"""

# Write a Python program that will accept the base and height of a triangle and compute its area.

"""print("-/-/-/-/-/-/-/-/-/-/")
print("AREA DE UM TRIÂNGULO")
print("-/-/-/-/-/-/-/-/-/-/")

def area_do_triangulo(base, altura):
    return (base * altura) / 2

base = float(input("Insira o comprimento da base do triângulo: "))
altura = float(input("Insira o comprimento da altura do triângulo: "))

area = area_do_triangulo(base, altura)

print(f"A área do triângulo é de {area}")"""

# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""OPCAO 1
Importação de funções através de math
import math
print("-/-/-/-/-/-/-/-/-/-/")
print("Maior Divisor Comum ")
print("-/-/-/-/-/-/-/-/-/-/")
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

gcd = math.gcd(num1, num2)

print(f"O maior divisor comum entre {num1} e {num2} é : {gcd} ")"""

"""OPCAO 2
print("-/-/-/-/-/-/-/-/-/-/")
print("Maior Divisor Comum ")
print("-/-/-/-/-/-/-/-/-/-/")
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
gdc = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        gdc = i
        break
print(f"O maior divisor comum entre {num1} e {num2} é : {gdc} ")"""

# Write a Python program to find the least common multiple (LCM) of two positive integers.
"""OPCAO 1
Importação de funções através de math
import math
print("-/-/-/-/-/-/-/-/-/-/")
print("Mínimo Múltiplo Comum")
print("-/-/-/-/-/-/-/-/-/-/")
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

lcm = math.lcm(num1, num2)

print(f"O mínimo múltiplo comum entre {num1} e {num2} é : {lcm} ")"""

"""OPCAO 2
print("-/-/-/-/-/-/-/-/-/-/")
print("Mínimo Múltiplo Comum")
print("-/-/-/-/-/-/-/-/-/-/")
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
mmc = 1
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        mmc = i
        break
print(f"O mínimo múltiplo comum entre {num1} e {num2} é : {mmc} ")
"""

#------------------------------------------------------------------    Lists    ----------------------------------------------------------------------------------------------------------

# 1 - Reverse a list in Python
"""
lista = [100, 200, 300, 400, 500]

lista.sort(reverse=True)

print(lista)"""

# 2 - Concanenar duas listas
"""
lista1 = ["O", "nome ", "César "]
lista2 = [" meu ", "é ", "Maia"]
lista3 = [i + j for i, j in zip(lista1, lista2)]
print(lista3)
"""

# 3 - Inserir qualquer número e retornar o seu quadrado
"""
lista = list()
result = []
for c in range(0, 8):
    num = int(input("Insira o numero: "))
    result.append(num * num)


print(f"Os números inseridos foram {lista} e o seu quadrado é {result}")
"""

# 4 - Concanenar duas listas 2.0
"""
lista1 = ["Olá ", "tome "]
lista2 = ["Querido/a ", "Senhor(a) "]
lista3 = [i + j for i in lista1 for j in lista2]
print(lista3)
"""
# 5 - Itenerar as listas simultaneamente
"""lista1 = [10, 20, 30, 40]
lista2 = [100, 200, 300, 400]
for i, j in zip(lista1, lista2[::-1]):
    print(i, j)"""

# 6. Remove empty strings from the list of strings
"""
lista = ["Mike", "", "Emma", "Kelly", "", "Brad"]

result = list(filter(None, lista))
print(result)
"""
# 7: Add new item to list after a specified item
"""
lista1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

num = int(input("Insira um numero:"))
lista1[2][2].append(num)
print(lista1)
"""
# 8: Extend nested list by adding the sublist
"""
lista = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_lista = ["h", "i", "j"]

lista[2][1][2].extend(sub_lista)
print(lista)
"""
# 1. Write a Python program to sum all the items in a list.
"""
lista1 = list()
resultado = 0
for c in range(0, 4):
    num1 = int(input("Insira um número: "))
    lista1.append(num1)
    resultado = sum(lista1)
    
print(resultado)
"""
# 2. Write a Python program to multiply all the items in a list.

"""
lista1 = list()
resultado = 1
for c in range(0, 4):
    num = int(input("Insira um numero: "))
    lista1.append(num)
    for num in lista1:
        resultado *= num

print(resultado)
"""

# 3. Write a Python program to get the largest number from a list.

"""
lista = list()
for c in range(0, 4):
    num = int(input("Insira um numero: "))
    lista.append(num)

maior = max(lista)
print(maior)
"""

# 4. Write a Python program to get the smallest number from a list.

"""
lista = list()
for c in range(0, 4):
    num = int(input("Insira um numero: "))
    lista.append(num)

menor = min(lista)
print(menor)
"""

# 5. Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

"""
lista = list()
ctr = 0
for c in range(0, 4):
    palavra = input("Insira um numero: ")
    lista.append(palavra)
    if len(palavra) > 1 and palavra[0] == palavra[-1]:
        ctr += 1

print(lista)
print(ctr)
"""

# 6. Write a Python program to get a list, sorted in increasing order by the last element
# in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

"""
lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lista_sort = sorted(lista, key=lambda x: x[-1])
print(lista_sort)
"""

# 7. Write a Python program to remove duplicates from a list.

"""
lista = list()

for c in range(0, 2):
    palavra = input("Insira algumas palavras: ")
    lista.append(palavra)

result = list(filter(None, set(lista)))
print(result)
"""

# 8. Write a Python program to check if a list is empty or not.

"""
lista = list()

for c in range(0, 4):
    palavra = input("Insira algumas palavras:")
    lista.append(palavra)
result = list(filter(None, lista))
print(result)
"""

# 9. Write a Python program to clone or copy a list.

"""
lista = list()

for c in range(0, 4):
    palavra = int(input("Insira algumas numeros: "))
    lista.append(palavra)

nova_lista = lista.copy()
print(nova_lista)
"""

# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

"""
lista = list()

for c in range(0,4):
    palavra = input("Palavras: ")
    lista.append(palavra)
lista = sorted(lista, key=len)
print(f"Palavra inserida com sucesso. Esta é a lista {lista}")

"""
# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

# 15. Write a Python program to shuffle and print a specified list.

# 16. Write a Python program to generate and print a list of the first and last 5 elements
# where the values are square numbers between 1 and 30 (both included).

# 17. Write a Python program to check if each number is prime in a given list of numbers.
# Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
