from cdp.CriaLabirinto import Labirinto
from cci.ControlaPlayer import *
from cih.ImprimeJogo import *

class JogoLabirinto:
    timer = 0

    def __init__(self):

        self.i=0
        self.labirinto=Labirinto(10,10) # gera o labirinto
        self.lst=self.labirinto.desenhaLabirinto(0,0) # gera uma lista com (posicao do blocos,gramas,player,saida)

        self.player = pygame.Rect(self.lst[2][0],self.lst[2][1],16,28) # paralelepipedo do tamanho do player

        self.gramas=self.lst[1] # lista com as posicoes das gramas
        self.blocos = self.lst[0] # lista com as posicoes dos blocos

        self.saida = pygame.Rect(self.lst[3][0],self.lst[3][1],30,30) #localizacao saida

        self.controlePlayer=ControlaPlayer()
        self.imprimiJogo=ImprimiJogo()

        return

    def atualizaTempo(self,controle): # atualiza o timer
        self.i+=1
        if self.i>=15:
            controle.tempoTotal +=1
            self.i=0
        return


    def mostraJogo(self, controle):

        self.atualizaTempo(controle) # Metodo para atualiza o tempo
        self.player=self.controlePlayer.controladorPlayer(controle,self.player,self.blocos,self.saida) # Metodo para controlar o deslocamento do player
        self.imprimiJogo.imprimirJanela(controle,self.gramas,self.blocos,self.player,self.saida) # Metodo para impressao da Janela do Jogo

        pygame.display.update()

        return

