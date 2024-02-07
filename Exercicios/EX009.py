"""# EX009
nome = input("Insira o seu nome:").strip()
print("Maiúsculas: {}".format(nome.upper()))
print("Minúsculas: {}".format(nome.lower()))

print("O seu nome tem {} caracteres".format(len(nome) - nome.count(" ")))

pNome = nome.split()

print("O seu primeiro nome é {} e tem {} caracteres".format( pNome[0], len(pNome[0])))
"""

"""# EX 010
num = int(input("Insira um numero de 0 a 9999:"))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))"""

"""# EX 011

frase = input("Escreva uma frase:").upper().strip()

print("A letra 'A' aparece {} vezes.".format(frase.count("A")))
print("O primeiro 'A' está na posição: {}.".format(frase.find("A") + 1))
print("O ultimo 'A' está na posição: {}.".format(frase.rfind("A") + 1))"""

# EX 012

nome = input("Insira o seu nome:").strip()

sNome = nome.split()
primeiraLetra = sNome[0][0]

print("Olá {}, o seu registo está completo.".format(nome))
print("O seu email é {}.{}.edu@empresa.pt".format(primeiraLetra.lower(), sNome[1].lower()))
