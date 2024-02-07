lista = list()

#faz a contagem de numeros
for count in range(0, 5):
    num = int(input("Insira um numero:"))
    index = 0
# enquanto o index for menor que o elemento dentro da lista e o numero for maior que o numero dentro do indice
#ele insere como o primeiro da lista
    while index < len(lista) and num > lista[index]:
        index +=1
    lista.insert(index, num)
    print(f"O {num} foi inserido.")

#Apresentação final
print(f"Ordem crescente: {lista}")