
jogos_e_precos = (
    ("GTA V", 29.99),
    ("Pokemon", 49.99),
    ("Sonic", 19.99),
    ("Jupiter", 39.99),
    ("Warframe", 59.99)
)

print("Jogo ------ Preço")
for jogo, preco in jogos_e_precos:
    print(f"{jogo} ${preco:.2f}")
