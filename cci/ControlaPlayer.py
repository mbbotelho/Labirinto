__author__ = 'Douglas'
class ControlaPlayer:
    def __init__(self):
        self.speed = 10 # quanto de deslocamento recebera (simula a velocidade)

    def controladorPlayer(self,controle,player,blocos,saida): # funcao que controla o deslocamento do player e suas colisoes

        self.blocos=blocos
        self.player=player
        self.saida=saida

        if controle.evento.keys[0]: # verifica se a tecla pressionada foi UP
            if self.player.top>=0 : # verifica se a parte superior do personagem e maior(mais para baixo) da tela superior
                dy=self.player[1] # guarda a posicao atual do personagem
                self.player[1]-=self.speed # adiciona speed a posicao do personagem
                for bloco in self.blocos[:]: # verifica para cada bloco
                    if self.player.colliderect(bloco): # se o personagem ira colidir, caso receba a nova posicao
                        self.player[1]=dy # se o personagem colidir com algum bloco, personagem recebera a posicao guardada

        elif controle.evento.keys[1]:
            if self.player.bottom<=931 :
                dy=self.player[1]
                self.player[1]+=self.speed
                for bloco in self.blocos[:]:
                    if self.player.colliderect(bloco):
                        self.player[1]=dy
        elif controle.evento.keys[2]:
            if self.player.left>=0:
                dx=self.player[0]
                self.player[0]-=self.speed
                for bloco in self.blocos[:]:
                    if self.player.colliderect(bloco):
                        self.player[0]=dx
        elif controle.evento.keys[3]:
            if self.player.right<=931 :
                dx=self.player[0]
                self.player[0]+=self.speed
                for bloco in self.blocos[:]:
                    if self.player.colliderect(bloco):
                        self.player[0]=dx

        elif self.player.colliderect(saida): # se chegar a saida, altera a opcao do loop principal
            controle.screen.fill(0) # limpa a tela
            controle.opcao=5

        return self.player



