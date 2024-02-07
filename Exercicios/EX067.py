
def valida():
    while True:
        num = input("Insira um número")

        if num.isnumeric():
            print("Número inteiro")
            break
        else:
            print("Número não inteiro")


valida()
