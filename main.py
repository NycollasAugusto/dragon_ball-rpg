from controller.batalha_controller import BatalhaController
from models.personagem_model import Personagem

def main():
    goku = Personagem("Goku", 120, 50, 15, 35, "Super Saiyajin")
    freezer = Personagem("Freezer", 100, 40, 12, 30, "Final Form")

    BatalhaController(goku, freezer).iniciar()

if __name__ == "__main__":
    main()
