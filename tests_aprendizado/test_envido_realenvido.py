import pytest
from Jogo.jogo import Jogo
from Jogo.baralho import Baralho
from Jogo.jogador import Jogador
from Jogo.carta import Carta

def test_envido_real_envido():
    baralho = Baralho()
    jogo = Jogo()

    j1 = jogo.criarJogador("Alice", baralho)
    j2 = jogo.criarJogador("Maria", baralho)

    j1.mao = [Carta(7, "COPAS"), Carta(3, "COPAS"), Carta(5, "BASTOS")]

    j2.mao = [Carta(6, "ESPADAS"), Carta(2, "COPAS"), Carta(1, "OUROS")]

    jogo.envido['quemPediu'] = 1  #Alice chama envido 
    jogo.aceitar_pedido(quem=2, rodada=0, aceito=True)  # Ana aceita

    jogo.real_envido['quemPediu'] = 2  # Ana pede real envido
    jogo.aceitar_pedido(quem=1, rodada=0, aceito=True)  # Alice aceita

    pontos_j1_re = jogo.retornarPontosEnvido(j1.mao) #pontos Alice
    pontos_j2_re = jogo.retornarPontosEnvido(j2.mao) #pontos Ana

    assert pontos_j1_re == 30
    assert pontos_j2_re == 6

    assert jogo.envido['aceito'] is True
    assert jogo.real_envido['aceito'] is True
