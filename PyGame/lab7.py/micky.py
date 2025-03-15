import pygame 
from sys import exit
import os

pygame.init()
#                                width,height
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Micky Clock")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

# Ensure Python starts from the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#-------------I   M   A   G   E   S-----------------------------------------------------------------
clock_surface = pygame.image.load('../images/clock.png')
clock_surface = pygame.transform.scale(clock_surface, (500, 400))  # (width, height)

left_arm= pygame.image.load('../images/leftarm.png')
left_arm = pygame.transform.scale(left_arm,(50, 500))

right_arm= pygame.image.load('../images/rightarm.png')
right_arm = pygame.transform.scale(right_arm,(700, 600))

text_surface= test_font.render("Micky Clocky", False, 'White')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

#               our surface, position
    screen.blit(clock_surface,(250,50))
    screen.blit(left_arm,(482,20))
    screen.blit(right_arm,(152,-40))
    screen.blit(text_surface, (400,12))
                
    pygame.display.update()
    clock.tick(60)