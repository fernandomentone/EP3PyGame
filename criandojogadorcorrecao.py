import pygame
# Inicializar Pygame
pygame.init()
# Definições de cores
BRANCO = (255, 255, 255)
VERDE = (0, 255, 50)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird")
FPS = 30
# Configurações do pássaro
pos_x = 50
pos_y = 300
velocidade_y = 0
gravidade = 1
pulo = -13
# Configurações do pássaro
pos_x = 50
pos_y = 300
velocidade_y = 0
gravidade = 1
pulo = -13

def criar_jogador():
    play = pygame.draw.rect(tela, 'yellow', (pos_x, pos_y, 30, 30), 0, 10)
    return play
