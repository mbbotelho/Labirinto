__author__ = 'Douglas'
from cih.ImprimeMenu import *


class MenuLabirinto:
    def __init__(self):
                     #Backg  #Jogar   #Credito   #Sair    #Cursor
        self.posicao=[(0,0),(230,150),(230,250),(230,350),[90,150]] # Lista com as posicoes dos botoes
        self.imprimirMenu=ImprimeMenu()
        return

    def mostraMenu(self, controle):

        if controle.evento.keys[0]: # se a tecla up for pressionada
            if self.posicao[4][1] > self.posicao[1][1]: # se a posicao do cursor for maior que a altura do primeiro icone (no caso o botao jogar)
                self.posicao[4][1]-=100 # a posicao do cursor decrementada em uma quantidade (no caso 100 unidades)

        if controle.evento.keys[1]: # se a tecla down for pressionada
            if self.posicao[4][1] < self.posicao[3][1]: # se a posicao do cursor for menor que a altura do ultimo icone (no caso o botao sair)
                self.posicao[4][1]+=100 # a posicao do cursor e incrementada em uma quantidade (no caso 100 unidades)

        if controle.evento.keys[6]: # se a tecla Space for pressionada
            if self.posicao[4][1]==self.posicao[1][1]: # se a posicao altura do cursor for a mesma que o botao jogar
                controle.opcao = 2 # seta opcao correspondente no loop principal (controle)

            if self.posicao[4][1]==self.posicao[2][1]: # se a posicao altura do cursor for a mesma que o botao creditos
                controle.numero = 0 # artimanha para avisar o menu creditos para onde voltar caso pressione ESC (0 para menuInicial, 1 para menuFinal)
                controle.opcao = 4 # seta opcao correspondente no loop principal (controle)

            if self.posicao[4][1]==self.posicao[3][1]: # se a posicao altura do cursor for a mesma que o botao sair
                controle.opcao = 0 # seta opcao correspondente no loop principal (controle)

        if controle.evento.keys[4]: # se a tecla pressionada for ESC
            controle.opcao = 0 # seta opcao correspondente no loop principal (controle)

        self.imprimirMenu.imprimiJanelaMenu(controle,self.posicao)

        pygame.display.update() # atualiza a tela

