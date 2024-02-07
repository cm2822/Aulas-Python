lista_pessoas = []
opcao = ""
mulheres_registadas = 0
total_pessoas = 0
homens_idade = 0
media_idades = 0
soma_idades = 0

while opcao != 'n':
    pessoa = {}
    pessoa["nome"] = input("Insira o nome da pessoa --> ")
    pessoa["idade"] = int(input("Insira a sua idade --> "))

    while True:
        pessoa["sexo"] = input("Qual o seu sexo? [m/f] --> ").lower()
        if pessoa["sexo"] in ["m", "f"]:
            break
        else:
            print("Por favor, insere o género correto.")

    lista_pessoas.append(pessoa)
    opcao = input("\nQuer continuar ? [s/n] --> ")

total_pessoas = len(lista_pessoas)

# adicionar as idades
for pessoa in lista_pessoas:
    soma_idades += pessoa["idade"]

# adicionar numero de mulheres
if pessoa["sexo"] == "f":
    mulheres_registadas += 1

# Sexo masculino e maior de idade
if pessoa["sexo"] == "m" and pessoa["idade"] > 17:
    homens_idade += 1

# calculo da media de idades
if total_pessoas > 0:
    media_idades = soma_idades / total_pessoas

#prints
print(f"\nTotal de pessoas registradas: {total_pessoas}")
print(f"Média de idades do grupo: {media_idades:.1f}")
print(f"Total de mulheres registradas: {mulheres_registadas}")
print(f"Total de homens com idade acima da média: {homens_idade}")
