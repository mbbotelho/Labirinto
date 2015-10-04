__author__ = 'Michelle_Douglas'
import pygame,sys,os,time,math,random
from pygame.locals import *


class Personagem () :

    def __init__(self,localizacaoInicial): #localizacaoIniial[eixoX,eixoY]
        pygame.init ()
        self.tamanho=[16,28] # tamanho=[largura,altura] no momento esta padrao guarda as tamanho do personagem
        self.__localizacaoAtual=localizacaoInicial # guarda a localizacao atual do personagem
        self.player = pygame.Rect(self.getlocalizacaoAtual()[0],self.getlocalizacaoAtual()[1],self.tamanho[0],self.tamanho[1]) # paralelepipedo do tamanho do player
        self.playerImagem = pygame.image.load(os.path.join("imagens","mario.png")) # carrega a imagem do personagem
        self.playerImagem = pygame.transform.scale(self.playerImagem,(16,28)) #se quiser redimensionar

    def setlocalizacaoAtual(self,lstNovaLocalizacao):
        self.__localizacaoAtual = lstNovaLocalizacao
        self.player = pygame.Rect(self.getlocalizacaoAtual()[0],self.getlocalizacaoAtual()[1],self.tamanho[0],self.tamanho[1]) # paralelepipedo do tamanho do player


    def getlocalizacaoAtual(self):
        return self.__localizacaoAtual


    def imprime(self,janela):# imprime a imagem na janela
        janela.blit(self.playerImagem,self.player)

