# tests/test_partida_completa.py
import pytest
from Jogo.jogo import Jogo
from Jogo.jogador import Jogador
from Jogo.carta import Carta
from Jogo.baralho import Baralho

def test_partida():
    baralho = Baralho()
    jogo = Jogo()

    j1 = jogo.criarJogador("Alice", baralho)
    j2 = jogo.criarJogador("Carlos", baralho)

    j1.mao = [Carta(4, "ESPADAS"), Carta(12, "COPAS"), Carta(1, "OUROS")]

    j2.mao = [Carta(5, "ESPADAS"), Carta(11, "COPAS"), Carta(3, "PAUS")]

    c1_r1 = j1.jogarCarta(0)
    c2_r1 = j2.jogarCarta(0)
    vencedor1 = jogo.verificarCartaVencedora(c1_r1, c2_r1) # verifica vencedor
    assert vencedor1.retornarNumero() in [c1_r1.retornarNumero(), c2_r1.retornarNumero()] #checa se o numero da carta ganhadora corresponde

    c1_r2 = j1.jogarCarta(0)
    c2_r2 = j2.jogarCarta(0)
    vencedor2 = jogo.verificarCartaVencedora(c1_r2, c2_r2)
    assert vencedor2.retornarNumero() in [c1_r2.retornarNumero(), c2_r2.retornarNumero()]

    c1_r3 = j1.jogarCarta(0)
    c2_r3 = j2.jogarCarta(0)
    vencedor3 = jogo.verificarCartaVencedora(c1_r3, c2_r3)
    assert vencedor3.retornarNumero() in [c1_r3.retornarNumero(), c2_r3.retornarNumero()]