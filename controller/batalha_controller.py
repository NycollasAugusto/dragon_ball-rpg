from models.batalha_model import BatalhaModel
from view.batalha_view import BatalhaView

class BatalhaController:
    def __init__(self, jogador, inimigo):
        self.batalha = BatalhaModel(jogador, inimigo)
        self.view = BatalhaView()

    def iniciar(self):
        print("\n🔥 INÍCIO DA BATALHA 🔥\n")

        while (
            self.batalha.jogador.vida > 0 and
            self.batalha.inimigo.vida > 0 and
            self.batalha.rodada <= self.batalha.max_rodadas
        ):
            self.view.mostrar_status(
                self.batalha.jogador,
                self.batalha.inimigo,
                self.batalha.rodada
            )

            acao = self.view.menu_jogador()

            jogador = self.batalha.jogador
            inimigo = self.batalha.inimigo

            if acao == 1:
                print(jogador.atacar_basico(inimigo))
            elif acao == 2:
                print(jogador.atacar_especial(inimigo))
            elif acao == 3:
                jogador.defender()
                print(f"\n🛡️ {jogador.nome} está defendendo!")
            elif acao == 4:
                print(jogador.carregar_ki())
            elif acao == 5:
                print(jogador.transformar())

            print(self.batalha.jogada_inimigo())

            self.batalha.rodada += 1

        vencedor = (
            "Empate (limite de rodadas)"
            if self.batalha.rodada > self.batalha.max_rodadas
            else (jogador.nome if jogador.vida > 0 else inimigo.nome)
        )

        self.view.mostrar_resultado(jogador, inimigo, vencedor)
        self.batalha.registrar_resultado(vencedor)
