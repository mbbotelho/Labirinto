__author__ = 'Michelle_Douglas'

import pygame,sys,os,time,math,random
from pygame.locals import *

class Moita (object):
      pygame.init()
      def __init__(self):
        self.moitaImage=pygame.image.load(os.path.join("imagens","mato1.png")) # carrega a imagem
        self.moitaImagem = pygame.transform.scale(self.moitaImage,(30,30)) # redimensiona a imagem


      def imprime(self,janela,posicao): #imprime a imagem na janela
          janela.blit(self.moitaImagem,posicao)
