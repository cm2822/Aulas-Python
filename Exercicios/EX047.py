#Criação do input e a lista
eq = input("Insira a equacao matematica com os parentesis respetivamente: ")
lista = list()

#Validação da existencia de parentesis: se n tiver parentesis, está incorreto
for parentesis in eq:
    if parentesis == '(':
        lista.append(parentesis)
    elif parentesis == ')':
        if not lista:
            result = "Parentesis incorretos"
            break
        lista.pop()
#se tiver parentesis diretos está correto e uma segunda validação se n estiver
else:
    result = "Parentesis corretos" if not lista else "Parentesis incorretos"

print(result)