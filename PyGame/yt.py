import pygame 
from sys import exit

pygame.init()
#                                width,height
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

# HOW TO INSERT A COLOR 
# test_surface = pygame.Surface((100,200))
# test_surface.fill('Red')

#HOW TO INSERT AN IMAGE
test_surface = pygame.image.load('images/clock.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

#               our surface, position
    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)