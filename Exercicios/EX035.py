print("TABUADAZINHA RAPIDAAAAAAA")

opcao = 0
while opcao != 2:

    print("[ 1 ] - Começar a tabuada")
    print("[ 2 ] - Sair")

    print("Escolha a sua opcao")
    opcao = int(input("-->"))

    if opcao == 1:
        num = int(input("Insira o numero que quer utilizar para fazer a tabuada: \n"))

        for c in range(0, 10):
            print(num, "  x  ", c + 1, " = ", num * (c + 1))
