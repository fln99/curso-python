import pygame

pygame.mixer.init()

pygame.mixer.music.load('caribbean_queen.mp3')
pygame.mixer.music.play()

input('Digite algo para encerrar o áudio: ')