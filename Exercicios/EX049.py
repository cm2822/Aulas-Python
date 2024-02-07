lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for v in range(0, 3):
        lista[i][v] = int(input("Insira um numero: "))

for i in range(0, 3):
    for v in range(0, 3):
        print(f"[{lista[i][v]}]", end=" ")
    print("")