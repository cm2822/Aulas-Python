# EX 012

nome = input("Insira o seu nome:").strip()

sNome = nome.split()
primeiraLetra = sNome[0][0]

print("Olá {}, o seu registo está completo.".format(nome))
print("O seu email é {}.{}.edu@empresa.pt".format(primeiraLetra.lower(), sNome[1].lower()))