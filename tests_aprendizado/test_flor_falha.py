import pytest
from Jogo.jogador import Jogador
from Jogo.baralho import Baralho
from Jogo.carta import Carta

def test_flor_falha():
    baralho = Baralho()
    jogador = Jogador("Humano")

    jogador.mao = [Carta(1, "COPAS"), Carta(7, "COPAS"), Carta(5, "PAUS")]

    jogador.checaFlor()  #verifca flor

    assert jogador.flor is True  #define flor como true (calsa erro)
