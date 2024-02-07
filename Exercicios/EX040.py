import random

rand_num = tuple(random.randint(0, 100) for c in range(5))

print(f"Números gerados: {rand_num}")

menor_numero = min(rand_num)
maior_numero = max(rand_num)

print(f"Maior numero: {maior_numero}")
print(f"Menor numero: {menor_numero}")

