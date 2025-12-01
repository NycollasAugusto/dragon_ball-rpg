class BatalhaView:

    @staticmethod
    def mostrar_status(jogador, inimigo, rodada):
        # Status simplificado só como referência de rodada (opcional)
        print(f"\n--- RODADA {rodada} ---")

    @staticmethod
    def menu_jogador():
        print("\nEscolha sua ação:")
        print("1️⃣  Ataque Básico")
        print("2️⃣  Ataque Especial")
        print("3️⃣  Defender")
        print("4️⃣  Carregar KI")
        print("5️⃣  Transformar")
        while True:
            try:
                escolha = int(input("➡ "))
                if 1 <= escolha <= 5:
                    return escolha
                print("Escolha inválida! Digite 1-5.")
            except ValueError:
                print("Digite um número válido!")

    @staticmethod
    def narrar(texto):
        print(texto)

    @staticmethod
    def mostrar_resultado(jogador, inimigo, vencedor):
        print(f"\n🏆 Fim da batalha contra {inimigo.nome}! Vencedor: {vencedor}\n")
class BatalhaView:

    @staticmethod
    def mostrar_status(jogador, inimigo, rodada):
        # Status simplificado só como referência de rodada (opcional)
        print(f"\n--- RODADA {rodada} ---")

    @staticmethod
    def menu_jogador():
        print("\nEscolha sua ação:")
        print("1️⃣  Ataque Básico")
        print("2️⃣  Ataque Especial")
        print("3️⃣  Defender")
        print("4️⃣  Carregar KI")
        print("5️⃣  Transformar")
        while True:
            try:
                escolha = int(input("➡ "))
                if 1 <= escolha <= 5:
                    return escolha
                print("Escolha inválida! Digite 1-5.")
            except ValueError:
                print("Digite um número válido!")

    @staticmethod
    def narrar(texto):
        print(texto)

    @staticmethod
    def mostrar_resultado(jogador, inimigo, vencedor):
        print(f"\n🏆 Fim da batalha contra {inimigo.nome}! Vencedor: {vencedor}\n")
