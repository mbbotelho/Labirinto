__author__ = 'Michelle_Douglas'
import pygame,sys,os,time,math,random
from pygame.locals import *

from Modelo.Labirinto import Labirinto
from Modelo.Personagem import Personagem
from Modelo.Bloco import Bloco
from Modelo.Moita import Moita

class Jogo(object):
    timer = 0
    def __init__(self):
        pygame.init ()
        timer=0
        self.i=0
        self.fonte = pygame.font.SysFont('comicsansms',25)
        self.textoTempo = self.fonte.render("TIME: ",1,(255,255,255))

        self.labirinto=Labirinto(10,10)
        self.lst=self.labirinto.desenhaLabirinto(0,0)
        self.personagem=Personagem(self.lst[2]);

        self.blocos=self.lst[0]
        self.moitas=self.lst[1]

        self.bloco=Bloco()
        self.moita=Moita()

        self.file_saida=os.path.join("imagens","saida.png")
        self.saidaimage = pygame.image.load(self.file_saida)
        self.saidaimagem = pygame.transform.scale(self.saidaimage,(30,30)) #para redimensionar
        self.saida = pygame.Rect(self.lst[3][0],self.lst[3][1],30,30) #localizacao saida


    def atualizaTempo(self, controle):
        self.i+=1
        if self.i>=15:
            controle.tempoTotal +=1
            self.i=0
        return


    def mostraJogo(self, controle):
        self.atualizaTempo(controle)
        speed = 10
        if controle.keys[0]:# verifica se colidiu para cima
            if self.personagem.player.top>=0 :
                dx= self.personagem.getlocalizacaoAtual()[0]
                dy= self.personagem.getlocalizacaoAtual()[1]
                self.personagem.setlocalizacaoAtual([dx,dy-speed])
                for bloco in self.blocos[:]:
                    if self.personagem.player.colliderect(bloco):
                          self.personagem.setlocalizacaoAtual([dx,dy])
        if controle.keys[1]:# verifica se colidiu para baixo
            if self.personagem.player.bottom<=931 :
                dx= self.personagem.getlocalizacaoAtual()[0]
                dy= self.personagem.getlocalizacaoAtual()[1]
                self.personagem.setlocalizacaoAtual([dx,dy+speed])
                for bloco in self.blocos[:]:
                    if self.personagem.player.colliderect(bloco):
                          self.personagem.setlocalizacaoAtual([dx,dy])
        if controle.keys[2]:# verifica se colidiu para esquerda
            if self.personagem.player.left>=0:
                dx= self.personagem.getlocalizacaoAtual()[0]
                dy= self.personagem.getlocalizacaoAtual()[1]
                self.personagem.setlocalizacaoAtual([dx-speed,dy])
                for bloco in self.blocos[:]:
                    if self.personagem.player.colliderect(bloco):
                          self.personagem.setlocalizacaoAtual([dx,dy])
        if controle.keys[3]:# verifica se colidiu para direita
            if self.personagem.player.right<=931 :
                dx= self.personagem.getlocalizacaoAtual()[0]
                dy= self.personagem.getlocalizacaoAtual()[1]
                self.personagem.setlocalizacaoAtual([dx+speed,dy])
                for bloco in self.blocos[:]:
                    if self.personagem.player.colliderect(bloco):
                          self.personagem.setlocalizacaoAtual([dx,dy])
        if self.personagem.player.colliderect(self.saida):
            controle.screen.fill(0)
            controle.opcao=5

        for m in self.moitas: # printando as moita
            self.moita.imprime(controle.screen,m)
        for b in self.blocos:
            self.bloco.imprime(controle.screen,b)


        self.personagem.imprime(controle.screen)#imprime o personagem

        controle.screen.blit(self.saidaimagem,self.saida)
        tempo_ = format("TIME: %d" % controle.tempoTotal )

        self.textoTempo = self.fonte.render(tempo_,1,(255,255,255))
        controle.screen.blit(self.textoTempo,(250,-2))

        pygame.display.update()

        return

