def divisao(a, b):
    div = a / b
    print(f"A divisão de {a} por {b} é {div}")


try:
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    print(divisao(num1, num2))

except ValueError as v:
    print("Utilizador por favor insira um numero")

except EOFError:
    print("Erro")
    
except Exception as e:
    """ZeroDivisionError print("Erro. Divisão por zero é impossivel")"""
    print(f"Não foi possível realizar a divisão devido a este erro --> {e.__class__}")

except KeyboardInterrupt:
    print("Codigo parado inesperadamante")

else:
    print("A divisão é possível")

finally:
    print("Terminou")