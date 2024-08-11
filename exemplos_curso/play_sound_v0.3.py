# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:07:23 2024

@author: Microsoft Copilot
@Modified by: github.com/aleitebr
"""

import pygame
import os

# muda para diretórios com arquivos de áudios
os.chdir('c:/Users/alexa/dados/audio')
lista_musicas = os.listdir('.')

# Inicializa o pygame
pygame.init()
# Inicializa o mixer do pygame
pygame.mixer.init()


for musica in lista_musicas: 
    # Carrega o arquivo de áudio
    pygame.mixer.music.load(musica)

    # Reproduz o áudio
    pygame.mixer.music.play()

    
    print("Pressione 'p' para pausar, 'r' para retomar, 'n' para próxima e 's' para parar.")

    # Loop para verificar os comandos do usuário
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        command = input("Digite um comando: ").strip().lower()
        if command == 'p':
            pygame.mixer.music.pause()
        elif command == 'r':
            pygame.mixer.music.unpause()
        elif command == 'n':
            pygame.mixer.music.stop()
            running = False
        elif command == 's':
            pygame.mixer.music.stop()
            running = False
                   
    if command == 's':  
        break
     
pygame.quit()

 