__author__ = 'Douglas'

import pygame
pygame.init()

class Eventos:
    def __init__(self):
                     #cima  #baixo #esqu  #dire  #esc         #espaco
        self.keys = [False, False, False, False, False, False,False]  # lista com as teclas setadas por padrao como falso

    def capturaEventos(self):

        for event in pygame.event.get(): # para cada evento possivel (o pygame verifica todas a interrupcoes possiveis)

            if event.type == pygame.QUIT: # verifica qual o tipo de evento
                self.opcao = 0
            if event.type == pygame.KEYDOWN: # se evento for do tipo tecla pressionada
                if event.key == pygame.K_UP:
                    self.keys[0] = True
                if event.key == pygame.K_DOWN: # verifica qual a tecla pressionada
                    self.keys[1] = True
                if event.key == pygame.K_LEFT:
                    self.keys[2] = True         # seta na lista de teclas o estado True
                if event.key == pygame.K_RIGHT:
                    self.keys[3] = True
                if event.key == pygame.K_ESCAPE:
                    self.keys[4] = True
                if event.key == pygame.K_SPACE:
                    self.keys[6] = True

            if event.type == pygame.KEYUP: # se evento for do tipo tecla nao pressionada
                if event.key == pygame.K_UP:
                    self.keys[0] = False
                if event.key == pygame.K_DOWN: # verifica qual a tecla nao pressionada
                    self.keys[1] = False
                if event.key == pygame.K_LEFT:
                    self.keys[2] = False         # seta na lista de teclas o estado False
                if event.key == pygame.K_RIGHT:
                    self.keys[3] = False
                if event.key == pygame.K_ESCAPE:
                    self.keys[4] = False
                if event.key == pygame.K_SPACE:
                    self.keys[6] = False
