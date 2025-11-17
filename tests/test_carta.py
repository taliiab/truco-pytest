import pytest
from Jogo.carta import Carta

def test_carta():
    carta = Carta(3, "ESPADAS") # cria carta
    
    assert carta.numero == 3 # verifica número
    assert carta.naipe == "ESPADAS" # verifica naipe
