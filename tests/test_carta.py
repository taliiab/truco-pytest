import pytest
from Jogo.carta import Carta
from Jogo.pontos import MANILHA, CARTAS_VALORES

#MOCKS - objetos predefinidos

def create_card(numero, naipe):
    return Carta(numero, naipe.upper())

c_aux = Carta(1, 'ESPADAS') #auxiliar maior carta
CARTA_1E = create_card(1, 'Espadas') 
CARTA_7O = create_card(7, 'Ouros')
CARTA_4C = create_card(4, 'Copas')
CARTA_5B = create_card(5, 'Bastos')
CARTA_5C = create_card(5, 'Copas')
CARTA_5E = create_card(5, 'Espadas')
CARTA_3O = create_card(3, 'Ouros')

# método __eq__ para comparar naipe e numero
def compare_cards(c_actual, c_expected):
    return c_actual.retornarNumero() == c_expected.retornarNumero() and c_actual.retornarNaipe() == c_expected.retornarNaipe()

class TestCarta:
    @pytest.mark.parametrize("c1, c2, esperado_alta, esperado_baixa", [ #mesmo teste com varios valores
        (CARTA_1E, CARTA_7O, CARTA_1E, CARTA_7O),       
        (CARTA_7O, CARTA_3O, CARTA_7O, CARTA_3O),       
        (CARTA_4C, create_card(7, 'Espadas'), create_card(7, 'Espadas'), CARTA_4C), 
        (CARTA_3O, CARTA_5B, CARTA_3O, CARTA_5B),       
        (CARTA_5B, CARTA_3O, CARTA_3O, CARTA_5B),       
        (CARTA_5B, create_card(5, 'Espadas'), create_card(5, 'Espadas'), create_card(5, 'Espadas')),
        (CARTA_1E, CARTA_4C, CARTA_1E, CARTA_4C),       
        (CARTA_4C, CARTA_7O, CARTA_7O, CARTA_4C),       
    ])

    def test_verificar_cartas_alta_e_baixa(self, c1, c2, esperado_alta, esperado_baixa): #função auxiliar para comparar as cartas
        assert compare_cards(c_aux.verificarCartaAlta(c1, c2), esperado_alta)
        assert compare_cards(c_aux.verificarCartaBaixa(c1, c2), esperado_baixa)

    @pytest.mark.parametrize("carta, esperado", [
        (CARTA_1E, MANILHA['1 de ESPADAS']),   #verifica manilha
        (CARTA_4C, CARTAS_VALORES['4']),        #verifica carta
    ])
    def test_retornar_pontos_carta(self, carta, esperado):
        assert c_aux.retornarPontosCarta(carta) == esperado #verifica os pontos da carta (manilha ou valor)

    @pytest.mark.parametrize("cartas, esperado_classificacao", [
        ([CARTA_3O, CARTA_5B, CARTA_4C], ['Alta', 'Media', 'Baixa']), 
        ([CARTA_1E, CARTA_7O, CARTA_4C], ['Alta', 'Media', 'Baixa']), 
        ([CARTA_5B, CARTA_5C, CARTA_5E], ['Media', 'Media', 'Baixa']), 
        ([CARTA_5B, CARTA_4C, CARTA_5C], ['Media', 'Baixa', 'Alta']), 
    ])
    def test_classificar_carta(self, cartas, esperado_classificacao): #veerifica classificação
        _, classificacao_obtida = c_aux.classificarCarta(cartas)
        assert classificacao_obtida == esperado_classificacao
        
    def test_printar_carta_especiais(self, capsys):
        CARTA_1E.printarCarta(0)
        out, _ = capsys.readouterr()
        assert '1 de ESPADAS' in out.strip() or 'ESPADÃO' in out.strip()
        
    def test_printar_carta_comum(self, capsys):
        CARTA_4C.printarCarta() 
        out, _ = capsys.readouterr()
        assert '4 de COPAS' in out.strip()

    def test_retornar_numero_naipe(self):
        assert CARTA_4C.retornarNumero() == 4 
        assert CARTA_4C.retornarNaipe() == 'COPAS' 

    def test_carta_verificar_manilha_mais_alta(self):        
        carta_1e = create_card(1, 'Espadas') 
        carta_1b = create_card(1, 'Bastos')  
        carta_3c = create_card(3, 'Copas')

        vencedora_manilha = carta_1e.verificarCartaAlta(carta_1e, carta_1b) #verifca carta vencedora
        assert vencedora_manilha.numero == 1 and vencedora_manilha.naipe == 'ESPADAS'

        vencedora_normal = carta_1e.verificarCartaAlta(carta_1e, carta_3c)
        assert vencedora_normal.numero == 1 and vencedora_normal.naipe == 'ESPADAS'

        vencedora_manilha_normal = carta_1b.verificarCartaAlta(carta_1b, carta_3c)
        assert vencedora_manilha_normal.numero == 1 and vencedora_manilha_normal.naipe == 'BASTOS'