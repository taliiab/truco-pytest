import pytest
from Jogo.jogador import Jogador
from Jogo.baralho import Baralho
from Jogo.carta import Carta

def create_card(numero, naipe):
    return Carta(numero, naipe.upper())

CARTA_1E = create_card(1, 'Espadas') 
CARTA_7O = create_card(7, 'Ouros')
CARTA_4C = create_card(4, 'Copas')

class TestJogador:
    
    def setup_method(self):
        self.baralho = Baralho()
        self.jogador = Jogador("Teste")
        self.jogador.mao = [CARTA_1E, CARTA_7O, CARTA_4C] 

    def test_criar_mao_tamanho(self):
        jogador_novo = Jogador("Novo")
        jogador_novo.criarMao(self.baralho)
        assert len(jogador_novo.mao) == 3 

    def test_jogar_carta(self):
        carta_jogada = self.jogador.jogarCarta(1) 
        assert len(self.jogador.mao) == 2 
        assert carta_jogada == CARTA_7O

    def test_checa_flor_verdadeiro(self):
        self.jogador.mao = [CARTA_4C, create_card(5, 'Copas'), create_card(1, 'Copas')]
        assert self.jogador.checaFlor() is True 

    def test_checa_flor_falso(self):
        assert self.jogador.checaFlor() is False 

    def test_resetar(self):
        self.jogador.resetar() #reseta a mao
        assert self.jogador.mao == [] #verifca se esta vazio

    def test_mostrar_opcoes_cenarios(self, capsys):
        self.jogador.mostrarOpcoes() 
        out, _ = capsys.readouterr()
        assert '[4] Truco' in out
        assert '[5] Envido' in out
        
        self.jogador.pediuTruco = True
        self.jogador.mostrarOpcoes() 
        out, _ = capsys.readouterr()
        assert '[4] Truco' not in out
        
        self.jogador.mao = [CARTA_1E, CARTA_7O]
        self.jogador.mostrarOpcoes() 
        out, _ = capsys.readouterr()
        assert '[5] Envido' not in out
        
    def test_mostrar_opcoes_flor_controle(self, capsys):
        self.jogador.mao = [CARTA_4C, create_card(5, 'Copas'), create_card(1, 'Copas')]
        self.jogador.flor = False
        self.jogador.mostrarOpcoes() 
        out, _ = capsys.readouterr()
        assert '[5] Flor' in out
        
        self.jogador.mostrarOpcoes() 
        out_novo, _ = capsys.readouterr()
        assert '[5] Flor' not in out_novo

    def test_mostrar_mao_loop_check(self, capsys):
        self.jogador.mostrarMao()
        out, _ = capsys.readouterr()
        lines = out.strip().split('\n')
        assert len(lines) == 3 