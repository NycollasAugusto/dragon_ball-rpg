from models.batalha_model import BatalhaModel
from view.batalha_view import BatalhaView

class BatalhaController:
    def __init__(self, jogador, inimigo):
        self.batalha = BatalhaModel(jogador, inimigo)
        self.view = BatalhaView()

    def iniciar(self):
        print(f"\n🔥 INÍCIO DA BATALHA CONTRA {self.batalha.inimigo.nome} 🔥")

        while (
            self.batalha.jogador.vida > 0 and
            self.batalha.inimigo.vida > 0 and
            self.batalha.rodada <= self.batalha.max_rodadas
        ):
            acao = self.view.menu_jogador()
            jogador = self.batalha.jogador
            inimigo = self.batalha.inimigo

            # Registrar apenas a ação feita
            if acao == 1:
                resultado = jogador.atacar_basico(inimigo)
                self.view.narrar(resultado)
            elif acao == 2:
                resultado = jogador.atacar_especial(inimigo)
                self.view.narrar(resultado)
            elif acao == 3:
                jogador.defender()
                self.view.narrar(f"🛡️ {jogador.nome} está defendendo!")
            elif acao == 4:
                self.view.narrar(jogador.carregar_ki())
            elif acao == 5:
                self.view.narrar(jogador.transformar())

            # Ação do inimigo
            resultado_inimigo = self.batalha.jogada_inimigo()
            self.view.narrar(resultado_inimigo)

            self.batalha.rodada += 1

        vencedor = (
            "Empate (limite de rodadas)"
            if self.batalha.rodada > self.batalha.max_rodadas
            else (jogador.nome if jogador.vida > 0 else inimigo.nome)
        )

        self.view.mostrar_resultado(jogador, inimigo, vencedor)
        self.batalha.registrar_resultado(vencedor)
