import pygame
from pygame.locals import *
from sys import exit

# Inicialização do jogo
pygame.init()

# Tamanho da tela
largura = 640
altura = 480

# Altura e largura da tela
tela = pygame.display.set_mode((largura, altura))

# Nome da tela
pygame.display.set_caption("Jogo de Introdução a Programação")

# Icone da tela
icone = pygame.image.load("imagens/bruxo.png")
pygame.display.set_icon(icone)

while True:
    for event in pygame.event.get():
        # Evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()
    # Atualizar o jogo a cada iteração
    pygame.display.update()