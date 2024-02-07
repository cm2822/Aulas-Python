# EX 025 Letras em palindromo

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