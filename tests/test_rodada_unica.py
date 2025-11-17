import pytest
import pandas as pd
from Jogo.jogo import Jogo
from Jogo.baralho import Baralho
from Jogo.carta import Carta
from Jogo.bot import Bot

# Mock do CBR
class MockCBR:
    def buscarSimilares(self, registro):
        # Retorna um DataFrame com as colunas que o Bot espera
        df = pd.DataFrame({
            "primeiraCartaHumano": [1],
            "primeiraCartaRobo": [0],   # necessário para evitar KeyError
            "segundaCartaHumano": [3],
            "segundaCartaRobo": [2],
            "terceiraCartaHumano": [5],
            "terceiraCartaRobo": [1],
            "acao": ["jogar"],
            "carta_escolhida": [0]      # coluna usada para decidir carta
        })
        return df

def test_rodada_unica():
    baralho = Baralho()
    jogo = Jogo()

    jogador = jogo.criarJogador("Humano", baralho) #cria joagor
    bot = jogo.criarBot("Bot", baralho, cbr=MockCBR()) #cria bot

    jogador.mao = [Carta(7, "ESPADAS"), Carta(3, "COPAS"), Carta(5, "BASTOS")]
    bot.mao = [Carta(6, "ESPADAS"), Carta(2, "COPAS"), Carta(1, "OUROS")]

    carta_jogador = jogador.jogarCarta(0)

    carta_bot = bot.jogarCarta()

    #verifica se as cartas foram removidas da mão
    assert len(jogador.mao) == 2
    assert len(bot.mao) == 2

    assert carta_bot.valor in [6, 2, 1] #verifica se o bot esta ok

    vencedor = jogo.verificarRodada(carta_jogador, carta_bot) #verifca vencedor
    assert vencedor == "Humano" 

    jogo.pontuarRodada(vencedor) #atualiza pontuação

    assert jogo.pontos_jogador == 1 # verifica se a pontuação vou atribuida 
    assert jogo.pontos_bot == 0

    assert jogo.rodada_atual == 1
