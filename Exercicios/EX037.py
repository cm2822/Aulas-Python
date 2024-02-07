"""Ler a idade e o sexo de cada pessoa
Opcao de continuar ou nao
Mostrar quantas pessoas têm mais de 25 anos
Mostrar quantos homens com menos de 17 foram registados
 Mulheres registadas
Menores de idade registados"""

# Importações e variáveis
opcao = 0
maior_25 = 0
menor_17 = 0
n_homens = 0
n_mulheres = 0

while opcao != 2:
    print("[ 1 ] - Inserir dados de um utilizador")
    print("[ 2 ] - Sair")

    print("Escolha a sua opcao")
    opcao = int(input("-->"))

    if opcao == 1:
        nome = input("Insira o seu nome: ")
        idade = int(input("Qual é a sua idade: "))
        sexo = input("Qual o seu sexo (M/F): ")

        print(f"O seu nome é {nome}, tem {idade} anos e é {sexo}\n")

        if sexo == 'M':
            n_homens += 1
        elif sexo == 'F':
            n_mulheres += 1

        if idade > 25:
            maior_25 += 1

        elif idade < 17:
            menor_17 += 1


print(f"Número de homens: {n_homens}")
print(f"Número de mulheres: {n_mulheres}")
print(f"Pessoas com mais de 25 anos: {maior_25}")
print(f"Pessoas com menos de 17 anos: {menor_17}")