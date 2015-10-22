from cdp.CriaImagensJogo import *

class Creditos:
    def __init__(self):
        self.imagemCreditos = [0,0] # posicao onde sera impresso o background ((0,0) e o topo superior esquerdo)
        self.creditosImagem = Imagens("backcreditos").criaImagens((632,632)) # file recebe o local da imagem que sera utilizada
        return

    def mostraCreditos(self,numero, controle):

        if controle.evento.keys[4]: # se a tecla ESC for pressionada
            if numero == 0:
                controle.opcao = 1 # retorna a opcao correspondente no loop principal (controle)
            if numero == 1:
                controle.opcao = 5 # retorna a opcao correspondente no loop principal (controle)

        controle.screen.fill(0) #limpar a tela
        controle.screen.blit(self.creditosImagem,self.imagemCreditos) # printar a tela
        pygame.display.update() # atualiza a imagem
