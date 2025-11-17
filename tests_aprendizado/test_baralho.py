import pytest
from Jogo.baralho import Baralho

def test_baralho_tem_40_cartas():
    baralho = Baralho()
    cartas = baralho.cartas  # atributo
    assert len(cartas) == 40  # verificação

def test_baralho_embaralha():
    baralho = Baralho()
    c1 = baralho.cartas.copy()  # estado inicial
    baralho.embaralhar()
    c2 = baralho.cartas # estado apos embaralhar 
    assert c1 != c2  # verifica se embaralhou
