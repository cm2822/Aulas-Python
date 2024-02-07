#EX 015

#Inicio de codigo
print("Seja bem vindo! Vamos criar um programa que lê numeros inteiros e retorna se sao pares ou impares\n")

#Inputs
numero = int(input("Digite um numero: "))

#Ciclo de eventos
if numero % 2 == 0:
    print(f"O numero {numero} e par")

else:
    print(f"O numero {numero} e impar")