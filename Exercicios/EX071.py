def divisao(a, b):
    div = a / b
    print(f"A divisão de {a} por {b} é {div:.1f}")


try:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print(divisao(num1, num2))

except ValueError:
    print("Utilizador por favor insira um numero")

except EOFError:
    print("O utilizador não inseriu qualquer dado")

except ZeroDivisionError:
    print("Erro. Divisão por zero é impossivel")

except KeyboardInterrupt:
    print("Codigo parado inesperadamante")

else:
    print("A divisão é possível")

finally:
    print("Terminou")
