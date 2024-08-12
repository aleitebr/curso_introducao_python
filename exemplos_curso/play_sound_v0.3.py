# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:07:23 2024

@author: Microsoft Copilot
@Modified by: github.com/aleitebr

Simple Graphical Interface
FULLSCREEN
"""

import pygame
import os

# Inicializa o pygame
pygame.init()
# Inicializa o mixer do pygame
pygame.mixer.init()

# muda para diretórios com arquivos de áudios
os.chdir('./dados/audio')
lista_musicas = os.listdir('.')

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Define as dimensões da janela
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Define a fonte e o tamanho do texto
font = pygame.font.SysFont('Arial', 20)

# Timer para animação
timer = pygame.time.Clock()

# Função para exibir texto na tela
def display_text(text, x, y):
    text_surface = font.render(text, True, BRANCO)  # Branco
    screen.blit(text_surface, (x, y))

# Carrega o arquivo de áudio
n = 0
pygame.mixer.music.load(lista_musicas[n])

# Reproduz o áudio
pygame.mixer.music.play()

#print("Pressione 'p' para pausar, 'r' para retomar, 'n' para próxima e 's' para parar.")

# Loop para verificar os comandos do usuário
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            print(event.unicode)
            command = str(event.unicode).lower()
            if command == 'p':
                pygame.mixer.music.pause()
            elif command == 'r':
                pygame.mixer.music.unpause()
            elif command == 'n':
                pygame.mixer.music.stop()
                try:
                    # Carrega o arquivo de áudio
                    n = n + 1
                    pygame.mixer.music.load(lista_musicas[n])
                    # Reproduz o áudio
                    pygame.mixer.music.play()
                except IndexError:
                    pygame.quit()
            elif command == 's':
                pygame.quit()
            
                
    # Preenche a tela com a cor de fundo
    screen.fill(PRETO)

    # Exibe o texto na tela
    display_text("Pressione 'p' para pausar, 'r' para retomar, 'n' para próxima e 's' para parar.", 20, 20)
    display_text("Digite um comando: ", 20, 100)

    # Atualiza a tela
    pygame.display.update()
            
    # Controla a taxa de atualização
    timer.tick(60)

pygame.quit()
     


 