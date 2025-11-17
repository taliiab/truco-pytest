# Truco Gaudério - Sistema em Python

## Descrição Geral do Sistema

O sistema será um jogo de Truco Gaudério digital, desenvolvido em Python, 
com modo **jogador vs jogador** e possibilidade de incluir modo **contra o computador**. 

O objetivo é atingir **15 ou 30 pontos** antes do adversário, seguindo
as regras tradicionais do Truco Gaudério.

------------------------------------------------------------------------

## Atores

### **Jogador 1**

Usuário que inicia a partida.

### **Jogador 2**

Adversário (outro jogador humano ou computador.

------------------------------------------------------------------------

## Casos de Uso

------------------------------------------------------------------------

### **UC01 -- Iniciar Jogo**

**Ator Principal:** Jogador 1\
**Objetivo:** Começar uma nova partida.

**Fluxo Principal:** - O jogador escolhe iniciar um novo jogo. - O
sistema embaralha o baralho e distribui 3 cartas para cada jogador. - O
sistema define aleatoriamente quem inicia. - O jogo começa.

**Regras de Negócio:** RN01, RN02, RN03

------------------------------------------------------------------------

### **UC02 -- Jogar Carta**

**Ator Principal:** Jogador 1 ou Jogador 2\
**Objetivo:** Jogar uma carta válida.

**Fluxo Principal:** - O sistema informa de quem é a vez. - O jogador
escolhe uma carta válida. - O sistema exibe a carta jogada. - Quando
ambos jogam, o sistema compara as cartas. - O vencedor da rodada é
registrado.

**Regras de Negócio:** RN04, RN05, RN06

------------------------------------------------------------------------

### **UC03 -- Pedir Truco / Retruco / Vale Quatro**

**Ator Principal:** Jogador\
**Objetivo:** Aumentar a aposta da rodada.

**Fluxo Principal:** - O jogador pede "Truco". - O oponente escolhe:
aceitar, recusar ou aumentar. - O sistema aplica: - **Aceitou:** aumenta
o valor da mão. - **Recusou:** quem pediu ganha os pontos. -
**Aumentou:** o outro jogador decide novamente.

**Regras de Negócio:** RN07, RN08, RN09, RN10

------------------------------------------------------------------------

### **UC04 -- Contar Pontos**

**Ator Principal:** Sistema\
**Objetivo:** Atualizar pontuação após a mão.

**Fluxo Principal:** - O sistema soma os pontos após cada mão. -
Verifica se algum jogador atingiu 15 ou 30 pontos. - Se sim, declara o
vencedor.

**Regras de Negócio:** RN11, RN12

------------------------------------------------------------------------

### **UC05 -- Envido e Flor**

**Ator Principal:** Jogador\
**Objetivo:** Jogar Envido ou Flor.

**Fluxo Principal:** - O jogador anuncia "Envido" ou "Flor". - O sistema
calcula os pontos conforme as cartas. - O oponente aceita ou recusa. - O
vencedor recebe a pontuação correspondente.

**Regras de Negócio:** RN13, RN14, RN15

------------------------------------------------------------------------

### **UC06 -- Finalizar Partida**

**Ator Principal:** Sistema\
**Objetivo:** Encerrar o jogo.

**Fluxo Principal:** - O sistema detecta que um jogador atingiu 15 ou 30
pontos. - Exibe o vencedor. - Oferece reiniciar ou sair.

**Regras de Negócio:** RN12

------------------------------------------------------------------------

## Regras de Negócio (RN)

### **RN01** -- Baralho com 40 cartas (sem 8 e 9).

### **RN02** -- Hierarquia das cartas:

1 \> 7 (ouro, espada) \> 3 \> 2 \> 12 \> 11 \> 10 \> 7 (pau, copa) \> 6
\> 5 \> 4

### **RN03** -- Cada jogador recebe 3 cartas.

### **RN04** -- Carta maior vence a rodada.

### **RN05** -- Quem vence 2 rodadas ganha a mão.

### **RN06** -- Empate: vence quem for "mão".

### **RN07** -- Truco vale 2 pontos; retruco 3; vale quatro 4.

### **RN08** -- Recusar dá pontos do nível anterior ao adversário.

### **RN09** -- Só pode pedir retruco se tiver aceitado truco antes.

### **RN10** -- Não pode pedir truco novamente após recusar.

### **RN11** -- Pontuação máxima: 15 ou 30.

### **RN12** -- Ao atingir 15 ou 30, o jogo termina automaticamente.

### **RN13** -- Envido é jogado antes da primeira rodada.

### **RN14** -- Flor só pode ser anunciada com 3 cartas do mesmo naipe.

### **RN15** -- Pontuação do Envido / Flor:

-   Soma das cartas do mesmo naipe + 10 pontos por carta.
-   Número da carta também soma (ex: 1 = 10 + 1, 2 = 10 + 2).
-   Cartas 10, 11, 12 somam apenas +10.

