def introducao(msg):
    print("-------------------------------------")
    print(f"{msg}")
    print("-------------------------------------")

def calcular_area(comprimento, altura):
    area = comprimento * altura
    print(f"O terreno tem {area:.2f} metros")


introducao("         Area de um terreno      ")
comprimento = float(input("Insira o comprimento do terreno: "))
altura = float(input("Insira a altura do terreno: "))
calcular_area(comprimento, altura)
