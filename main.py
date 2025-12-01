from models.personagem_model import Personagem
from controller.batalha_controller import BatalhaController

def main():
    goku = Personagem("Goku", 120, 40, 15, 35, "SSJ")
    freezer = Personagem("Freeza", 150, 0, 12, 0, "Final")

    BatalhaController(goku, freezer).iniciar()

main()
