__author__ = 'Douglas'
from cih.ImprimeNivel import *
import pygame


class MenuNiveis:
    def __init__(self):
                     #Backg  #Facil   #Medio   #Dificil    #Cursor
        self.posicao=[(0,0),(230,150),(230,250),(230,350),[90,150]]
        self.imprimiNivel=ImprimeNivel()
        return

    def mostraMenuNiveis(self, controle):

        if controle.evento.keys[0]:
            if self.posicao[4][1] > 150:
                self.posicao[4][1]-=100

        if controle.evento.keys[1]:
            if self.posicao[4][1] < 350:
                self.posicao[4][1]+=100

        if controle.evento.keys[6]:
            if self.posicao[4][1]==150:
                controle.opcao = 3

            if self.posicao[4][1]==250:
                controle.opcao = 3

            if self.posicao[4][1]==350:
                controle.opcao = 3

        if controle.evento.keys[4]:
            controle.opcao = 0

        self.imprimiNivel.imprimiJanelaNivel(controle,self.posicao)


        pygame.display.update()
