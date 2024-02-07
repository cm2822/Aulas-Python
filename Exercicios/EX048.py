lista = list()
par = list()
impar = list()

for c in range(0, 10):
    num = int(input("Insira um numero: "))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(sorted(lista))
print(sorted(par))
print(sorted(impar))