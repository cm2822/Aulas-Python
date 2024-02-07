
def conta_numeros():
    numeros = []
    for c in range(0, 5):
        numero = int(input("Insira um numero: "))
        numeros.append(numero)
    for numero in numeros:
        print(f"{numero}", end=" ")

    maior_num = max(numeros)
    print(f"\nO maior número é: {maior_num}")


conta_numeros()
