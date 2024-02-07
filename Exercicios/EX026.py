#EX 026 Ano de nascimento
from datetime import date


maior_idade = 0
menor_idade = 0

for c in range(1, 8):
    ano = int(input(f"Ano da {c} pessoa: \n"))
    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade >= 18:
        maior_idade += 1

    else:
        menor_idade += 1

print(f"Aqui tem {maior_idade} maiores de idade.")
print(f"Aqui tem {menor_idade} menores de idade.")
