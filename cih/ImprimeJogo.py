__author__ = 'Douglas'
from cdp.CriaImagensJogo import *

class ImprimiJogo:
    def __init__(self):

        self.fonte = pygame.font.SysFont("comicsansms",25)
        self.textoTempo = self.fonte.render("TIME: ",1,(255,255,255))
        self.playerImagem = Imagens("player").criaImagens((16,28)) # recebe as imagens a serem imprimidas
        self.gramaImagem = Imagens("grama").criaImagens((30,30))
        self.blocoImagem = Imagens("bloco").criaImagens((30,30))
        self.saidaImagem = Imagens("saida").criaImagens((30,30))

    def imprimirJanela(self,controle,gramas,blocos,player,saida):

        for grama in gramas: # printando as gramas
            controle.screen.blit(self.gramaImagem,grama)

        for bloco in blocos: # printando os blocos
            controle.screen.blit(self.blocoImagem,bloco)

        controle.screen.blit(self.playerImagem,player) # printar a tela (com player)

        controle.screen.blit(self.saidaImagem,saida) # printando a saida

        tempo_ = format("TIME: %d" % controle.tempoTotal )
        self.textoTempo = self.fonte.render(tempo_,1,(255,255,255))
        controle.screen.blit(self.textoTempo,(250,-2))