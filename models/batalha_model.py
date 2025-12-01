import random

class BatalhaModel:
    def __init__(self, jogador, inimigo):
        self.jogador = jogador
        self.inimigo = inimigo
        self.fase = 1

    def jogada_inimigo(self):
        dano = random.randint(5, 15)
        self.jogador.vida -= dano
        return f"{self.inimigo.nome} atacou e causou {dano} de dano!"

    def registrar_resultado(self, vencedor):
        print(f"\n📘 Registro: Vitória de {vencedor} salva!\n")
