
# EX 014

#Inserir a velocidade que o radar apanha
velocidade = int(input("Insere ai a velocidade a que o carro ia: "))

#Utilizar um ciclo de eventos para saber o que fazer caso aconteça diferentes eventos (lol)
if velocidade > 80:
    print("Super multado, esquece, es mauco")
    multa = 100 + 7 * (velocidade - 80)
    print("Tas com uma coima de ", multa, 'toine')

elif velocidade <= 80:
    print("Muito responsavel, continua assim")

