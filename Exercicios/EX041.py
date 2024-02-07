valores = tuple(int(input(f"Insira o {i + 1}º valor: "))for i in range(4))

numero_7 = valores.count(7)

rank_num_5 = valores.index(5) + 1 if 5 in valores else "Número não encontrado"

num_par = [valor for valor in valores if valor % 2 == 0]

print(f"Quantidade de 7's: {numero_7}")
print(f"Posição do numero 5: {rank_num_5}")
print(f"Numeros pares: {num_par}" if num_par else "Não existe")
