import random
import time

print("-----------|-----------|---------|")
print("-----------|-----------|---------|")
print("-----------|EUROMILHÕES|---------|")
print("-----------|-----------|---------|")
print("-----------|-----------|---------|")

sorteios = []
palpites = int(input("Insira um numero de chaves para o euromilhoes: "))
i = 0
for i in range(0, palpites):

    numeros = random.sample(range(1, 51), 5)
    estrelas = random.sample(range(1, 13), 2)
    sorteio = [numeros, estrelas]
    sorteios.append(sorteio)

time.sleep(2)
print("A inserir as chaves", end="")
time.sleep(0.7)
print(".", end="")
time.sleep(0.7)
print(".", end="")
time.sleep(0.7)
print(".")


for i, sorteio in enumerate(sorteios):
    time.sleep(0.75)
    print(f"Chave {i+1}: Numeros: {sorteio[0]} Estrelas : {sorteio[1]}")
