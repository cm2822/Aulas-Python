import datetime


# Criando o cabeçalho para reutilizar:
def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


# Funcao ler numero inteiro. Para reutilizar!
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("\n\033[31mERRO: Por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mUsuário preferiu não digitar o número.\033[m")
            return None
        else:
            return n


# Criando o Menu
def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[33mSua Opção -> \033[m")
    return opc


# Apenas para ver se arquivo de texto existe.
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# Se não existir, vai criar.
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo\033[m')
    else:
        print('\033[32mO Arquivo foi criado com sucesso!\033[m')


# Funções previamente definidas ...

# Função para checar duplicatas
def duplicados(novo_livro):
    return any(
        livro_encontrado['isbn'] == novo_livro['isbn']
        for livro_encontrado in livros
    )


# Função para adicionar um livro à lista
def adicionar_livro():
    livro = {}

    livro["utilizador"] = input("Insira o seu nome --> ")
    livro["titulo_livro"] = input("Nome do Livro --> ")
    livro["autor"] = input("Autor ou autores --> ")
    livro["isbn"] = input("ISBN --> ")

    while len(livro['isbn']) != 13 or not livro['isbn'].startswith('978'):
        print("O ISBN tem que ter obrigatoriamente 13 dígitos e começar por '978'.")
        livro['isbn'] = str(input('ISBN: '))

    try:
        livro['ano'] = int(input('Ano de Publicação: '))
        if len(str(livro['ano'])) != 4:
            raise ValueError("O ano deve ter obrigatoriamente 4 dígitos.")
    except ValueError as e:
        print(f"Erro: {e}")
        return

    livro['editora'] = str(input("Nome da Editora: "))
    livro['categoria'] = str(input("Qual categoria?"))
    livro['disponibilidade'] = bool(int(input("Disponível? (1 para sim, 0 para não) ")))

    if not duplicados(livro):
        livros.append(livro)
        print("Livro adicionado com sucesso.")
    else:
        print("Este livro já existe.")


# Função para remover um livro da lista
def remover_livro():
    utilizador = input("Insira o seu nome --> ")
    ref = input("Insira a referência que tiver do livro (titulo, autor, isbn) --> ")

    livro_encontrado = None
    for livro in livros:
        if ref.lower() in livro['titulo_livro'].lower() or ref.lower() in livro['autor'].lower() or ref == livro['isbn']:
            livro_encontrado = livro
            break

    if livro_encontrado is not None:
        print(f"Nome do Livro: {livro_encontrado['titulo_livro']}")
        print(f"Autor: {livro_encontrado['autor']}")
        print(f"ISBN: {livro_encontrado['isbn']}")
        print(f"Editora: {livro_encontrado['editora']}")
        print(f"Categoria: {livro_encontrado['categoria']}")
        print(f"Disponibilidade: {livro_encontrado['disponibilidade']}")

        confirmar = input("É este o livro que procura? [s/n] --> ").lower()
        if confirmar == 's':
            if livro_encontrado["disponibilidade"]:
                devolvido = input("O livro está marcado como emprestado. Foi devolvido? [s/n] --> ").lower()
                if devolvido != 's':
                    print("Não é possível remover o livro enquanto estiver emprestado.")
                else:
                    livros.remove(livro_encontrado)
                    print(f"O livro foi removido da base de dados por {utilizador}.")
            else:
                livros.remove(livro_encontrado)
                print(f"O livro foi removido da base de dados por {utilizador}.")
        else:
            print("Operação cancelada.")
    else:
        print("Livro não encontrado na base de dados.")
        pass


# Função para listar livros
def listar_livros():
    for livro in livros:
        print(f"Nome do Livro: {livro['titulo_livro']}")
        print(f"Autor: {livro['autor']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Editora: {livro['editora']}")
        print(f"Categoria: {livro['categoria']}")
        print("-----")


# Função para procurar um livro
def procurar_livro():
    print("Livros Disponíveis:")
    for livro in livros:
        if livro['disponibilidade']:
            print(f"Nome do Livro: {livro['titulo_livro']}")
            print(f"Autor: {livro['autor']}")
            print(f"ISBN: {livro['isbn']}")
            print(f"Editora: {livro['editora']}")
            print(f"Categoria: {livro['categoria']}")
            print("-----")


# Função para realizar empréstimo ou devolução de livros
def emprestimo_devolucao():
    utilizador = input("Insira o seu nome --> ")
    ref = input("Insira a referência que tiver do livro (titulo, autor, isbn) --> ")

    livro_encontrado = None
    for livro in livros:
        if ref.lower() in livro['titulo_livro'].lower() or ref.lower() in livro['autor'].lower() or ref == livro['isbn']:
            livro_encontrado = livro
            break

    if livro_encontrado is not None:
        print(f"Nome do Livro: {livro_encontrado['titulo_livro']}")
        print(f"Autor: {livro_encontrado['autor']}")
        print(f"ISBN: {livro_encontrado['isbn']}")
        print(f"Editora: {livro_encontrado['editora']}")
        print(f"Categoria: {livro_encontrado['categoria']}")
        print(f"Disponibilidade: {livro_encontrado['disponibilidade']}")
        confirmar = input("É este o livro que procura? [s/n] --> ").lower()

        if confirmar == 's':
            if livro_encontrado['disponibilidade']:
                emprestimo = input("Deseja realizar o empréstimo deste livro? [s/n] ? --> ").lower()
                if emprestimo == 's':
                    livro_encontrado['disponibilidade'] = False
                    print(
                        f"Empréstimo realizado com sucesso a {utilizador}. Data do empréstimo: {datetime.datetime.now()}")
            else:
                devolucao = input("Deseja realizar a devolução deste livro? [s/n] ? --> ").lower()
                if devolucao == 's':
                    livro_encontrado['disponibilidade'] = True
                    print(
                        f"Devolução realizada com sucesso de {utilizador}. Data da devolução: {datetime.datetime.now()}")
        else:
            print("Operação cancelada.")
    else:
        print("Livro não encontrado na base de dados.")
        pass


# Função principal para interagir com o usuário
def biblioteca():
    opcao = 0
    while opcao != 6:
        print("[ 1 ] - Adicionar Livro")
        print("[ 2 ] - Remover Livro")
        print("[ 3 ] - Listar Livro")
        print("[ 4 ] - Procurar Livro")
        print("[ 5 ] - Empréstimo/Devolução de Livros")
        print("[ 6 ] - Sair")

        print("O que deseja efetuar")
        opcao = int(input("--> "))

        if opcao == 1:
            adicionar_livro()
        elif opcao == 2:
            remover_livro()
        elif opcao == 3:
            listar_livros()
        elif opcao == 4:
            procurar_livro()
        elif opcao == 5:
            emprestimo_devolucao()
        elif opcao == 6:
            print("Saindo da Biblioteca. Até logo!")
        else:
            print("Opção inválida. Tente novamente.")


def cadastrar(arquivo):
    try:
        with open(arquivo, 'at') as a:
            adicionar_livro()
            a.write(str(livros) + '\n')

        print(f'\033[32mNovo registro de livro adicionado com sucesso!\033[m')
    except:
        print('Houve um erro na hora de escrever os dados!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler arquivo!\033[m')
    else:
        print(a.readlines())


arquivo = "grupo001.txt"

if arquivoExiste(arquivo):
    print('Arquivo Encontrado com sucesso!')
else:
    print('Erro ao encontrar o arquivo!')
    criarArquivo(arquivo)

cabecalho("SISTEMA BIBLIOTECÁRIO")

livros = []

while True:
    resposta = menu(
        ["Adicionar livro", "Remover livro", "Listar livros", "Procurar livros", "Emprestar livros", "Sair do Sistema"]
    )

    if resposta == 1:
        cabecalho("ADICIONAR LIVRO")
        cadastrar(arquivo)

    elif resposta == 2:
        cabecalho("REMOVER LIVRO")
        remover_livro()

    elif resposta == 3:
        cabecalho("LISTAR LIVROS")
        listar_livros()

    elif resposta == 4:
        cabecalho("PROCURAR LIVROS")
        procurar_livro()

    elif resposta == 5:
        cabecalho("EMPRÉSTIMO/DEVOLUÇÃO DE LIVROS")
        emprestimo_devolucao()

    elif resposta == 6:
        print("Saindo da Biblioteca. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
# Execução do programa
biblioteca()
