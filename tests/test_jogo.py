import pytest
from Jogo.jogo import Jogo
from Jogo.jogador import Jogador
from Jogo.carta import Carta
from Jogo.pontos import MANILHA, CARTAS_VALORES, ENVIDO

def create_card(numero, naipe):
    return Carta(numero, naipe.upper())

CARTA_1E = create_card(1, 'Espadas') 
CARTA_7O = create_card(7, 'Ouros')
CARTA_5B = create_card(5, 'Bastos')
CARTA_3O = create_card(3, 'Ouros')
CARTA_4C = create_card(4, 'Copas')

class TestJogo:
    
    def setup_method(self):
        self.jogo = Jogo()
        self.j1 = Jogador("P1")
        self.j2 = Jogador("P2")

    def test_resetar_jogo_inicializacao(self):
        assert self.jogo.pontos_mao == 1 
        assert self.jogo.rodadas_vencedor == [0,0,0] 
        assert self.jogo.truco['pontos'] == 2 
        assert self.jogo.vale_quatro['pontos'] == 4 
        assert self.jogo.truco['aceito'] is None 

    @pytest.mark.parametrize("pedido_name, quem_pediu, aceito_status, esperado_status", [
        ('truco', 1, True, True),
        ('truco', 1, False, False), 
        ('retruco', 2, True, True),
        ('vale_quatro', 1, False, False), 
        ('envido', 1, True, True), 
        ('falta_envido', 2, False, False), 
        ('flor', 1, True, True), 
    ])
    def test_aceitar_pedidos_variados(self, pedido_name, quem_pediu, aceito_status, esperado_status):
        rec = getattr(self.jogo, pedido_name)
        rec['quemPediu'] = quem_pediu 
        self.jogo.aceitar_pedido(quem=3-quem_pediu, rodada=0, aceito=aceito_status) 
        assert rec['aceito'] == esperado_status

    @pytest.mark.parametrize("c1, c2, esperado", [
        (CARTA_3O, CARTA_5B, CARTA_3O),         
        (CARTA_5B, CARTA_3O, CARTA_3O),         
        (CARTA_5B, create_card(5, 'Espadas'), "Empate"), 
    ])
    def test_verificar_carta_vencedora(self, c1, c2, esperado):
        assert self.jogo.verificarCartaVencedora(c1, c2) == esperado

    @pytest.mark.parametrize("mao, esperado", [
        ([CARTA_3O, create_card(3, 'Bastos'), create_card(3, 'Espadas')], 3), 
        ([CARTA_7O, create_card(6, 'Ouros'), CARTA_4C], 33), 
        ([create_card(10, 'Espadas'), create_card(10, 'Copas'), CARTA_4C], 24), 
        ([CARTA_7O, CARTA_5B, CARTA_4C], 7), 
        ([create_card(10, 'Espadas'), create_card(11, 'Copas'), create_card(12, 'Bastos')], 0), 
        ([CARTA_7O, create_card(6, 'Ouros'), create_card(5, 'Ouros')], 33), 
    ])
    def test_retornar_pontos_envido_comb(self, mao, esperado):
        assert self.jogo.retornarPontosEnvido(mao) == esperado

    def test_trocar_jogador_mao(self):
        self.jogo.maoAtual = 1
        self.j1.primeiro = True
        self.j2.primeiro = False
        
        self.jogo.trocarJogadorMao(self.j1, self.j2) 
        assert self.jogo.maoAtual == 2
        
        self.jogo.trocarJogadorMao(self.j1, self.j2) 
        assert self.jogo.maoAtual == 1

    def test_envido_calculo_apenas_carta_alta_unica(self):
        jogo = Jogo()
        mao = [
            create_card(7, 'ESPADAS'), 
            create_card(5, 'COPAS'),   
            create_card(4, 'OUROS')    
        ]
    
        pontos = jogo.retornarPontosEnvido(mao)
        assert pontos == 7

def test_envido_calculo_tres_cartas_iguais_valor_zero():
    jogo = Jogo()
    mao = [
        create_card(10, 'ESPADAS'), 
        create_card(11, 'COPAS'),   
        create_card(12, 'OUROS')    
    ]
    
    pontos = jogo.retornarPontosEnvido(mao)
    assert pontos == 0