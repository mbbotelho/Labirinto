__author__ = 'Douglas'
from cdp.JogoLabirinto import *
from cdp.CriaBotoes import *

class ImprimeFinal:
    def __init__(self):
        self.jogarImagem = Botoes("novapartida").criaBotao()  # retorna a imagem do botao para a janela do final de jogo
        self.creditosImagem = Botoes("creditos").criaBotao()
        self.sairImagem = Botoes("sair").criaBotao()
        self.cursorImagem = Botoes("cursor").criaBotao()
        self.backImagem = pygame.image.load(os.path.join("imagens","backpequeno.png")) # retorna a imagem do background para a janela do final de jogo

        self.fonte = pygame.font.SysFont("comicsansms",80) # seleciona a fonte do texto
        self.textoTempo = self.fonte.render("TIME: ",1,(255,255,255)) # seta o texto

    def imprimirJanelaFinal(self,controle,posicao):
        controle.screen.blit(self.backImagem,posicao[0]) # imprimi a imagem do botao (imagem , posicao a se printada)
        controle.screen.blit(self.jogarImagem,posicao[1])
        controle.screen.blit(self.creditosImagem,posicao[2])
        controle.screen.blit(self.sairImagem,posicao[3])
        controle.screen.blit(self.cursorImagem,posicao[4])

        tempo_ = format("Tempo: %d seg" %(controle.tempoTotal))
        JogoLabirinto.textoTempo = self.fonte.render(tempo_,1,(0,0,0))
        controle.screen.blit(JogoLabirinto.textoTempo,(60,90))