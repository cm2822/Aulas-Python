"""aluno = {"nome": "Cesar", "Media": 14}
print(f"O aluno {aluno['nome']} tem a média de {aluno['Media']} valores.")

if aluno["Media"] >= 9.5:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Reprovado"


print(aluno['Situação'])
print(aluno.items())"""

"""aluno = dict()

aluno["Nome"] = input("Nome do aluno: ")
aluno["EX001"] = int(input("nota: "))
aluno["EX002"] = int(input("nota: "))
aluno["EX003"] = int(input("nota: "))


aluno["Media"] = (aluno["EX001"] + aluno["EX002"] + aluno["EX003"]) / 3

print(aluno.items())"""


cidade = {"Nome": "Porto", "Codigo": "OPO", "Baixa": "Ribeira", "Rio": "Douro"}
cidade2 = {"Nome": "Lisboa", "Codigo": "LX", "Baixa": "Chiado", "Rio": "Tejo"}


pais = list()
pais.append(cidade)
pais.append(cidade2)


"""for k, v in cidade.items():
    print(f"O {k} é {v}")"""

for c in range(0, len(pais)):
    print(f"As cidades registadas são: {pais[c]['Nome']}")