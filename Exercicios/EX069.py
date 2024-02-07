
def calc_imc(peso, altura):
    imc = peso / (altura**2)

    if imc < 18.5:
        print("Abaixo do peso! Boa !")
    elif 18.5 <= imc < 25:
        print("Peso Normal! Muito bem !")
    elif 25 <= imc < 30:
        print("Sobrepeso, atenção..")
    elif 30 <= imc < 35:
        print("Obesidade de grau 1...")
    elif 35 <= imc < 40:
        print("Obesidade de grau 2...")
    else:
        print("Obesidade de grau 3....mórbido")
    return imc


print("Bem vindo á Calculadora de IMC", end="\n")

peso = float(input("Insira o seu peso -->"))
altura = float(input("Insira a sua altura --> "))
imc = calc_imc(peso, altura)

print()
print(f"O seu imc é: {imc:.2f}")
