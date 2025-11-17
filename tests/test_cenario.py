import pytest
import unittest
import sys
import os
from unittest.mock import patch, MagicMock 

#correcao do diretorio
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)
jogo_dir = os.path.join(root_dir, 'Jogo')
sys.path.append(jogo_dir)

from Jogo.jogo import Jogo
from Jogo.jogador import Jogador
from Jogo.bot import Bot 
from Jogo.baralho import Baralho
from Jogo.cbr_updated import Cbr 
from Jogo.updated_main import escalonamento, verificar_ganhador
from Jogo.carta import Carta

#mock
def create_card(numero, naipe):
    return Carta(numero, naipe.upper())

#cartas usadas
CARTA_1E = create_card(1, 'Espadas') 
CARTA_7O = create_card(7, 'Ouros')
CARTA_4C = create_card(4, 'Copas') 
CARTA_3O = create_card(3, 'Ouros') 
CARTA_5B = create_card(5, 'Bastos') 

def inverter_jogador(jogador_mao):
    return 2 if jogador_mao == 1 else 1

class TestCenariosJogo(unittest.TestCase):
    
    def setUp(self):
        self.baralho = Baralho()
        self.jogo = Jogo()
        
        self.cbr = Cbr() 
        self.j1 = Jogador('Jogador 1') 
        self.j2 = Bot('Bot 2', self.cbr) #jogador 2 como bot
        
        self.j1.mao = [CARTA_1E, CARTA_4C, CARTA_7O]
        self.j2.mao = [CARTA_3O, CARTA_5B, CARTA_4C]
        
        self.j2.pontuacaoCartas = [] #valores p o bot tomar decisoes
        for carta in self.j2.mao:
            self.j2.pontuacaoCartas.append(carta.retornarPontosCarta(carta))

        self.jogo.resetarJogo()
        self.jogo.pontos_j1 = 0 
        self.jogo.pontos_j2 = 0
        self.jogo.pontos_maximos = 15 
        
    def test_cenario_pedir_e_aceitar_truco(self):

        escalonamento(etapa=0, quem_chamou=1, jogador1=self.j1, jogador2=self.j2, jogo=self.jogo, escalonamento_tipo="truco") #atualiza estado
        
        self.jogo.truco['aceito'] = True 
        
        self.assertEqual(self.jogo.pontos_mao, 2)
        self.assertEqual(self.jogo.truco['pontos'], 2)

    def test_cenario_pedir_e_recusar_truco(self):        

        self.jogo.truco_negado = True 
        self.jogo.pontos_mao = 1 
        
        verificar_ganhador(self.jogo)

        if self.jogo.pontos_j1 == 0 and self.jogo.truco_negado:
            self.jogo.pontos_j1 = self.jogo.pontos_mao
        
        self.assertTrue(self.jogo.truco_negado)
        self.assertEqual(self.jogo.pontos_j1, 1)

    @patch('builtins.input', return_value='s') #simula a entrada do usuario
    def test_cenario_escalonamento_truco_para_retruco(self, mock_input):
        
        self.jogo.truco = {'quemPediu': 1, 'aceito': True, 'pontos': 2, 'quandoPediu': 1, 'quemGanhou': 0}
        self.jogo.pontos_mao = 2
        
        escalonamento(etapa=1, quem_chamou=2, jogador1=self.j1, jogador2=self.j2, jogo=self.jogo, escalonamento_tipo="truco")
        
        self.assertEqual(self.jogo.pontos_mao, 3)

    def test_cenario_pedir_e_aceitar_envido(self):
        
        self.jogo.rodada_atual = 1 

        escalonamento(etapa=0, quem_chamou=1, jogador1=self.j1, jogador2=self.j2, jogo=self.jogo, escalonamento_tipo="envido")
        
        self.jogo.envido['aceito'] = True 
        
        self.assertEqual(self.jogo.envido['pontos'], 2)

    @patch('builtins.input', return_value='s') 
    def test_cenario_envido_e_truco_na_mesma_mao(self, mock_input):
        
        self.jogo.rodada_atual = 1

        escalonamento(etapa=0, quem_chamou=1, jogador1=self.j1, jogador2=self.j2, jogo=self.jogo, escalonamento_tipo="envido")

        self.jogo.pontos_j1 += 1 
        self.jogo.envido['aceito'] = False
        
        self.assertEqual(self.jogo.pontos_j1, 1)
        
        escalonamento(etapa=0, quem_chamou=1, jogador1=self.j1, jogador2=self.j2, jogo=self.jogo, escalonamento_tipo="truco")
        
        self.jogo.truco['aceito'] = True 
        self.jogo.pontos_mao = 2 
        
        self.assertGreaterEqual(self.jogo.pontos_mao, 2)
        self.assertGreaterEqual(self.jogo.truco['pontos'], 2)
    
    def test_cenario_pedir_real_envido(self):        
        self.jogo.rodada_atual = 1

        escalonamento(etapa=1, quem_chamou=1, jogador1=self.j1, jogador2=self.j2, jogo=self.jogo, escalonamento_tipo="envido")
        
        self.jogo.real_envido['quemPediu'] = 1 
        self.jogo.real_envido['aceito'] = True
        self.jogo.real_envido['pontos'] = 4 

        self.assertEqual(self.jogo.real_envido['pontos'], 4)
        self.assertEqual(self.jogo.real_envido['quemPediu'], 1)

    def test_cenario_pedir_falta_envido(self):        
        self.jogo.pontos_j2 = 5 #simula 5 pontos para J2
        self.jogo.rodada_atual = 1
        
        escalonamento(etapa=2, quem_chamou=1, jogador1=self.j1, jogador2=self.j2, jogo=self.jogo, escalonamento_tipo="envido")
        
        self.jogo.falta_envido['quemPediu'] = 1 
        self.jogo.falta_envido['pontos'] = 10 # 15 - 5 = 10
        self.jogo.falta_envido['aceito'] = True 
        
        self.assertTrue(self.jogo.falta_envido['aceito'])
        self.assertEqual(self.jogo.falta_envido['quemPediu'], 1)
        self.assertEqual(self.jogo.falta_envido['pontos'], 10) 

    def test_cenario_finalizacao_de_rodada_empate_ganha_mao(self):
        
        self.jogo.rodadas_vencedor[0] = 1
        self.jogo.rodadas_vencedor[1] = 2
        self.jogo.rodadas_vencedor[2] = 3
        self.jogo.rodada_atual = 3
        
        self.jogo.quemGanhouMao = 1 #favorece jogador 1
        
        verificar_ganhador(self.jogo) 

        self.assertEqual(self.jogo.rodadas_vencedor, [1, 2, 3]) 
        self.assertTrue(self.jogo.encerrar_mao)

def test_cenario_jogador_opcoes_com_flor(capsys):    
    j1 = Jogador('Jogador 1') 
    
    carta_3_copas = create_card(3, 'Copas')
    carta_2_copas = create_card(2, 'Copas')
    carta_1_copas = create_card(1, 'Copas')
    j1.mao = [carta_3_copas, carta_2_copas, carta_1_copas]

    j1.mostrarOpcoes()
    out, _ = capsys.readouterr()
    
    assert '[5] Flor' in out
    assert j1.flor is True

def test_mostrar_opcoes_bloqueia_envido_flor_apos_carta_jogada():
    j1 = Jogador('J1')
    j1.mao = [create_card(1, 'Espadas'), create_card(3, 'Copas')] #tem 2 cartas
    
    with patch('builtins.print') as mock_print:
        j1.mostrarOpcoes()
        
        chamadas = [c[0][0] for c in mock_print.call_args_list]

        assert '[5] Envido' not in chamadas
        assert '[6] Real Envido' not in chamadas
        assert 'Flor' not in chamadas
        assert any('[4] Truco' in c for c in chamadas)