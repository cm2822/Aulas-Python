lista = list()

#contar os numeros inseridos e adiciona-los á lista
for cont in range(0, 5):
    num = int(input("Insira um numero: "))
    lista.append(num)
    print(f"O {num} foi inserido.")

#ele procura o numero e se estiver a aparecer mais que uma vez ele limpa da lista
num_repetido = any(lista.count(num) > 1 for num in set(lista))

if num_repetido:
    print("Insira um numero diferente, este já foi inserido anteriormente.")

#ordernar a lista de forma decrescente
lista.sort(reverse=True)
print(f"Os numeros que inseriu de forma decrescente são: {lista}")
