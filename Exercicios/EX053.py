from _operator import itemgetter
import random

jogadores = ["Jogador1", "Jogador2", "Jogador3", "Jogador4"]

ordem_jogador = {}

for jogador in jogadores:
    ordem_jogador[jogador] = random.randint(1,6)

ranking = sorted(ordem_jogador.items(), key=itemgetter(1))

print("Ordem de jogada:")
for i, (jogador, _) in enumerate(ranking):
    print(f"{i + 1}º {jogador}", end="--> ")
    print(f"{ordem_jogador[jogador]}")