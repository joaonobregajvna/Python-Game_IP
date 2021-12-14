import pygame
from pygame.locals import *
from sys import exit
from random import randint
# Inicialização do jogo
pygame.mixer.init()
pygame.init()

# Música de Fundo
pygame.mixer.music.set_volume(0.3)
# Tocar
musica_de_fundo = pygame.mixer.music.load('musics/musica_de_fundo.mp3')
# Não parar de tocar a música
pygame.mixer.music.play(-1)
# Barulho da colisão
barulho_colisao = pygame.mixer.Sound('musics/colisao.wav')

# Tamanho da tela
largura = 1024
altura = 720

# A nave com 100x100 px
nave = pygame.transform.scale(pygame.image.load("images/sprite_nave.png"), (100, 100))

# Background
img = pygame.transform.scale(pygame.image.load("images/background.jpg"), (largura, altura))

# Imagem da gasolina
gasolina = pygame.transform.scale(pygame.image.load("images/gasolina.png"), (50, 50))

# Altura e largura da tela
tela = pygame.display.set_mode((largura, altura))

# Icone da janela
icone = pygame.image.load("images/icon.jpg")
pygame.display.set_icon(icone)

# Nome da  tela
pygame.display.set_caption("A Viagem Espacial de Calegário")

# Pontuação inicial
pontuacao = 0

# Movimentação do jogador
x = 0
y = 0

# Relogio de tempo
relogio = pygame.time.Clock()

# Posição aleátoria
position_x = randint(0, largura-40)
position_y = randint(0, altura-40)

# Fonte das mensagens na telaa
fonte = pygame.font.SysFont("Arial", 30, True, True)

while True:
    # Carregar background
    tela.blit(img, (0, 0))

    # 30 segundos de tempo ao total
    tempo_total = (30000 / 1000)
    # Tirar 1 segundo a cada segundo
    tempo_total -= (pygame.time.get_ticks() / 1000)

    # FPS
    relogio.tick(60)

    # Se o tempo chegar até 0 perdeu
    if tempo_total <= 0:
        quit()

    # Mensagem na tela do tempo
    mensagem = f'Tempo: {int(tempo_total)}'
    texto_formatado = fonte.render(mensagem, False, (255, 255, 255))

    # Mensagem na tela da pontuação
    message = f'Pontuacao: {int(pontuacao)}'
    pontuacao_formatada = fonte.render(message, False, (255, 255, 255))

    for event in pygame.event.get():
        # Evento de fechar o jogo
        if event.type == QUIT:
            pygame.quit()
            exit()

        # Esquerda
        if pygame.key.get_pressed()[K_a]:
            if x <= 0:
                x += 10
            x -= 10
        # Direita
        if pygame.key.get_pressed()[K_d]:
            if x >= largura-100:
                x -= 10
            x += 10
        # Cima
        if pygame.key.get_pressed()[K_w]:
            if y <= 0:
                y += 10
            y -= 10
        # Baixo
        if pygame.key.get_pressed()[K_s]:
            if y >= altura-100:
                y -= 10
            y += 10

    # Fundo transparente pra o box não aparecer
    s = pygame.Surface((largura, altura))
    s.set_alpha(0)
    s.fill((255, 255, 255))

    # Colocar a nave e o fundo na tela
    tela.blit(s, (0, 0))
    tela.blit(nave, (x, y))

    # Criar um retângulo na nave para colidir
    ret_player = pygame.draw.rect(s, (0, 0, 0), (x, y, 100, 100))

    # Subir a pontuação aleatoriamente
    pontuacao += 1

    # Quadrado de colisão e imagem da gasolina
    ret_gasolina = pygame.draw.rect(s, (100, 100, 255), (position_x, position_y, 50, 50))
    tela.blit(gasolina, (position_x, position_y))

    if ret_player.colliderect(ret_gasolina):
        # Barulho quando colidir
        barulho_colisao.play()
        # Recriar o objeto em uma posição aleatoria dentro da tela
        position_x = randint(0, largura-40)
        position_y = randint(0, altura-40)
        # Quando pegar a gasolina ganha + 500 pontos
        pontuacao += 500

    # Aparecer a pontuação e o tempo na tela
    tela.blit(pontuacao_formatada, (largura-300, 40))
    tela.blit(texto_formatado, (largura-200, 0))

    # Atualizar o jogo a cada iteração
    pygame.display.update()
