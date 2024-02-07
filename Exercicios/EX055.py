futebol = []
opcao = ""

while opcao != 'n':
    jogador = {}
    jogador["nome"] = input("Nome do jogador: ")
    jogador["num_jogos"] = int(input("Numero de jogos que jogou: "))
    jogador["golos"] = int(input("Numero de golos marcados: "))
    jogador["mediagolos"] = jogador["golos"] / jogador["num_jogos"]
    futebol.append(jogador)
    opcao = input("\nQuer continuar ? [s/n] --> ")

nome_jogador = input("Insira o nome do jogador: ")

for jogador in futebol:
    if jogador["nome"] == nome_jogador:
        print(f"Nome do jogador --> {jogador["nome"]} ")
        print(f"Número de jogos que participou --> {jogador["num_jogos"]} ")
        print(f"Número de golos marcados --> {jogador["golos"]}")
        print(f"Media de golos por jogo é de --> {jogador["mediagolos"]:.2f} por jogo")
else:
    print(f"O jogador {nome_jogador} não existe.")

print("Todos os resultados: ")
for jogador in futebol:
    print(f"Nome do jogador --> {jogador["nome"]} ")
    print(f"Número de jogos que participou --> {jogador["num_jogos"]} ")
    print(f"Número de golos marcados --> {jogador["golos"]}")
    print(f"Media de golos por jogo é de --> {jogador["mediagolos"]:.2f} por jogo")
