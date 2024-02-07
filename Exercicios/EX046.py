lista = list()
lista_par = list()
lista_impar = list()

for cont in range(0, 5):
    num = int(input("Insira um numero: "))
    lista.append(num)
    print(f"O {num} foi inserido.")

    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

num_repetido = any(lista.count(num) > 1 for num in set(lista))

if num_repetido:
    print("Insira um numero diferente, este já foi inserido anteriormente.")

print(f"Os numeros inseridos foram: {lista}")
print(f"Os numeros pares são: {lista_par}")
print(f"Os numeros impares são: {lista_impar}")

