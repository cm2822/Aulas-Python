#EX 016
#Pequena introducao
print("Boas! Bem-vindo aos calculos de media. Por favor, insere 5 notas de uma disciplina")
disciplina = input("Insere só o nome da disciplina: \n")

#Inputzinhos
nota1 = float(input("Insere a primeira nota: "))
nota2 = float(input("Insere a segunda nota: "))
nota3 = float(input("Insere a terceira nota: "))
nota4 = float(input("Insere a quarta nota: "))
nota5 = float(input("Insere a quinta e ultima nota: "))

#Calculos
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if media >= 9.5:
    print(f"A media no final e de {media}. Passou!")
elif media > 8 and 9.5 :
    print(f"A media no final e de {media}. Parece que vamos ter de recuperar de alguma forma ")
else:
    print(f"A media no final e de {media}. Parece que reprovou :(")