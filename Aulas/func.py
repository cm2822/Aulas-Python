"""def cabecalho(msg):
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
    print(msg)
    print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
    print()


cabecalho("Ola Mundo")
cabecalho("Olá turma")
"""


def soma(a, b):
    s = a + b
    print(f"A soma entre {a} e {b} igual a {s}")


def conta_numeros(*num):
    print(f"Inseriu {len(num)} numeros")
    for numeros in num:
        print(f"{numeros}", end="")
        print()


# Principal
print("Função Soma")
soma(5, 5)
soma(32, 15)
soma(4, 4)
print()
print("Função Desempacotar")
conta_numeros(1, 2, 3, 4, 5, 6)
