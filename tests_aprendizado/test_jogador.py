import pytest
from Jogo.jogador import Jogador
from Jogo.baralho import Baralho

def test_jogador_recebe_carta():
    baralho = Baralho()
    jogador = Jogador("Alice")
    jogador.criarMao(baralho) 

    assert len(jogador.mao) == 3 #verifica quant de cartas

def test_jogador_joga_carta():
    baralho = Baralho()
    jogador = Jogador("Maria")
    jogador.criarMao(baralho)
    
    carta_escolhida = 0  # escolhe a primeira carta
    carta = jogador.jogarCarta(carta_escolhida)
    
    assert carta not in jogador.mao #verica se a carta foi removida da mão
    assert len(jogador.mao) == 2 #verifica quant cartas
