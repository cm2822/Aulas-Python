lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
maior_valor3 = 0
soma_coluna_2 = 0

for i in range(0, 3):
    for v in range(0, 3):
        lista[i][v] = int(input("Insira um numero: "))

for i in range(0, 3):
    for v in range(0, 3):
        if lista[i][v] % 2 == 0:
            soma_par += lista[i][v]

        soma_coluna_2 = sum(lista[1])
        maior_valor3 = max(lista[2])

        print(f"[{lista[i][v]}]", end=" ")
    print("")

print(f"{soma_par}")
print(f"{soma_coluna_2}")
print(f"{maior_valor3}")
