# Ex 030 3 numeros soma, mul, div, resto

import time

opcao = 0
soma = 0
mult = 0
div = 0
rest = 0

print("---/---/---/---/")
print(" CALCULADORA ")
print("---/---/---/---/")

time.sleep(2)
print("Bem Vindo á Calculadora")

while opcao != 6:
    print("[ 1 ] - Soma")
    print("[ 2 ] - Multiplicação")
    print("[ 3 ] - Divisão")
    print("[ 4 ] - Resto da Divisão")
    print("[ 5 ] - Comparação de números")
    print("[ 6 ] - Sair")

    print("Qual a sua opção: ")
    opcao = int(input("--->>"))

    if opcao == 1:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        soma = num1 + num2
        print(f"{num1} + {num2} = {soma}")

    elif opcao == 2:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        mult = num1 * num2
        print(f"{num1} * {num2} = {mult}")

    elif opcao == 3:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        div = num1 / num2
        print(f"{num1} / {num2} = {div}")

    elif opcao == 4:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        rest = num1 % num2
        print(f"{num1} + {num2} = {rest}")

    elif opcao == 5:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        if num1 > num2:
            print(f"O {num1} é maior que {num2}")

        elif num1 == num2:
            print(f"O {num1} é igual a {num2}")
        else:
            print(f"O {num2} é maior que {num1}")

    else:
        print("Por favor insira um número")
    break