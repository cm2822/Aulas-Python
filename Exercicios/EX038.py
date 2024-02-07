num_extenso = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
               'treze', 'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte']

num = int(input("Insira um número de 0 a 20: "))

if 0 <= num <= 20:
    print(f"O numero {num} em extenso é {num_extenso[num]} ")
else:
    print("O número que introduziu não está dentro dos parâmetros.")
