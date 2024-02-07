"""#EX 017

#Inputs e Prints
num = int(input("Digite o numero: "))

print("----Conversor----")
print("[1] - Binario")
print("[2] - Octal")
print("[3] - Hexadecimal")
opcao = int(input("Agora escolha a conversao deste numero: "))
#Ciclo de eventos

if opcao == 1:
    print(f"O numero {num} em binario e: {bin(num)[2:]}")
elif opcao == 2:
    print(f"O numero {num} em binario e: {oct(num)[2:]}")

elif opcao == 3:
    print(f"O numero {num} em binario e: {hex(num)[2:]}")
else:
    print("Insira uma opção válida")"""