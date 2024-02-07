import time

print("---/---/---/---/---/---/")
print("  CALCULADORA DE IMC")
print("---/---/---/---/---/---/")

time.sleep(2)
peso = float(input("Insira o seu peso: \n"))

time.sleep(2)

altura = float(input("Insira a sua altura: \n"))


imc = round(peso / (altura * altura),2)

time.sleep(3)

print("Estamos a analisar o imc....\n")
time.sleep(1)
print("Análise feita\n")


if imc < 18.5:
    time.sleep(2)
    print(f"|-- O seu imc é de {imc}. Isto significa que está abaixo do peso ideal. --|")

elif imc <= 24.9:
    time.sleep(2)
    print(f"|-- O seu imc é de {imc}. Isto significa que está no peso ideal. --|")

elif imc <= 29.9:
    time.sleep(2)
    print(f"|-- O seu imc é de {imc}. Isto significa que está acima do peso ideal mas não muito distante. --|")

elif imc <= 34.9:
    time.sleep(2)
    print(f"|-- O seu imc é de {imc}. Isto significa que está na faixa da obeisade grau 1 :( . --|")

elif imc <= 39.9:
    time.sleep(2)
    print(f"|-- O seu imc é de {imc}. Isto significa que está na faixa da obeisade grau 2 :( . --|")

else:
    time.sleep(2)
    print(f"O seu imc é de {imc}. Isto significa que está na faixa da obesiade grau 3. Tas gordoooooooooooo! --|")