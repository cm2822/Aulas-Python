import random, time


class JogoPPT:
    def __init__(self):
        self._opcoes = ["Pedra", "Papel", "Tesoura"]

    def escolha_utilizador(self):
        escolha = input("Escolha Pedra, Papel ou Tesoura -->").capitalize()
        if escolha not in self._opcoes:
            print("Por favor insira uma escolha válida.")
            return self.escolha_utilizador()
        else:
            return escolha

    def escolha_pc(self):
        return random.choice(self._opcoes)

    def verificar_vencedor(self, escolha_utilizador, escolha_pc):
        if escolha_utilizador == escolha_pc:
            print("Empate! WOW")
        elif (
            (escolha_utilizador == "Pedra" and escolha_pc == "Papel")
            or (escolha_utilizador == 'Pedra' and escolha_pc == 'Tesoura')
            or (escolha_utilizador == 'Tesoura' and escolha_pc == 'Papel')
        ):
            print("Você ganhou!!!!!!!!!")
        else:
            print("Você perdeu :( ")

    def jogar(self):
        time.sleep(2)
        print("---/---/---/---/---/")
        print(" PEDRA PAPEL TESOURA")
        print("---/---/---/---/---/")
        time.sleep(0.4)
        print("Bem-vindo ao jogo de pedra papel tesoura contra o CPU!")
        time.sleep(0.4)
        escolha_utilizador = self.escolha_utilizador()
        escolha_pc = self.escolha_pc()
        time.sleep(0.5)
        print(f"A sua escolha --> {escolha_utilizador}")
        time.sleep(0.5)
        print(f"O PC escolheu --> {escolha_pc}")

        self.verificar_vencedor(escolha_utilizador, escolha_pc)


jogo = JogoPPT()
jogo.jogar()
