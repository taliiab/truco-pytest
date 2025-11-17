import pytest
from Jogo.baralho import Baralho
from Jogo.carta import Carta

class TestBaralho:
    
    def setup_method(self):
        self.baralho = Baralho() #cria baralho

    def test_criar_baralho_tamanho_e_ausencia(self):
        assert len(self.baralho.cartas) == 40 #verifica quantidade de cartas
        cartas_presentes = [c.numero for c in self.baralho.cartas] #lisa de cartas
        assert 8 not in cartas_presentes and 9 not in cartas_presentes #verificar a existencia das cartas de valor 8 e 9

    def test_embaralhar_ordem(self):
        cartas_antes = [str(c.numero) + c.naipe for c in self.baralho.cartas] #lista antes de embaralhar
        self.baralho.embaralhar() #embaralahmento
        cartas_depois = [str(c.numero) + c.naipe for c in self.baralho.cartas] #lista depois de embaralhar
        assert cartas_antes != cartas_depois #verifca se embaralhou

    def test_retirar_carta(self):
        carta_retirada = self.baralho.retirarCarta() #retira carta
        assert len(self.baralho.cartas) == 39 #verifica se retirou
        assert isinstance(carta_retirada, Carta) 

    def test_resetar_baralho(self):
        self.baralho.retirarCarta()
        self.baralho.resetarBaralho() #limpa a lista de cartas
        assert len(self.baralho.cartas) == 0 #verifica o reset
        
    def test_inicializacao_de_listas(self):
        assert len(self.baralho.cartas) == 40 #verifica tamanho
        assert self.baralho.manilhas == [] # verifica manilhas

    def test_printar_baralho_vazio(self, capsys):
        self.baralho.resetarBaralho() #reseta lista do baralho
        self.baralho.printarBaralho() #verifica se esta vario
        out, _ = capsys.readouterr()
        assert out == "" #verifica se esta vario

    def test_printar_baralho_completo(self, capsys):
        self.baralho.printarBaralho() 
        out, _ = capsys.readouterr()
        assert len(out.strip().split('\n')) == 40 #verica se tem 40 cartas