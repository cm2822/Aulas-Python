import time

lista = list()

#adicionar os numeros inseridos á lista, contar o seu menor e maior numero
for cont in range(0, 5):
    num = int(input("Insira um numero: "))
    lista.append(num)
    menor = min(lista)
    maior = max(lista)
    time.sleep(1)
    print(f"O {num} foi inserido")

#enumerar a sua posição conforme a sua distribuição  a lista
for i, v in enumerate(lista):
    time.sleep(2)
    print(f"Posição {i} --> {v}")

#inputs
time.sleep(2)
print(f"O maior numero é: {maior}")
time.sleep(2)
print(f"O menor numero é: {menor}")
