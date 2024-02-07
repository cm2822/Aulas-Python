import random
import time
from datetime import date


def ex01():
    print("Ola Mundo")

    # EX002
    print("Bem vindo(a) caro utilizador!")

    # EX003 - Exibir a soma
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero:"))

    resultado = num1 + num2

    print("A sua soma e ", resultado)


def ex02():
    # EX002 - Mensagem de Boas Vindas
    print("---------------------------------")
    print("-----Welcome-to-our-Software-----")
    print("---------------------------------")


def ex03():
    # EX003 - Exibir soma
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    resultado = num1 + num2
    print(num1, "+", num2, "=", resultado, "\n\n")


def ex04():
    num = int(input("Digite um numero: "))
    ant = num - 1
    suc = num + 1
    print("O antecessor desse numero e ", ant, "e o seu sucessor e ", suc)


def ex05():
    num1 = int(input("Digite um numero:\n"))
    num2 = int(input("Digite outro numero:\n"))

    # estruturar variáveis e cálculos
    soma = num1 + num2
    subtracao = num1 - num2
    mult = num1 * num2
    div = num1 / num2
    resto = num1 % num2

    print("Soma:\n", soma)
    print("Subtracao:\n", subtracao)
    print("Multiplicacao:\n", mult)
    print("Divisao:\n", div)
    print("Resto da divisao:\n", resto)


def ex06():
    # Pequena introducao
    print("Boas! Bem-vindo aos calculos de media. Por favor, insere 5 notas de uma disciplina")

    # Inputzinhos
    nota1 = float(input("Insere a primeira nota: "))
    nota2 = float(input("Insere a segunda nota: "))
    nota3 = float(input("Insere a terceira nota: "))
    nota4 = float(input("Insere a quarta nota: "))
    nota5 = float(input("Insere a quinta e ultima nota: "))

    # Calculos
    media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

    # Finalzin
    print("Entao, apos os calculos feitos a tua media e de ", media, "valores")


def ex07():
    # Pequena brincadeira com inputs e a criacao de input do ano de nascimento
    print("Ola! Hoje vamos experimentar fazer o calculo da tua idade")
    anonasc = int(input("Insere apenas o ano de nascimento:\n "))
    ano_atual = int(input("Insira o ano atual"))

    # Inserir a data atual e o calculo da sua idade
    idade = ano_atual - anonasc

    # Output final
    print("Fazendo os calculos a tua idade e", idade)


def ex08():
    # EX008
    km_percorridos = float(input("Insira os kms percorridos: "))
    dias_alugado = int(input("Insira o numero de dias que alugou o carro:"))

    total_kms = km_percorridos * 0.456
    total_dias = dias_alugado * 60

    total_pagar = total_kms + total_dias

    print("O total a pagar pelo aluguer do carro e de", total_pagar)


def ex09():
    # EX009
    # Pedir nome do utilizador
    nome = input("Digite o seu nome completo: ").strip()
    print("Estou a analisar o seu nome...")

    # Mostrar nome em maiúsculas
    print("O seu nome em maiúsculas é {}".format(nome.upper()))

    # Mostrar nome em minúsculas
    print("O seu nome em minúsculas é {}".format(nome.lower()))

    # Mostrar tamanho nome sem espaços
    print("O seu nome tem {} caracteres".format(len(nome) - nome.count(" ")))

    # split
    pnome = nome.split()

    # Mostrar tamanho do primeiro nome
    print("O seu primeiro nome é {} e tem {} caracteres".format(pnome[0], len(pnome[0])))


def ex010():
    # EX 010
    num = int(input("Insira um numero de 0 a 9999:"))

    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

    print("Unidade: {}".format(u))
    print("Dezena: {}".format(d))
    print("Centena: {}".format(c))
    print("Milhar: {}".format(m))


def ex011():
    # EX 011
    frase = input("Escreva uma frase:").upper().strip()

    print("A letra 'A' aparece {} vezes.".format(frase.count("A")))
    print("O primeiro 'A' está na posição: {}.".format(frase.find("A") + 1))
    print("O ultimo 'A' está na posição: {}.".format(frase.rfind("A") + 1))


def ex012():
    # EX 012

    nome = input("Insira o seu nome:").strip()

    snome = nome.split()
    primeiraletra = snome[0][0]

    print("Olá {}, o seu registo está completo.".format(nome))
    print("O seu email é {}.{}.edu@empresa.pt".format(primeiraletra.lower(), snome[1].lower()))


def ex013():
    # EX 13

    palavra = "Python"
    palavra_invertida = palavra[5] + palavra[4] + palavra[3] + palavra[2] + palavra[1] + palavra[0]
    print(palavra_invertida)
    # print(palavra[::-1])


def ex014():
    # EX 014

    # Inserir a velocidade que o radar apanha
    velocidade = int(input("Insere ai a velocidade a que o carro ia: "))

    # Utilizar um ciclo de eventos para saber o que fazer caso aconteça diferentes eventos (lol)
    if velocidade > 80:
        print("Super multado, esquece, es mauco")
        multa = 100 + 7 * (velocidade - 80)
        print("Tas com uma coima de ", multa, 'toine')

    elif velocidade <= 80:
        print("Muito responsavel, continua assim")


def ex015():
    # EX 015

    # Inicio de codigo
    print("Seja bem vindo! Vamos criar um programa que lê numeros inteiros e retorna se sao pares ou impares\n")

    # Inputs
    numero = int(input("Digite um numero: "))

    # Ciclo de eventos
    if numero % 2 == 0:
        print(f"O numero {numero} e par")

    else:
        print(f"O numero {numero} e impar")


def ex016():
    # EX 016
    # Pequena introducao
    print("Boas! Bem-vindo aos calculos de media. Por favor, insere 5 notas de uma disciplina")

    # Inputzinhos
    nota1 = float(input("Insere a primeira nota: "))
    nota2 = float(input("Insere a segunda nota: "))
    nota3 = float(input("Insere a terceira nota: "))
    nota4 = float(input("Insere a quarta nota: "))
    nota5 = float(input("Insere a quinta e ultima nota: "))

    # Calculos
    media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

    if media >= 9.5:
        print(f"A media no final e de {media}. Passou!")
    elif media > 8 and 9.5:
        print(f"A media no final e de {media}. Parece que vamos ter de recuperar de alguma forma ")
    else:
        print(f"A media no final e de {media}. Parece que reprovou :(")


def ex017():
    # Inputs e Prints
    num = int(input("Digite o numero: "))

    print("----Conversor----")
    print("[1] - Binario")
    print("[2] - Octal")
    print("[3] - Hexadecimal")
    opcao = int(input("Agora escolha a conversao deste numero: "))
    # Ciclo de eventos

    if opcao == 1:
        print(f"O numero {num} em binario e: {bin(num)[2:]}")
    elif opcao == 2:
        print(f"O numero {num} em binario e: {oct(num)[2:]}")

    elif opcao == 3:
        print(f"O numero {num} em binario e: {hex(num)[2:]}")
    else:
        print("Insira uma opção válida")


def ex018():
    # EX 018

    # Inputs e Prints
    print("Este programa serve para fazer a comparação entre números.")
    num1 = int(input("Insira um numero"))

    num2 = int(input("Insira outro numero"))

    if num1 > num2:
        print(f"O {num1} é maior que {num2}")

    elif num1 == num2:
        print(f"O {num1} é igual a {num2}")
    else:
        print(f"O {num1} é menor que {num2}")


def ex019():
    # Ex 019

    print("---/---/---/---/")
    print(" RANDOM NUMBERS")
    print("---/---/---/---/")
    n = random.randint(0, 7)

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


def ex020():
    # EX 020

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


def ex021():
    # EX 021
    for c in range(10, 0, -1):
        print(c)
        time.sleep(1)


def ex022():
    # EX 022
    i = 0
    f = 100
    salto = 2

    for mj in range(i, f, salto):
        print(mj)

    for c in range(i, f):
        if c == 0:
            continue
        elif c % 2 == 0:
            print(c)


def ex023():
    # EX 023

    print("TABUADAZINHA RAPIDAAAAAAA")
    num = int(input("Insira o numero que quer utilizar para fazer a tabuada: \n"))

    for c in range(0, 10):
        print(num, "  x  ", c + 1, " = ", num * (c + 1))


def ex024():
    # EX 024

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


def ex025():
    # EX 025 Letras em palindromo

    frase = input("Insira uma frase: \n").strip().upper()

    frase = ("".join(frase.split()))

    for pal in range(len(frase)):
        if frase == frase[::-1]:
            print(f"{frase} é um palindromo\n")
            break
        else:
            print(f"{frase} não é um palindromo\n")
        break


def ex026():
    # EX 026 Ano de nascimento

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


def ex027():
    # EX 027 menor e maior

    maior_idade = 0
    menor_idade = 0

    for c in range(1, 11):
        idade = int(input(f"Idade da {c} pessoa: \n"))

        if maior_idade < idade:
            maior_idade = idade

        if menor_idade == 0 or idade < menor_idade:
            menor_idade = idade

    print(f"A maior idade inserida e: {maior_idade}")
    print(f"A menor idade inserida e: {menor_idade}")


def ex028():
    # Ex 028 3 perguntas v/f

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


def ex029():
    # EX 029 - Adivinha 2.0

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
            print(
                f"O numero que inseriu é {num_util} . Coincide com o numero do computador. Acaba de ganhar 2 milhoes\n")

        else:
            time.sleep(2)
            print(f"O numero que o computador acaba de pensar e {n}\n")
            time.sleep(1)
            print(f"O numero que inseriu é {num_util} . Nao coincide com o numero do computador! Pouca sorte\n")
            break


def ex030():
    # Ex 030 3 numeros soma, mul, div, resto

    opcao = 0

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
        break


def ex031():
    print("---/---/---/---/")
    print(" FATORIAL ")
    print("---/---/---/---/")

    print("Olá, vamos descobrir o fatorial de um número")
    n = int(input("Insira o número a ser fatorizado: "))
    c = n
    f = 1
    print(f"Fatorial: {n}! = ", end="")
    while c > 0:
        print(f"{c}", end="")
        print(" x " if c > 1 else " = ", end="")
        f *= c
        c -= 1
    print(f"{f}")


def ex032():
    # Ex 032 Sequência de Fibonacci

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


def ex033():
    # EX 033 Numero de tentativas e a soma dos números inseridos

    opcao = 0
    soma = 0
    tentativas = 0

    while opcao != 2:
        print("[ 1 ] - Inserir número")
        print("[ 2 ] - Sair")

        print("Qual a sua opção: ")
        opcao = int(input("--->>"))

        if opcao == 1:
            num = int(input("Insira o número: "))
            soma += num
            tentativas += 1

    print(f"Inseriu {tentativas} números ")
    print(f"A soma destes números é de: {soma}")


def ex034():
    # Ex 034 Medias das notas de várias disciplinas

    # Pequena introducao
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


def ex035():
    print("TABUADAZINHA RAPIDAAAAAAA")

    opcao = 0
    while opcao != 2:

        print("[ 1 ] - Começar a tabuada")
        print("[ 2 ] - Sair")

        print("Escolha a sua opcao")
        opcao = int(input("-->"))

        if opcao == 1:
            num = int(input("Insira o numero que quer utilizar para fazer a tabuada: \n"))

            for c in range(0, 10):
                print(num, "  x  ", c + 1, " = ", num * (c + 1))


def ex036():
    # EX 036 Jogo do Par ou Impar e contar o número de vezes que o jogador ganhou

    # importações e variáveis

    tentativas = 0
    opcao = 0
    # prints
    print("Jogo do Par ou Ímpar")
    time.sleep(2)

    def resultado(numero):
        return numero % 2 == 0

    while opcao != 3:
        num = random.randint(0, 33)
        print(f"Este número é par ou impar: {num}")
        print("[ 1 ] - Par")
        print("[ 2 ] - Impar")
        print("[ 3 ] - Sair")

        opcao = int(input("Insira a opcao (1 . 2 . 3) --> "))

        if opcao == 1 or opcao == 2:
            if (resultado(num) and opcao == 1) or (not resultado(num) and opcao == 2):
                print("Parabéns, acertou!")
                tentativas += 1
            else:
                time.sleep(1)
                print(f"Após {tentativas} vitórias consecutivas perdeu.")
                break
        else:
            print("Por favor, mete a opção correta.")
    time.sleep(2)


def ex037():
    """Ler a idade e o sexo de cada pessoa
    Opcao de continuar ou nao
    Mostrar quantas pessoas têm mais de 25 anos
    Mostrar quantos homens com menos de 17 foram registados
     Mulheres registadas
    Menores de idade registados"""

    # Importações e variáveis
    opcao = 0
    maior_25 = 0
    menor_17 = 0
    n_homens = 0
    n_mulheres = 0

    while opcao != 2:
        print("[ 1 ] - Inserir dados de um utilizador")
        print("[ 2 ] - Sair")

        print("Escolha a sua opcao")
        opcao = int(input("-->"))

        if opcao == 1:
            nome = input("Insira o seu nome: ")
            idade = int(input("Qual é a sua idade: "))
            sexo = input("Qual o seu sexo (M/F): ")

            print(f"O seu nome é {nome}, tem {idade} anos e é {sexo}\n")

            if sexo == 'M':
                n_homens += 1
            elif sexo == 'F':
                n_mulheres += 1

            if idade > 25:
                maior_25 += 1

            elif idade < 17:
                menor_17 += 1

    print(f"Número de homens: {n_homens}")
    print(f"Número de mulheres: {n_mulheres}")
    print(f"Pessoas com mais de 25 anos: {maior_25}")
    print(f"Pessoas com menos de 17 anos: {menor_17}")


def ex038():
    num_extenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                   'doze',
                   'treze', 'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte']

    num = int(input("Insira um número de 0 a 20: "))

    if 0 <= num <= 20:
        print(f"O numero {num} em extenso é {num_extenso[num]} ")
    else:
        print("O número que introduziu não está dentro dos parâmetros.")


def ex039():
    rank_fut_esp = ['Real Madrid', 'Girona', 'Barcelona', 'Athletic Bilbao', 'Atlético de Madrid', 'Real Sociedad',
                    'Betis', 'Getafe', 'Valência', 'Las Palmas', 'Rayo Vallecano', 'Osasuna', 'Villarreal', 'Mallorca',
                    'Alavés', 'Sevilla', 'Celta', 'Cádiz', 'Granada', 'Almería']

    cinco = rank_fut_esp[:5]

    fim_quatro = rank_fut_esp[-4:]

    ordem = sorted(rank_fut_esp)

    laspalmas = rank_fut_esp.index("Las Palmas") + 1

    print(f" Os primeiros classificados: {cinco}")
    print(f"Os ultimos: {fim_quatro}")
    print(f"Ordem alfabética: {ordem}")
    print(f"Classificação dos Las Palmas: {laspalmas}")


def ex040():

    rand_num = tuple(random.randint(0, 100) for c in range(5))

    print(f"Números gerados: {rand_num}")

    menor_numero = min(rand_num)
    maior_numero = max(rand_num)

    print(f"Maior numero: {maior_numero}")
    print(f"Menor numero: {menor_numero}")


def ex041():
    valores = tuple(int(input(f"Insira o {i + 1}º valor: ")) for i in range(4))

    numero_7 = valores.count(7)

    rank_num_5 = valores.index(5) + 1 if 5 in valores else "Número não encontrado"

    num_par = [valor for valor in valores if valor % 2 == 0]

    print(f"Quantidade de 7's: {numero_7}")
    print(f"Posição do numero 5: {rank_num_5}")
    print(f"Numeros pares: {num_par}" if num_par else "Não existe")


def ex042():
    jogos_e_precos = (
        ("GTA V", 29.99),
        ("Pokemon", 49.99),
        ("Sonic", 19.99),
        ("Jupiter", 39.99),
        ("Warframe", 59.99)
    )

    print("Jogo ------ Preço")
    for jogo, preco in jogos_e_precos:
        print(f"{jogo} ${preco:.2f}")


def ex043():

    lista = list()

    menor = float('inf')
    maior = float('-inf')

    # adicionar os numeros inseridos á lista, contar o seu menor e maior numero
    for cont in range(0, 5):
        num = int(input("Insira um numero: "))
        lista.append(num)
        menor = min(menor, num)
        maior = max(maior, num)
        time.sleep(1)
        print(f"O {num} foi inserido")

    # enumerar a sua posição conforme a sua distribuição  a lista
    for i, v in enumerate(lista):
        time.sleep(2)
        print(f"Posição {i} --> {v}")

    # inputs
    time.sleep(2)
    print(f"O maior numero é: {maior}")
    time.sleep(2)
    print(f"O menor numero é: {menor}")


def ex044():
    lista = list()

    # contar os numeros inseridos e adiciona-los á lista
    for cont in range(0, 5):
        num = int(input("Insira um numero: "))
        lista.append(num)
        print(f"O {num} foi inserido.")

    # ele procura o numero e se estiver a aparecer mais que uma vez ele limpa da lista
    num_repetido = any(lista.count(num) > 1 for num in set(lista))

    if num_repetido:
        print("Insira um numero diferente, este já foi inserido anteriormente.")

    # ordernar a lista de forma decrescente
    lista.sort(reverse=True)
    print(f"Os numeros que inseriu de forma decrescente são: {lista}")


def ex045():
    lista = list()

    # faz a contagem de numeros
    for count in range(0, 5):
        num = int(input("Insira um numero:"))
        index = 0
        # enquanto o index for menor que o elemento dentro da lista e o numero for maior que o numero dentro do indice
        # ele insere como o primeiro da lista
        while index < len(lista) and num > lista[index]:
            index += 1
        lista.insert(index, num)
        print(f"O {num} foi inserido.")

    # Apresentação final
    print(f"Ordem crescente: {lista}")


def ex046():
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


def ex047():
    # Criação do input e a lista
    eq = input("Insira a equacao matematica com os parentesis respetivamente: ")
    lista = list()
    count = 0
    # Validação da existencia de parentesis: se n tiver parentesis, está incorreto
    for parentesis in eq:
        if parentesis == '(':
            count += 1
        elif parentesis == ')':
            count -= 1
            if count < 0:
                result = "Parentesis incorretos"
                break
            lista.pop()
    # se tiver parentesis diretos está correto e uma segunda validação se n estiver
    else:
        result = "Parentesis corretos" if count == 0 else "Parentesis incorretos"

    print(result)


def ex048():
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


def ex049():
    lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0, 3):
        for v in range(0, 3):
            lista[i][v] = int(input("Insira um numero: "))

    for i in range(0, 3):
        for v in range(0, 3):
            print(f"[{lista[i][v]}]", end=" ")
        print("")


def ex050():
    lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    soma_par = 0
    maior_valor3 = 0
    soma_coluna_2 = 0

    for i in range(0, 3):
        for v in range(0, 3):
            lista[i][v] = int(input("Insira um numero: "))

    for i in range(0, 3):
        for v in range(0, 3):
            if lista[i][v] % 2 == 0:
                soma_par += lista[i][v]

            soma_coluna_2 = sum(lista[1])
            maior_valor3 = max(lista[2])

            print(f"[{lista[i][v]}]", end=" ")
        print("")

    print(f"{soma_par}")
    print(f"{soma_coluna_2}")
    print(f"{maior_valor3}")


funcoes = [ex01, ex02, ex03, ex04, ex05, ex06, ex07, ex08, ex09, ex010, ex011, ex012, ex013, ex014, ex015, ex016, ex017, ex018, ex019, ex020, ex021, ex022, ex023, ex024, ex025, ex026, ex027, ex028, ex029, ex030, ex031, ex032, ex033, ex034, ex035, ex036, ex037, ex038, ex039, ex040, ex041, ex042, ex043, ex044, ex045, ex046, ex047, ex048, ex049, ex050]

while True:
    escolha = input("\nDigite o número da função desejada (1-50) ou 0 para sair --> ")
    if escolha == '0':
        break
    elif escolha.isdigit() and 1 <= int(escolha) <= len(funcoes):
        funcoes[int(escolha) - 1]()
    else:
        print("Escolha inválida. Tente novamente.")

# Mensagem de conclusão
print("Todos os exercícios foram executados.")
