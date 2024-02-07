import datetime


def validar_carta(ano):
    ano_atual = datetime.datetime.today().year
    idade = ano_atual - ano
    print(f"Esta pessoa tem {idade} anos")
    if idade > 18:
        return "Já pode tirar a carta! Boa sorte."
    elif idade < 16:
        return "Ainda não pode retirar a carta, infelizmente."
    elif 16 < idade < 18:
        return "Pode tirar a carta...mas tem de ter uma autorização provinda dos pais."


ano = int(input("Em que ano nasceu? "))
print(validar_carta(ano))
