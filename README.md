🐉 Dragon Ball Terminal — Inimigo com Machine Learning

Um mini-jogo de Dragon Ball totalmente no terminal, com batalhas em turnos e um inimigo inteligente usando Machine Learning (Logistic Regression).
A cada luta, o inimigo coleta dados, aprende com seus erros e se torna mais difícil de vencer!

🚀 Funcionalidades
⚔️ Sistema de combate em turnos

Você pode escolher entre:

🥊 Ataque básico

🌩️ Ataque especial

🛡️ Defender

🔋 Carregar KI

🔥 Transformar (quando disponível)

🧠 Inimigo com Inteligência Artificial (IA)

O oponente usa Logistic Regression para decidir qual ação é melhor com base em:

❤️ Vida do inimigo

💙 Vida do jogador

🔥 Nível de agressividade

📈 IA que aprende com cada batalha

Após o fim da luta, a IA analisa:

Se venceu ou perdeu

Qual ação tomou

Como estavam as vidas no momento

E adiciona isso ao treinamento

➡ Resultado: o inimigo fica mais esperto e imprevisível conforme você joga.

🗂️ Como funciona a IA

A classe InimigoAI usa:

numpy para gerenciar dados

scikit-learn para o modelo Logistic Regression

📊 Base inicial de treinamento
Vida do Inimigo	Vida do Jogador	Agressividade	Ação
100	100	0.5	defender
30	80	0.5	atacar
80	20	0.5	carregar

Com base nisso, o modelo começa a prever ações —
e conforme você joga, o dataset cresce.

🤖 Código da IA (Machine Learning)
import random
import numpy as np
from sklearn.linear_model import LogisticRegression

class InimigoAI:
    def __init__(self, agressividade=0.5):
        self.agressividade = agressividade

        # Modelo de Machine Learning
        self.model = LogisticRegression(max_iter=500)

        # Base inicial de treino (3 exemplos)
        self.X = np.array([
            [100, 100, agressividade],
            [30, 80, agressividade],
            [80, 20, agressividade]
        ])

        # 0 = defender | 1 = atacar | 2 = carregar
        self.y = np.array([0, 1, 2])

        # Treina o modelo inicial
        self.model.fit(self.X, self.y)

    def decidir_acao(self, vida_inimigo, vida_jogador):
        dados = np.array([[vida_inimigo, vida_jogador, self.agressividade]])

        try:
            acao = self.model.predict(dados)[0]
        except Exception:
            # Backup caso o modelo falhe
            acao = random.choice([0, 1, 2])

        acoes = ["defender", "atacar", "carregar"]
        return acoes[acao]

    def aprender(self, vida_inimigo, vida_jogador, acao_tomada, venceu):
        mapa = {"defender": 0, "atacar": 1, "carregar": 2}
        acao = mapa[acao_tomada]

        # Reforço leve para vitórias
        repeticoes = 2 if venceu else 1

        novo_x = np.tile(
            np.array([[vida_inimigo, vida_jogador, self.agressividade]]),
            (repeticoes, 1)
        )
        novo_y = np.tile(np.array([acao]), repeticoes)

        # Atualiza dataset
        self.X = np.vstack([self.X, novo_x])
        self.y = np.hstack([self.y, novo_y])

        # Garante que existe mais de 1 classe para treinar
        if len(set(self.y)) > 1:
            self.model.fit(self.X, self.y)

🧩 Instalação
1️⃣ Clone o repositório
git clone MeuProjeto
cd MeuProjeto

2️⃣ Instale as dependências
pip install numpy scikit-learn

▶️ Como rodar

Execute o arquivo principal:

python main.py

🛠️ Tecnologias usadas

🐍 Python

📘 Scikit-learn (Logistic Regression)

🔢 NumPy