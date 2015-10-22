__author__ = 'Douglas'
from cdp.CriaBotoes import *

class ImprimeMenu:
    def __init__(self):
        self.jogarImagem = Botoes("jogar").criaBotao() # recebe a imagem do botao jogar
        self.creditosImagem = Botoes("creditos").criaBotao() # recebe a imagem do botao creditos
        self.sairImagem = Botoes("sair").criaBotao() # recebe a imagem do botao sair
        self.cursorImagem = Botoes("cursor").criaBotao() # recebe a imagem do cursor

        self.file_back=os.path.join("imagens","backpequeno.png") #file recebe o local da imagem que sera utilizada
        self.backImagem = pygame.image.load(self.file_back) # recebe a imagem do background

    def imprimiJanelaMenu(self,controle,posicao):
        controle.screen.fill(0) #limpar a tela
        controle.screen.blit(self.backImagem,posicao[0]) # printa o background
        controle.screen.blit(self.jogarImagem,posicao[1]) # printar o botao jogar
        controle.screen.blit(self.creditosImagem,posicao[2]) # printar o botao creditos
        controle.screen.blit(self.sairImagem,posicao[3]) # printar o botao sair
        controle.screen.blit(self.cursorImagem,posicao[4]) # printar o cursor