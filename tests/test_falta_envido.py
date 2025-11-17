import pytest
from Jogo.jogo import Jogo
from Jogo.baralho import Baralho
from Jogo.jogador import Jogador
from Jogo.carta import Carta

def test_falta_envido():
    baralho = Baralho()
    jogo = Jogo()

    j1 = jogo.criarJogador("Alice", baralho) #cria jogador 1
    j2 = jogo.criarJogador("Carlos", baralho) #cria jogador 2

    j1.mao = [Carta(7, "COPAS"), Carta(6, "COPAS"), Carta(1, "BASTOS")]
    j2.mao = [Carta(5, "ESPADAS"), Carta(4, "BASTOS"), Carta(3, "OUROS")]

    jogo.falta_envido['chamador'] = j1 # Alice chama falta envido
    jogo.falta_envido['pendente'] = True

    j2.opcao_atual = "Aceitar Falta Envido"
    if jogo.falta_envido['pendente'] and j2.opcao_atual == "Aceitar Falta Envido": #Carlos aceita falta envido
        jogo.falta_envido['aceito'] = True
        jogo.falta_envido['pendente'] = False

    # calcula os pontos
    pontos_j1 = jogo.retornarPontosEnvido(j1.mao)
    pontos_j2 = jogo.retornarPontosEnvido(j2.mao)

    #define ganhador
    vencedor = j1 if pontos_j1 > pontos_j2 else j2

    assert jogo.falta_envido['aceito'] is True, "Falta Envido deveria ter sido aceita"
    assert vencedor == j1, "Alice deveria vencer a Falta Envido"
