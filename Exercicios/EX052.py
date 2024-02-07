aluno = dict()


aluno["nome"] = input("Nome do aluno -->")
aluno["media"] = int(input("Media do aluno -->"))

if aluno["media"] >= 9.5:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"

print(f"Nome --> {aluno['nome']}")
print(f"Media --> {aluno['media']}")
print(f"Situação --> {aluno['situacao']}")
