import pygame
import time

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("021.mp3.mp3")
pygame.mixer.music.play()

# Mantém o programa aberto enquanto o áudio toca
while pygame.mixer.music.get_busy():
    time.sleep(0.1)
