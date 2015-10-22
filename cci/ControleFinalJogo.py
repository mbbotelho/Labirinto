from cih.ImprimeFinal import *

class FinalJogo:
    def __init__(self):
                      #Backg #JogNovo #Credito   #Sair    #Cursor
        self.posicao=[(0,0),(230,300),(230,400),(230,500),[100,300]]
        self.imprimiFinal=ImprimeFinal()

        return

    def mostraMenuFinalJogo(self, controle):

        if controle.evento.keys[0]: #se pressionar para cima
            if self.posicao[4][1] > 300:
                self.posicao[4][1]-=100

        if controle.evento.keys[1]: #se pressionar para baixo
            if self.posicao[4][1] < 500:
                self.posicao[4][1]+=100

        if controle.evento.keys[6]:#chama o jogo, creditos ou sair do jogo
            if self.posicao[4][1]==300:  # Implementar "Jogar Novamente"
                controle.jogo = JogoLabirinto() # gera novo labirinto
                controle.tempoTotal = 0 # zera o contador de tempo
                controle.opcao = 2

            if self.posicao[4][1]==400:
                controle.numero = 1 # artimanha para avisar o menu creditos para onde voltar caso pressione ESC (0 para menuInicial, 1 para menuFinal)
                controle.opcao = 4  # entrar nos creditos

            if self.posicao[4][1]==500:
                controle.opcao = 0 # sair do jogo

        if controle.evento.keys[4]: # se pressionar esc
            controle.opcao = 0  # sair do jogo

        self.imprimiFinal.imprimirJanelaFinal(controle,self.posicao)

        pygame.display.update()
