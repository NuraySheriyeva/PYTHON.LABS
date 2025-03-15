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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle_y-=20
    if keys[pygame.K_DOWN]:
        circle_y+=20
    if keys[pygame.K_LEFT]:
        circle_x-=20
    if keys[pygame.K_RIGHT]:
        circle_x+=20
        
    if circle_x < 25: circle_x=25
    if circle_y < 25: circle_y=25
    if circle_x > 775: circle_x=775
    if circle_y > 375: circle_y=375

    #             R    G    B
    screen.fill((255, 255, 255))
    #                            R   G  B    position  radius
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), 25)
    
    
    pygame.display.update()
    clock.tick(60)