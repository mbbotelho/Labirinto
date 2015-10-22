__author__ = 'Douglas'
import pygame,os

class Imagens:
    def __init__(self,nome):
        self.tiponome=nome+".png" # compilar a String nome com o tipo de imagem .png

    def criaImagens(self,tamanho): # tamanho que desejo as imagens
        self.file=os.path.join("imagens",self.tiponome) # file recebe o local da imagem que sera utilizada e o nome da imagem
        self.Imagem = pygame.image.load(self.file) # carrega a imagem
        return pygame.transform.scale(self.Imagem,tamanho) # redimensiona a imagem