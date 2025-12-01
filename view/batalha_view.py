class BatalhaView:

    @staticmethod
    def mostrar_status(jogador, inimigo):
        print("\n" + "="*45)
        print(f" STATUS DA BATALHA ".center(45, "="))
        print("="*45)
        print(f"💙 {jogador.nome}: {jogador.vida} HP | ⚡ KI: {jogador.ki}")
        print(f"❤️ {inimigo.nome}: {inimigo.vida} HP | ⚡ KI: {inimigo.ki}")
        print("="*45 + "\n")

    @staticmethod
    def menu_jogador():
        print("Escolha sua ação:")
        print("1️⃣  Ataque Básico")
        print("2️⃣  Ataque Especial")
        print("3️⃣  Defender")
        print("4️⃣  Carregar KI")
        print("5️⃣  Transformar")
        return int(input("➡ "))

    @staticmethod
    def narrar(texto):
        print(texto)

    @staticmethod
    def mostrar_resultado(jogador, inimigo, vencedor):
        print("\n" + "="*50)
        print(f" 🎉 RESULTADO FINAL 🎉 ".center(50))
        print("="*50)
        print(f"VENCEDOR: {vencedor}")
        print(f"{jogador.nome}: {jogador.vida} HP")
        print(f"{inimigo.nome}: {inimigo.vida} HP")
        print("="*50 + "\n")
