import pytest
from Jogo.jogo import Jogo
from Jogo.baralho import Baralho
from Jogo.carta import Carta

def test_envido():
    baralho = Baralho()
    jogo = Jogo()
    
    jogador = jogo.criarJogador("Ana", baralho)  
    
    jogador.mao = [Carta(1, "ESPADAS"), Carta(7, "COPAS"), Carta(5, "BASTOS")] # cria a mão do jogador
    
    pontos_envido = jogo.retornarPontosEnvido(jogador.mao) # calcula envido
    
    assert pontos_envido == 7 #verifica resultado 
