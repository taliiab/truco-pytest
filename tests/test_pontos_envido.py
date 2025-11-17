def test_pontos_envido():
    from Jogo.jogo import Jogo
    from Jogo.carta import Carta
    jogo = Jogo()

    mao = [Carta(6, "ESPADAS"), Carta(5, "ESPADAS"), Carta(3, "ESPADAS")] #ideal seria chamar "FLOR"
    pontos = jogo.retornarPontosEnvido(mao) #retona os pontos do envido

    assert pontos == 20 + 6 + 5  #verifica resulatdo
