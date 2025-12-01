Dragon Ball Terminal — Inimigo com Machine Learning

Este projeto é uma versão de Dragon Ball para terminal, onde o jogador batalha contra um inimigo que aprende com as escolhas do jogador usando Machine Learning (Logistic Regression).
O objetivo é criar um sistema simples, rápido e divertido onde o inimigo fica mais inteligente a cada luta!
 Funcionalidades
 Sistema de combate em turnos

Atacar

Defender

Carregar energia
 Inimigo com Inteligência Artificial (IA)

O inimigo usa Machine Learning para decidir qual ação tomar baseado em:

Vida do inimigo

Vida do jogador

Nível de agressividade

 IA que aprende com as batalhas

Após cada luta, o inimigo analisa:

se venceu ou perdeu

qual ação tomou

estado das vidas no momento

E adiciona esses dados ao treinamento, ficando cada vez mais esperto.

 Como funciona a IA

A classe InimigoAI usa LogisticRegression do scikit-learn.
Os dados usados pelo modelo são:

Vida do Inimigo	Vida do Jogador	Agressividade	Ação
100	100	0.5	defender
30	80	0.5	atacar
80	20	0.5	carregar

Após cada batalha, novos dados são adicionados com base no resultado.

Código da IA (Machine Learning)
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

 Instalação
1. Clone o repositório
git clone MeuProjeto
cd MeuProjeto

2. Instale as dependências
pip install numpy scikit-learn

 Como rodar

Execute o arquivo principal:

python main.py

 Tecnologias usadas

Python

Scikit-learn (Logistic Regression)

NumPy

 Objetivo educacional

Esse projeto demonstra:

Como integrar ML em jogos simples

Como treinar modelos dinamicamente

Como criar IA adaptativa usando Logistic Regression

 

