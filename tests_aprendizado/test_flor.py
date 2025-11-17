import pytest
from Jogo.jogo import Jogo
from Jogo.baralho import Baralho
from Jogo.jogador import Jogador
from Jogo.carta import Carta

def test_flor():
    baralho = Baralho()
    jogo = Jogo()

    jogador = jogo.criarJogador("Ana", baralho)

    jogador.mao = [Carta(1, "COPAS"), Carta(7, "COPAS"), Carta(5, "COPAS")]

    assert jogador.flor is False #antes do inicio da partida flor deve ser falsa

    jogador.mostrarOpcoes() #inicia 

    jogador.checaFlor()  #verifca flor

    assert jogador.flor is True  #define flor como true (calsa erro)
