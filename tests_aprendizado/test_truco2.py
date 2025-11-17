import pytest
from Jogo.jogo import Jogo

def test_aceitar_truco():
    jogo = Jogo()
    jogo.truco['quemPediu'] = 1
    jogo.aceitar_pedido(quem=2, rodada=0, aceito=True)
    assert jogo.truco['aceito'] is True #teste passa

def test_recusar_truco():
    jogo = Jogo()
    jogo.truco['quemPediu'] = 1
    jogo.aceitar_pedido(quem=2, rodada=0, aceito=False) #nao aceita
    assert jogo.truco['aceito'] is True  #teste falha 
