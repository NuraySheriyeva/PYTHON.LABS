import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pygame.display.set_caption('Musicing')

play = pygame.image.load('../images/play.png')
pause = pygame.image.load('../images/pause.jpg')
next = pygame.image.load('../images/next.png')
prev = pygame.image.load('../images/previous.png')

pygame.draw.rectangle('White', (200, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(play, (100, 100))

    pygame.display.update()
    clock.tick(60)