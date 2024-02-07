#EX 027 menor e maior

maior_idade = 0
menor_idade = 0

for c in range(1, 11):
    idade = int(input(f"Idade da {c} pessoa: \n"))

    if maior_idade < idade:
        maior_idade = idade

    if menor_idade == 0 or idade < menor_idade:
        menor_idade = idade

print(f"A maior idade inserida e: {maior_idade}")
print(f"A menor idade inserida e: {menor_idade}")
