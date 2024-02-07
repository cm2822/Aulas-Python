import funciones
from funciones import soma

# programa principal
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

print(f"{num1} + {num2} = {funciones.soma(num1, num2)}")
