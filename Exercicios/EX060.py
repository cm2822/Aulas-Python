from time import sleep


def introducao(msg):
    print("-------------------------------------")
    print(f"{msg}")
    print("-------------------------------------")


def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    sleep(1)
    cont = inicio

    if inicio < fim:
        while cont <= fim:
            print(f"{cont}", end=" ")
            cont += passo
            sleep(0.3)
        print("FIM")
    else:
        while cont > fim:
            print(f"{cont}", end=" ")
            cont -= passo
            sleep(0.3)
        print("FIM")


introducao("Contagem de números")
inicio = int(input("Insira o primeiro numero: "))
fim = int(input("Insira o ultimo numero: "))
passo = int(input("Insira o passo a dar: "))
contagem(inicio, fim, passo)
