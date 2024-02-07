from tabuada import tabuada
from fatorial import factorial
from primo import primo
from par_impar import par_impar
from calculadora import calculadora


opcao = 0

while opcao != 6:
    print("[ 1 ] - Calculadora")
    print("[ 2 ] - Tabuada")
    print("[ 3 ] - Par ou Ímpar")
    print("[ 4 ] - Números Primos")
    print("[ 5 ] - Fatorial")
    print("[ 6 ] - Sair")

    print("Escolha a sua opção")
    opcao = int(input("--> "))

    try:

        if opcao == 1:
            num1 = float(input("Digite o primeiro numero: "))
            num2 = float(input("Digite o segundo numero: "))
            sinal = input("Escola o operando a utilizar --> ")
            calculadora(num1, num2, sinal)

        elif opcao == 2:
            num = int(input("Insira o número que deseja iniciar a tabuada --> "))
            tabuada(num)

        elif opcao == 3:
            num = float(input("Insira um numero --> "))
            par_impar(num)

        elif opcao == 4:
            num = float(input("Insira um numero --> "))
            primo(num)

        elif opcao == 5:
            num = float(input("Insira o número a ser fatorizado: "))
            factorial(num)

    except ValueError:
        print("Por favor insira um valor válido (número)")

    except KeyboardInterrupt:
        print("WOW, ok ... decidiste sair do código...Tudo bem :D")

    except EOFError:
        print("Erro")

    finally:
        print("----------  Código  -----  Terminado  -----------")
