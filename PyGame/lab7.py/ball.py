import pygame 
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("BAller")
clock = pygame.time.Clock()

circle_x = 400
circle_y = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    circle_x-=5
    circle_y-=5
    if circle_x < 25: circle_x=25
    if circle_y < 25: circle_y=25

    #             R    G    B
    screen.fill((255, 255, 255))
    #                            R   G  B    position  radius
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), 25)
    pygame.display.update()
    clock.tick(60)