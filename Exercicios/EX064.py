def celsius(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Estão neste momento, {fahrenheit}º")

def fahrenheit(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Estão neste momento, {celsius}º")


opcao = 0
while opcao != 3:
    print("[ 1 ] - Celsius")
    print("[ 2 ] - Fahrenheit")
    print("[ 3 ] - Sair")

    print("Insira a sua opção: ")
    opcao = int(input("--> "))

    if opcao == 1:
        celsius = float(input("Fahrenheit -->"))
        fahrenheit(celsius)
    elif opcao == 2:
        fahrenheit = float(input("Celsius -->"))
        celsius(fahrenheit)
