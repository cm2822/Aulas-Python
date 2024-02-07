import time
def calculadora(num):
    for c in range(0, 10):
        time.sleep(0.5)
        print(num, "  x  ", c + 1, " = ", num * (c + 1))


opcao = 0
while opcao != 2:
    print()
    print("[ 1 ] - Começar a tabuada")
    print("[ 2 ] - Sair")

    print("Escolha a sua opcao")
    opcao = int(input("-->"))

    if opcao == 1:
        numeros = int(input("Insira o numero que quer utilizar para fazer a tabuada: \n"))
        calculadora(numeros)
