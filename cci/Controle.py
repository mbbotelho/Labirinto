import pygame,sys,os,time,math,random
from pygame.locals import *
from cci.ControleMenu import MenuLabirinto
from cdp.JogoLabirinto import JogoLabirinto
from cci.ControleCreditos import Creditos
from cci.ControleFinalJogo import FinalJogo
from cci.ControleNiveis import *
from cci.ControleEventos import Eventos

class Controle:

    def __init__(self):
        self.opcao = 1
        self.mainClock = pygame.time.Clock()
        self.tempoTotal = 0
        self.width,self.height = 632,632
        self.screen = pygame.display.set_mode((self.width,self.height))

    def controla(self):
        pygame.init()
        pygame.display.set_caption('Labirinto do Capeta')
        self.numero = 0
        self.evento = Eventos()
        self.menu = MenuLabirinto()
        self.jogo = JogoLabirinto()
        self.creditos = Creditos()
        self.finaljogo = FinalJogo()
        self.niveis = MenuNiveis()

        while self.opcao != 0:
            self.evento.capturaEventos()

            if self.opcao == 1:
                self.menu.mostraMenu(self)

            elif self.opcao == 2:
                self.niveis.mostraMenuNiveis(self)

            elif self.opcao == 3:
                self.jogo.mostraJogo(self)

            elif self.opcao == 4:
                self.creditos.mostraCreditos(self.numero,self)

            elif self.opcao == 5:
                self.finaljogo.mostraMenuFinalJogo(self)

            self.mainClock.tick(15)

        pygame.quit()
        sys.exit() # para sair de uma forma mais suave

