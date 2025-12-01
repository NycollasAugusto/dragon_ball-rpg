from models.batalha_model import BatalhaModel
from view.batalha_view import BatalhaView

class BatalhaController:

    def __init__(self, jogador, inimigo):
        self.batalha = BatalhaModel(jogador, inimigo)
        self.view = BatalhaView()

    def iniciar(self):
        print("\n🔥 INÍCIO DA BATALHA 🔥\n")

        while self.batalha.jogador.vida > 0 and self.batalha.inimigo.vida > 0:

            self.view.mostrar_status(self.batalha.jogador, self.batalha.inimigo)
            acao = self.view.menu_jogador()

            jogador = self.batalha.jogador
            inimigo = self.batalha.inimigo

            if acao == 1:
                print(jogador.atacar_basico(inimigo))
            elif acao == 2:
                print(jogador.atacar_especial(inimigo))
            elif acao == 3:
                jogador.defendendo = True
                print("\n🛡️ Você está defendendo!")
            elif acao == 4:
                jogador.ki += 20
                print("\n⚡ Você carregou KI +20!")
            elif acao == 5:
                print(jogador.transformar())

            print(self.batalha.jogada_inimigo())

        vencedor = (
            jogador.nome if jogador.vida > 0 else inimigo.nome
        )

        self.view.mostrar_resultado(jogador, inimigo, vencedor)
        self.batalha.registrar_resultado(vencedor)
