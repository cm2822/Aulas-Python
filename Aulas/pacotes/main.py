import header
from matematica import calculadora


header.header("Calculadora")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
sinal = input(f'Digite o seu operador [+ - * /] -->').strip().lower()

print(f"{num1} {sinal} {num2} = {calculadora(num1, num2, sinal)}")
