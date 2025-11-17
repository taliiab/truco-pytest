# tests/test_jogo.py
import pytest
from Jogo.jogo import Jogo
from Jogo.baralho import Baralho

@pytest.fixture
def jogo():
    return Jogo()

@pytest.fixture
def baralho():
    return Baralho()

def test_criar_jogador(jogo, baralho):
    jogador = jogo.criarJogador("Alice", baralho)
    assert jogador.nome == "Alice"
    assert len(jogador.mao) == 3  

def test_criar_bot(jogo, baralho):
    bot = jogo.criarBot("Bot", baralho, cbr=None)
    assert bot.nome == "Bot"
    assert len(bot.mao) == 3

def test_pontos_envido(jogo, baralho):
    jogador = jogo.criarJogador("Alice", baralho)
    pontos = jogo.retornarPontosEnvido(jogador.mao) #calcula envido
    assert isinstance(pontos, int) #valor inteiro
    assert pontos >= 0 #valor positivo

def test_verificar_carta_vencedora(jogo, baralho):
    jogador = jogo.criarJogador("Alice", baralho)
    jogador2 = jogo.criarJogador("Ana", baralho)
    carta_vencedora = jogo.verificarCartaVencedora(jogador.mao[0], jogador2.mao[0])  #atribui o valor do vencedor
    assert carta_vencedora == jogador.mao[0] or carta_vencedora == jogador2.mao[0] or carta_vencedora == "Empate" #verifica ganhador ou se empatou

def test_trocar_jogador_mao(jogo, baralho):
    jogo.maoAtual = 1 #qual mao corresponde
    jogador1 = jogo.criarJogador("Alice", baralho)
    jogador2 = jogo.criarJogador("Ana", baralho)
    jogador1.primeiro = True #quem joga
    jogador2.primeiro = False

    jogo.trocarJogadorMao(jogador1, jogador2) 
    assert jogador1.primeiro is False
    assert jogador2.primeiro is True #quem joga
    assert jogo.maoAtual == 2 #qual mao corresponde
