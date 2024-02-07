def analisar_notas(notas):
    # Calcula a quantidade de notas
    quantidade = len(notas)

    # Calcula a maior nota
    maior_nota = max(notas)

    # Calcula a média da turma
    media = sum(notas) / quantidade

    # Define a situação com base nas condições fornecidas
    if media > 12:
        situacao = "Boa"
    elif media < 9.5:
        situacao = "Fraca"
    else:
        situacao = "Razoável"

    # Cria um dicionário com os resultados
    resultado = {
        'quantidade': quantidade,
        'maior_nota': maior_nota,
        'media': media,
        'situacao': situacao
    }

    return resultado


# Exemplo de uso
notas_alunos = [15, 17, 20, 9.5, 9]
resultado_analise = analisar_notas(notas_alunos)

print("Análise das notas: ")
print("Quantidade de notas --> ", resultado_analise['quantidade'])
print("Maior nota --> ", resultado_analise['maior_nota'])
print("Média da turma --> ", resultado_analise['media'])
print("Situação --> ", resultado_analise['situacao'])

