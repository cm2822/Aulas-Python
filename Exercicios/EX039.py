rank_fut_esp = ['Real Madrid', 'Girona', 'Barcelona', 'Athletic Bilbao', 'Atlético de Madrid', 'Real Sociedad', 'Betis', 'Getafe', 'Valência', 'Las Palmas', 'Rayo Vallecano', 'Osasuna', 'Villarreal', 'Mallorca', 'Alavés', 'Sevilla', 'Celta', 'Cádiz', 'Granada', 'Almería']

cinco = rank_fut_esp[:5]

fim_quatro = rank_fut_esp[-4:]

ordem = sorted(rank_fut_esp)

laspalmas = rank_fut_esp.index("Las Palmas") + 1

print(f" Os primeiros classificados: {cinco}")
print(f"Os ultimos: {fim_quatro}")
print(f"Ordem alfabética: {ordem}")
print(f"Classificação dos Las Palmas: {laspalmas}")