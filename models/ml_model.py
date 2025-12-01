import random

class InimigoAI:
    def __init__(self, agressividade=0.5):
        self.agressividade = agressividade

    def decidir_acao(self, vida_inimigo, vida_jogador):
        # IA simples por enquanto
        if vida_inimigo < 30:
            return "defender"

        if vida_jogador < 20:
            return "atacar"

        return random.choice(["atacar", "carregar", "defender"])
