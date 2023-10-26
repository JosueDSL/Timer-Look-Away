import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("look_away.mp3")
    
while True:
    pygame.mixer.music.play()
    time.sleep(600)