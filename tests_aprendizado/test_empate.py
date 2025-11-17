import pytest
from Jogo.jogo import Jogo
from Jogo.baralho import Baralho
from Jogo.jogador import Jogador
from Jogo.carta import Carta

def test_empate():
    baralho = Baralho()
    jogo = Jogo()
    j1 = jogo.criarJogador("Alice", baralho) # cria jogador 1
    j2 = jogo.criarJogador("Carlos", baralho) # cria joagor 2

    j1.mao = [Carta(2, "COPAS"), Carta(3, "BASTOS"), Carta(4, "ESPADAS")] # mao jogador 1
    j2.mao = [Carta(2, "ESPADAS"), Carta(3, "COPAS"), Carta(4, "BASTOS")]  # mao joador 2

    resultados = [] # lista com resultados
    for i in range(3):
        c1 = j1.jogarCarta(0)
        c2 = j2.jogarCarta(0)
        vencedor = jogo.verificarCartaVencedora(c1, c2) # determina ganhador da rodada
        resultados.append(vencedor) # salva na lista

    for i, vencedor in enumerate(resultados): # verifica cada resultado
        c1_num = j1.mao[i].retornarNumero() if i < len(j1.mao) else None
        c2_num = j2.mao[i].retornarNumero() if i < len(j2.mao) else None

        assert vencedor == 'Empate' or vencedor in [c1_num, c2_num] # verifica resultado válido
