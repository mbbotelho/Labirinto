__author__ = 'Michelle_Douglas'
import pygame,sys,os,time,math,random
from pygame.locals import *

class Bloco (object):
      pygame.init()
      def __init__(self):
        self.blocoimage=pygame.image.load(os.path.join("imagens","bloco.png"))# carrega a imagem
        self.blocoimagem = pygame.transform.scale(self.blocoimage,(30,30)) # redimensiona a imagem


      def imprime(self,janela,posicao): # imprime a imagem na tela
          janela.blit(self.blocoimagem,posicao)