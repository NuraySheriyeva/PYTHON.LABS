import pygame
from sys import exit
import os

pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pygame.display.set_caption('Musicing')

# Ensure Python starts from the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

play = pygame.image.load('../images/play.png')
pause = pygame.image.load('../images/pause.png')
next = pygame.image.load('../images/next.png')
prev = pygame.image.load('../images/previous.png')

play = pygame.transform.scale(play, (50, 50))

pygame.draw.rect(screen, 'White', (200, 150, 450, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(play, (100, 100))

    pygame.display.update()
    clock.tick(60)