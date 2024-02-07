"""#EX001
print("Ola Mundo")

#EX002
print("Bem vindo(a) caro utilizador!")

#EX003 - Exibir a soma
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero:"))

resultado = num1 + num2

print("A sua soma e ", resultado)

#EX004

num = int(input("Digite um numero: "))

ant = num - 1

suc = num + 1

print("O antecessor desse numero e ", ant, "e o seu sucessor e ", suc)"""

"""#EX005

num1 = int(input("Digite um numero:\n"))
num2 = int(input("Digite outro numero:\n"))

#estruturar variáveis e cálculos
soma = num1 + num2
subtracao = num1 - num2
mult = num1 * num2
div = num1 / num2
resto = num1 % num2


print("Soma:\n", soma)
print("Subtracao:\n", subtracao)
print("Multiplicacao:\n", mult)
print("Divisao:\n", div)
print("Resto da divisao:\n", resto)"""

"""#EX006

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

#Finalzin
print("Entao, apos os calculos feitos a tua media e de ", media, "valores")"""

"""#EX007

#Pequena brincadeira com inputs e a criacao de input do ano de nascimento
print("Ola! Hoje vamos experimentar fazer o calculo da tua idade")
anonasc = int(input("Insere apenas o ano de nascimento:\n "))
ano_atual = int(input("Insira o ano atual")

#Inserir a data atual e o calculo da sua idade
idade = ano_atual - anonasc

#Output final
print("Fazendo os calculos a tua idade e", idade)"""

# EX008

"""km_percorridos = float(input("Insira os kms percorridos: "))
dias_alugado = int(input("Insira o numero de dias que alugou o carro:"))

total_kms = km_percorridos * 0.456
total_dias = dias_alugado * 60

total_pagar = total_kms + total_dias

print("O total a pagar pelo aluguer do carro e de", total_pagar)"""

"""#guardar a primeira letra do primeiro nome em maiusculas
primeira_letra = nome[0].lower()

#guardas as letras apos o espaco em minusculas
ultimo_nome = nome [indice-espaco + 1:].lower()

#Formatar o email com as iniciais sem espaco apos o ponto
email = f"{primeira_letra}.{ultimo_nome}.edu@empresa.pt"

#Imprimir resultado
print(f"Nome: {nome}")
print(f"Email: {email}")
"""
"""#EX 13

palavra = "Python"
palavra_invertida = palavra[5] + palavra[4] + palavra[3] + palavra[2] + palavra[1] + palavra[0]
print(palavra_invertida)
#print(palavra[::-1])"""

"""# EX 014

#Inserir a velocidade que o radar apanha
velocidade = int(input("Insere ai a velocidade a que o carro ia: "))

#Utilizar um ciclo de eventos para saber o que fazer caso aconteça diferentes eventos (lol)
if velocidade > 80:
    print("Super multado, esquece, es mauco")
    multa = 100 + 7 * (velocidade - 80)
    print("Tas com uma coima de ", multa, 'toine')

elif velocidade <= 80:
    print("Muito responsavel, continua assim")
"""

"""#EX 015

#Inicio de codigo
print("Seja bem vindo! Vamos criar um programa que lê numeros inteiros e retorna se sao pares ou impares\n")

#Inputs
numero = int(input("Digite um numero: "))

#Ciclo de eventos
if numero % 2 == 0:
    print(f"O numero {numero} e par")

else:
    print(f"O numero {numero} e impar")"""

"""#EX 016
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
    print(f"A media no final e de {media}. Parece que reprovou :(")"""

"""#EX 017

#Inputs e Prints
num = int(input("Digite o numero: "))

print("----Conversor----")
print("[1] - Binario")
print("[2] - Octal")
print("[3] - Hexadecimal")
opcao = int(input("Agora escolha a conversao deste numero: "))
#Ciclo de eventos

if opcao == 1:
    print(f"O numero {num} em binario e: {bin(num)[2:]}")
elif opcao == 2:
    print(f"O numero {num} em binario e: {oct(num)[2:]}")

elif opcao == 3:
    print(f"O numero {num} em binario e: {hex(num)[2:]}")
else:
    print("Insira uma opção válida")"""

"""#EX 018

#Inputs e Prints
print("Este programa serve para fazer a comparação entre números.")
num1 = int(input("Insira um numero"))

num2 = int(input("Insira outro numero"))

if num1 > num2:
    print(f"O {num1} é maior que {num2}")

elif num1 == num2:
    print(f"O {num1} é igual a {num2}")
else:
    print(f"O {num1} é menor que {num2}")
"""

"""#Ex 019
import random , time

print("---/---/---/---/")
print(" RANDOM NUMBERS")
print("---/---/---/---/")
n = random.randint(0,7)

num_util = int(input("Escreva um numero de [ 0 -- 7 ]: "))

time.sleep(1)

print("Analisar se os numeros coincidem...")

time.sleep(1)
print("E agora o momento que mais esperava...")

if num_util == n:
    time.sleep(2)
    print(f"O numero que o computador foi buscar foi {n}\n")
    time.sleep(1)
    print(f"O numero que inseriu é {num_util} . Coincide com o numero do computador. Acaba de ganhar 2 milhoes")

else:
    time.sleep(2)
    print(f"O numero que o computador acaba de pensar e {n}\n")
    time.sleep(1)
    print(f"O numero que inseriu é {num_util} . Nao coincide com o numero do computador! Pouca sorte")
"""

"""#EX 020

import random, time

time.sleep(2)

print("---/---/---/---/---/")
print(" PEDRA PAPEL TESOURA")
print("---/---/---/---/---/")

time.sleep(2)

print("Bem vindo ao jogo de pedra papel tesoura contra o CPU!")

time.sleep(2)

nome = str(input("Insere o teu nome: "))

meu = str(input("Escolhe uma jogada (escreve a palavra): "))
mao = meu.lower().capitalize()

if meu == 'pedra' or meu == 'papel' or meu == 'tesoura':
    escolha = ["Pedra", "Papel", "Tesoura"]

    cescolha = random.choice(escolha)

    time.sleep(2)

    print("O pc analisa a jogada...\n ")

    if cescolha == mao:
        time.sleep(2)

        print(f"O computador jogou {cescolha}, e o {nome} jogou {mao}\n")
        print("Empate")

    elif cescolha == 'Pedra' and mao == 'Tesoura':
        time.sleep(2)

        print(f"O computador jogou {cescolha}, e o {nome} jogou {mao}\n")
        print("O computador ganhou \n")

    elif cescolha == 'Papel' and mao == 'Pedra':
        time.sleep(2)

        print(f"O computador jogou {cescolha}, e o {nome} jogou {mao}\n")
        print("O computador ganhou \n")

    else:
        time.sleep(2)

        print(f"Muitos parabéns {nome}")
        print(f"O computador jogou {cescolha}, e o {nome} jogou {mao}\n")
else:
    print("Epa não brinques com a minha cara e escolhe a jogada certa, PAH \n")
"""

"""num = int(input("Digite um numero")

          for c in range()
          if (num / 1 == 0):
print()

elif (num / num == 0):"""

"""#EX 021
from playsound import playsound
import time
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)


playsound("new-year-fireworks-sound4-180205.mp4")"""

"""#EX 022 i = 0
f = 100
salto = 2

for mj in range(i,f, salto):
    print(mj)

for c in range(i, f):
    if c == 0:
        continue
    elif c % 2 == 0:
        print(c)"""

"""#EX 023

print("TABUADAZINHA RAPIDAAAAAAA")
num = int(input("Insira o numero que quer utilizar para fazer a tabuada: \n"))


for c in range(0,10):
    print(num, "  x  ", c + 1, " = ", num * (c + 1))"""

"""
#EX 024

import time

num = int(input("Digite um numero: \n"))


for c in range(2, num):
    time.sleep(2)

    print("Deixe o pc analisar...Ele é meio lento\n")

    time.sleep(2)

    if num == 2 or num == 3:
        print(f"O {num} é considerado um número primo")
        break

    elif num % c == 0:
        print(f"O {num} não é considerado um número primo")
        break

    else:
        print(f"O {num} é considerado um número primo")
        break

"""

"""# EX 025 Letras em palindromo

frase = input("Insira uma frase: \n").strip().upper()

frase = ("".join(frase.split()))

tam_palavra = int(len(frase))

for pal in range(len(frase)):
    if frase == frase[::-1]:
        print(f"{frase} é um palindromo\n")
        break
    else:
        print(f"{frase} não é um palindromo\n")
    break
"""

"""#EX 026 Ano de nascimento
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
print(f"Aqui tem {menor_idade} menores de idade.")"""

"""#EX 027 menor e maior

maior_idade = 0
menor_idade = 0

for c in range(1, 11):
    idade = int(input(f"Idade da {c} pessoa: \n"))

    if maior_idade < idade:
        maior_idade = idade

    if menor_idade == 0 or idade < menor_idade:
        menor_idade = idade

print(f"A maior idade inserida e: {maior_idade}")
print(f"A menor idade inserida e: {menor_idade}")"""

# Ex 028 3 perguntas v/f

"""resposta_correta = ['V', 'V', 'F']
perguntas = 0
print("Bem vindo a um quiz de perguntas. Se acertares as 3 ganhas 20.000 euros. \n")

nome = str(input("Primeiro, diz me, como te chamas: "))
time.sleep(2)

print(f"Certo {nome}, vamos começar as perguntas: ")
time.sleep(2)

pergunta1 = str(input("Lisboa é capital de Portugal.\n"
                      "V\n"
                      "F\n"
                      "Não responder\n"))
resposta1 = input("---> ").strip().upper()
time.sleep(2)
print("Muito bem...Vamos continuar...")

while resposta1 != 'VF':
    print("Insere um V ou F")
    resposta1 = input("---> ").strip().upper()

if resposta1 == 'V':
    print("Está correto")
else:
    print("Está errado")

pergunta2 = str(input("O ser humano é feito de 70% água.\n"
                      "V\n"
                      "F\n"
                      "Não responder\n"))
resposta2 = input("---> ").strip().upper()
time.sleep(2)

print("Muito bem...Vamos continuar...")

while resposta2 != 'VF':
    print("Insere um V ou F")
    resposta2 = input("---> ").strip().upper()

if resposta2 == 'V':
    print("Está correto")
else:
    print("Está errado")

print("Vamos agora para a última")

pergunta3 = str(input("O ser humano precisa de 8 horas de sono.\n"
                      "V\n"
                      "F\n"
                      "Não responder\n"))
resposta3 = input("---> ").strip().upper()
time.sleep(2)

while resposta1 != 'VF':
    print("Insere um V ou F")
    resposta1 = input("---> ").strip().upper()

if resposta1 == 'V':
    print("Está correto")
else:
    print("Está errado")

print("E agora...")
time.sleep(2)
if pergunta1 != resposta1 or pergunta2 != resposta2 or pergunta3 != resposta3:
    print("Tentaste!")

else:
    print("Acabas de ganhar 20.000 euros!")

"""

# EX 029 - Adivinha 2.0
"""

import random, time

print("---/---/---/---/")
print(" RANDOM NUMBERS")
print("---/---/---/---/")
n = random.randint(0, 7)
tentativas = 1
num_util = int(input("Escreva um numero de [ 0 -- 7 ]: "))

time.sleep(1)

print("Analisar se os numeros coincidem...")

time.sleep(1)

while num_util != n:
    print("Tenta mais uma vez!\n")
    num_util = int(input("Escreva um numero de [ 0 -- 7 ]: "))
    tentativas = tentativas + 1

    if num_util == n:
        time.sleep(2)
        print(f"O numero que o computador foi buscar foi {n}\n")
        time.sleep(1)
        print(f"Após {tentativas} tentativa(s)...\n")
        print(f"O numero que inseriu é {num_util} . Coincide com o numero do computador. Acaba de ganhar 2 milhoes\n")

    else:
        time.sleep(2)
        print(f"O numero que o computador acaba de pensar e {n}\n")
        time.sleep(1)
        print(f"O numero que inseriu é {num_util} . Nao coincide com o numero do computador! Pouca sorte\n")
        break
"""
"""
# Ex 030 3 numeros soma, mul, div, resto

import time

opcao = 0
soma = 0
mult = 0
div = 0
rest = 0

print("---/---/---/---/")
print(" CALCULADORA ")
print("---/---/---/---/")

time.sleep(2)
print("Bem Vindo á Calculadora")

while opcao != 6:
    print("[ 1 ] - Soma")
    print("[ 2 ] - Multiplicação")
    print("[ 3 ] - Divisão")
    print("[ 4 ] - Resto da Divisão")
    print("[ 5 ] - Comparação de números")
    print("[ 6 ] - Sair")

    print("Qual a sua opção: ")
    opcao = int(input("--->>"))

    if opcao == 1:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        soma = num1 + num2
        print(f"{num1} + {num2} = {soma}")

    elif opcao == 2:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        mult = num1 * num2
        print(f"{num1} * {num2} = {mult}")

    elif opcao == 3:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        div = num1 / num2
        print(f"{num1} / {num2} = {div}")

    elif opcao == 4:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        rest = num1 % num2
        print(f"{num1} + {num2} = {rest}")

    elif opcao == 5:
        num1 = int(input("Insira o primeiro número: "))
        num2 = int(input("Insira o segundo número: "))
        if num1 > num2:
            print(f"O {num1} é maior que {num2}")

        elif num1 == num2:
            print(f"O {num1} é igual a {num2}")
        else:
            print(f"O {num2} é maior que {num1}")

    else:
        print("Por favor insira um número")
    break"""

# Ex 031 fatorial
"""
print("---/---/---/---/")
print(" FATORIAL ")
print("---/---/---/---/")

print("Olá, vamos descobrir o fatorial de um número")
num = int(input("Por favor insere o número: "))

resultado = 1
fatorial = 1
while fatorial <= num:
    resultado *= fatorial
    fatorial += 1
    print(f"O fatorial de {num} é {resultado}")
    
                    OU
"""
"""
num = int(input("Insira um numero:"))

for i in range(1, num):
    fatorial = (i*num)
    num = fatorial
    print(f"O fatorial é {fatorial}")
"""

"""                OU
from math import factorial
n = int(input("Insira o número a ser fatorizado: "))
f = factorial(n)
print(f"O fatorial de {n} é {f}.")"""

"""n = int(input("Insira o número a ser fatorizado: "))
c = n
f = 1
print(f"Fatorial: {n}! = ", end="")
while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print(f"{f}")"""

"""# Ex 032 Sequência de Fibonacci

n = 10
num1 = 0
num2 = 1
num_seg = num2
seq = 1

while seq <= n:
    print(num_seg, end=" ")
    seq += 1
    num1, num2 = num2, num_seg
    num_seg = num1 + num2
print()
"""

"""#Ex 033 Medias das notas de várias disciplinas
import time

#Pequena introducao
print("Boas! Bem-vindo aos calculos de media.\n")

opcao = 0

time.sleep(2)
while opcao != 6:
    print("[ 1 ] - Matemática")
    print("[ 2 ] - Português")
    print("[ 3 ] - História")
    print("[ 4 ] - Geografia")
    print("[ 5 ] - Ed. Fisica")
    print("[ 6 ] - Sair")

    print("Qual a sua opção: ")
    opcao = int(input("--->>"))

    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
        nota1 = float(input("Insere a primeira nota: "))
        nota2 = float(input("Insere a segunda nota: "))
        nota3 = float(input("Insere a terceira nota: "))
        nota4 = float(input("Insere a quarta nota: "))
        nota5 = float(input("Insere a quinta e ultima nota: "))

        media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
        time.sleep(3)
        print("\n")
        print("A fazer o cálculo...")
        time.sleep(4)
        if media >= 9.5:
            print(f"A media no final e de {media}. Passou!\n")
        elif media > 8 and 9.5:
            print(f"A media no final e de {media}. Parece que vamos ter de recuperar a nota de alguma forma \n")
        else:
            print(f"A media no final e de {media}. Parece que reprovou :(\n")
        break

"""
