from controller.batalha_controller import BatalhaController
from models.personagem_model import Personagem

def main():
    # Personagem do jogador
    goku = Personagem("Goku", 150, 50, 20, 40, "Super Saiyajin")

    # Lista de inimigos em sequência (torneio)
    inimigos = [
        Personagem("Freezer", 100, 40, 15, 30, "Final Form"),
        Personagem("Cell", 120, 50, 18, 35, "Perfect Form"),
        Personagem("Majin Boo", 150, 60, 20, 40, "Kid Buu")
    ]

    # Loop para enfrentar cada inimigo
    for inimigo in inimigos:
        print(f"\n⚔️ Próximo inimigo: {inimigo.nome} ⚔️")
        BatalhaController(goku, inimigo).iniciar()

        # Se o jogador morrer, encerra o torneio
        if goku.vida <= 0:
            print("\n💀 Você foi derrotado! Fim do torneio.")
            break
    else:
        print("\n🏆 Parabéns! Você venceu todos os inimigos do torneio!")

if __name__ == "__main__":
    main()
