def test_truco():
    from Jogo.jogo import Jogo
    jogo = Jogo()
    rodada_atual = 1

    jogo.truco['quemPediu'] = 1 #jogador 1 pediu truco
    aceito = jogo.aceitar_pedido(quem=2, rodada=rodada_atual, aceito=True) #jogador 2 aceitou

    assert aceito is True
    assert jogo.truco['aceito'] is True
    assert jogo.truco['quandoPediu'] == rodada_atual #rodada que o truco foi pedido
