#EX 033 Numero de tentativas e a soma dos números inseridos

opcao = 0
soma = 0
tentativas = 0

while opcao != 2:
    print("[ 1 ] - Inserir número")
    print("[ 2 ] - Sair")

    print("Qual a sua opção: ")
    opcao = int(input("--->>"))

    if opcao == 1:
        num = int(input("Insira o número: "))
        soma += num
        tentativas += 1

print(f"Inseriu {tentativas} números ")
print(f"A soma destes números é de: {soma}")



