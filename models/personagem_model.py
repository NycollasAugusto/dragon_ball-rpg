class Personagem:
    def __init__(self, nome, vida, ki, ataque_basico, ataque_especial, transformacao):
        self.nome = nome
        self.vida = vida
        self.ki = ki
        self.ataque_basico = ataque_basico
        self.ataque_especial = ataque_especial
        self.transformacao = transformacao
        self.defendendo = False

    def atacar_basico(self, alvo):
        dano = self.ataque_basico
        alvo.vida -= dano
        return f"{self.nome} causou {dano} de dano em {alvo.nome}!"

    def atacar_especial(self, alvo):
        if self.ki < 10:
            return f"{self.nome} tentou usar especial mas não tinha KI!"
        
        self.ki -= 10
        dano = self.ataque_especial
        alvo.vida -= dano
        return f"{self.nome} lançou um ESPECIAL de {dano} em {alvo.nome}! 🔥"

    def defender(self):
        self.defendendo = True
        return f"{self.nome} está defendendo! 🛡️"

    def carregar_ki(self):
        self.ki += 20
        return f"{self.nome} carregou KI +20 ⚡"

    def transformar(self):
        return f"{self.nome} transformou em {self.transformacao}! 🔥🔥🔥"
