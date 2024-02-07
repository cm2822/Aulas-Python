import time


def calculadora(a, b, c):
    if c == '+':
        soma = a + b
        time.sleep(0.5)
        print("Analisar os números inseridos...")
        time.sleep(0.5)
        print(f"{a:.0f} + {b:.0f} = {soma:.0f}")
    elif c == '-':
        sub = a - b
        time.sleep(0.5)
        print("Analisar os números inseridos...")
        time.sleep(0.5)
        print(f"{a:.0f} - {b:.0f} = {sub:.0f}")
        return sub
    elif c == '*':
        mul = a * b
        time.sleep(0.5)
        print("Analisar os números inseridos...")
        time.sleep(0.5)
        print(f"{a:.0f} * {b:.0f} = {mul:.0f}")
        return mul
    elif c == '/':
        div = a / b
        time.sleep(0.5)
        print("Analisar os números inseridos...")
        time.sleep(0.5)
        print(f"{a:.0f} / {b:.0f} = {div:.0f}")