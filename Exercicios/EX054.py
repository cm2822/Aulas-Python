import time

simulador = {}

simulador["nome"] = input("Nome: ")
simulador["ano_nasc"] = int(input("Ano de Nascimentos: "))
simulador["rendimentos"] = float(input("Rendimentos mensais: "))
simulador["despesas"] = float(input("Despesas mensais: "))
simulador["montante_cred"] = float(input("Montante do Crédito: "))
simulador["prazo"] = int(input("Prazo do crédito: "))
simulador["ano_atual"] = 2023

simulador["idade"] = simulador["ano_atual"] - simulador["ano_nasc"]

if simulador["rendimentos"] > simulador["despesas"]:
    simulador["remanescente"] = simulador["rendimentos"] - simulador["despesas"]
else:
    simulador["remanescente"] = simulador["despesas"] - simulador["rendimentos"]

if simulador["remanescente"] > simulador["montante_cred"] / simulador["prazo"]:
    simulador["credito"] = 'Aprovado'
else:
    simulador["credito"] = 'Reprovado'

print("\nInformações do Cliente:")
time.sleep(0.8)
print(f"Nome --> {simulador['nome']}")
time.sleep(0.8)
print(f"Ano de Nascimento --> {simulador['ano_nasc']}")
time.sleep(0.8)
print(f"Idade --> {simulador['idade']} anos")
time.sleep(0.8)
print(f"Rendimentos Mensais --> €{simulador['rendimentos']:.2f}")
time.sleep(0.8)
print(f"Despesas Mensais --> €{simulador['despesas']:.2f}")
time.sleep(0.8)
print(f"Remanescente após Despesas --> €{simulador['remanescente']:.2f}")
time.sleep(0.8)
print(f"Montante do Crédito --> €{simulador['montante_cred']:.2f}")
time.sleep(0.8)
print(f"Prazo do Crédito--> {simulador['prazo']} anos")
time.sleep(0.8)
print(f"Valor Mensal do Crédito --> €{simulador['montante_cred'] / simulador['prazo']:.2f}")
time.sleep(0.8)

# Mensagem de aprovação ou reprovação
if simulador["credito"] == 'Aprovado':
    print("\n A calcular", end="")
    time.sleep(0.2)
    print(".", end="")
    time.sleep(0.2)
    print(".", end="")
    time.sleep(0.2)
    print(".", end="")
    time.sleep(0.8)
    print("\nParabéns! Seu crédito foi aprovado.")
else:
    print("\nDesculpe, seu crédito foi reprovado.")

if simulador["remanescente"] > simulador["montante_cred"] / simulador["prazo"]:
    simulador["credito"] = 'Aprovado'
else:
    simulador["credito"] = 'Reprovado'
