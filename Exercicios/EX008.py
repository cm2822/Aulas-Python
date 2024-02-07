# EX008
km_percorridos = float(input("Insira os kms percorridos: "))
dias_alugado = int(input("Insira o numero de dias que alugou o carro:"))

total_kms = km_percorridos * 0.456
total_dias = dias_alugado * 60

total_pagar = total_kms + total_dias

print("O total a pagar pelo aluguer do carro e de", total_pagar)
