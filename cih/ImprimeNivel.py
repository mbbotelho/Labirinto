__author__ = 'Douglas'
from cdp.CriaBotoes import *

class ImprimeNivel:
    def __init__(self):

        self.facilImagem = Botoes("facil").criaBotao() # recebe a imagem a ser utilizada
        self.medioImagem = Botoes("medio").criaBotao()
        self.dificilImagem = Botoes("dificil").criaBotao()
        self.cursorImagem = Botoes("cursor").criaBotao()

        self.back = (0,0) # paralelepipedo do tamanho do botao
        self.file_back=os.path.join("imagens","backpequeno.png") #file recebe o local da imagem que sera utilizada
        self.backImagem = pygame.image.load(self.file_back)

    def imprimiJanelaNivel(self,controle,posicao):
        controle.screen.fill(0) #limpar a tela
        controle.screen.blit(self.backImagem,posicao[0]) # printar a tela
        controle.screen.blit(self.facilImagem,posicao[1]) # printar a tela
        controle.screen.blit(self.medioImagem,posicao[2]) # printar a tela
        controle.screen.blit(self.dificilImagem,posicao[3]) # printar a tela
        controle.screen.blit(self.cursorImagem,posicao[4]) # printar a tela