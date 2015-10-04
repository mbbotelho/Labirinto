__author__ = 'Michelle_Douglas'

import pygame,sys,os,time,math,random
from pygame.locals import *
from Visao.JanelaMenuInicial import JanelaMenuInicial
from Modelo.Jogo import Jogo
from Visao.JanelaCreditos import JanelaCreditos
from Visao.JanelaFinalJogo import JanelaFinalJogo

class Controle:

    def __init__(self):
        self.opcao = 1
        self.mainClock = pygame.time.Clock()
        self.tempoTotal =0
        width,height = 632,632
        self.screen = pygame.display.set_mode((width,height)) #cria janela
        pygame.display.set_caption('Labirinto do Capeta')
        self.menu = JanelaMenuInicial() # instacia a janela de menu
        self.jogo = Jogo() # instacia jogo
        self.creditos = JanelaCreditos() #instancia a janela de credito
        self.finaljogo = JanelaFinalJogo() # instancia a janela de final do jogo
                     #cima  #baixo #esqu  #dire  #esc         #espaco
        self.keys = [False, False, False, False, False, False,False]


    def controla(self):# controla os eventos das janelas
        pygame.init()

        while self.opcao != 3:
            self.capturaEventos()

            if self.opcao == 1:
                self.menu.mostraMenu(self) # exibi o menu do jogo

            elif self.opcao == 2:
                self.jogo.mostraJogo(self) # chama o controlador do jogo

            elif self.opcao == 4:
                self.creditos.mostraCreditos(self) # exibi os creditos

            elif self.opcao == 5:
                self.finaljogo.mostraMenuFinalJogo(self) # exibe a tela final do jogo

            self.mainClock.tick(15)

        pygame.quit()
        sys.exit() # para sair de uma forma mais suave

    def capturaEventos(self): #captura os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.opcao = 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.keys[0] = True
                if event.key == pygame.K_DOWN:
                    self.keys[1] = True
                if event.key == pygame.K_LEFT:
                    self.keys[2] = True
                if event.key == pygame.K_RIGHT:
                    self.keys[3] = True
                if event.key == pygame.K_ESCAPE:
                    self.keys[4] = True
                if event.key == pygame.K_SPACE:
                    self.keys[6] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.keys[0] = False
                if event.key == pygame.K_DOWN:
                    self.keys[1] = False
                if event.key == pygame.K_LEFT:
                    self.keys[2] = False
                if event.key == pygame.K_RIGHT:
                    self.keys[3] = False
                if event.key == pygame.K_ESCAPE:
                    self.keys[4] = False
                if event.key == pygame.K_SPACE:
                    self.keys[6] = False
