from models.personagem_model import Personagem
import random

class BatalhaModel:
    def __init__(self, jogador: Personagem, inimigo: Personagem):
        self.jogador = jogador
        self.inimigo = inimigo
        self.rodada = 1
        self.max_rodadas = 10

    def jogada_inimigo(self):
        # IA simples aleatória
        if self.inimigo.ki >= 10:
            acao = random.choice(["basico", "especial", "defender", "carregar"])
        else:
            acao = random.choice(["basico", "defender", "carregar"])

        if acao == "basico":
            return self.inimigo.atacar_basico(self.jogador)
        elif acao == "especial":
            return self.inimigo.atacar_especial(self.jogador)
        elif acao == "defender":
            self.inimigo.defender()
            return f"{self.inimigo.nome} está defendendo! 🛡️"
        elif acao == "carregar":
            self.inimigo.carregar_ki()
            return f"{self.inimigo.nome} carregou KI! ⚡"

    def registrar_resultado(self, vencedor):
        print(f"\n🏆 Fim da batalha! Vencedor: {vencedor}")
