import time


def turma():
    n_alunos = int(input("Insira o numero de alunos que pretende inserir na base de dados --> "))
    # Caso o utilizador insira mais de 22 alunos
    if n_alunos > 22:
        print("Por favor insira um número de alunos entre 1 a 22")
        time.sleep(0.45)
        print(".....Por favor tente novamente.....")
        time.sleep(0.5)
        n_alunos = int(input("Insira o numero de alunos que pretende inserir na base de dados --> "))

    n_notas = int(input("Insira o numero de notas de uma disciplina para cada aluno --> "))

    alunos = []

    for alunos_id in range(1, n_alunos + 1):
        notas = []
        for i in range(1, n_notas + 1):
            time.sleep(0.5)
            nota = float(input(f"Insira a {i}º nota do aluno {alunos_id} --> "))
            # caso o utilzador seja capaz de inserir números supeiores a 20
            if nota > 20:
                print("Por favor insira um valor entre 0 a 20.....Por favor tente novamente")
                nota = float(input(f"Insira a {i}º nota do aluno {alunos_id} --> "))
            print(end='')
            time.sleep(0.5)
            notas.append(nota)

        # Contagem de notas inseridas
        quantidade_notas = len(notas)

        # Maior nota inserida
        maior_nota = max(notas)

        # media de cada aluno
        media_aluno = sum(notas) / quantidade_notas

        # Situação logica de cada aluno
        """usar apenas if, elifs e else para conseguir realizar cada situação"""
        situacao = ""
        if media_aluno < 9.5:
            situacao = "Fraca"
        elif 9.5 > media_aluno < 12:
            situacao = "Razoável"
        elif media_aluno > 12:
            situacao = "Muito bem"

        alunos.append({
            'alunos_id': alunos_id,
            'notas': notas,
            'quantidade_notas': quantidade_notas,
            'maior_nota': maior_nota,
            "media_aluno": media_aluno,
            "situacao": situacao
        })

    media_turma = sum(aluno['media_aluno'] for aluno in alunos) / n_alunos

    while True:
        aluno_desejado = int(input("Insira o número do aluno que deseja observar as suas notas --> "))
        if 1 <= aluno_desejado <= n_alunos:
            aluno_selecionado = alunos[aluno_desejado - 1]
            print(f"\nAluno {aluno_selecionado['aluno_id']}:")
            print(f"Notas: {aluno_selecionado['notas']}")
            print(f"Quantidade de notas inseridas: {aluno_selecionado['quantidade_notas']}")
            print(f"Maior nota: {aluno_selecionado['maior_nota']}")
            print(f"Média do aluno: {aluno_selecionado['media_aluno']}")
            print(f"Situação: {aluno_selecionado['situacao']}")
        else:
            print(f"Aluno inválido. Insira um número entre 1 e {n_alunos}.")

        continuar = input("Deseja esccolher outro aluno? [S/N] --> ").lower()
        if continuar != 's':
            break

    # Imprime a média da turma
    print(f"\nMédia da turma: {media_turma}")


# Chamada da função
turma()
