import pygame 
from sys import exit
import os
import time
from math import sin, cos, radians

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
right_arm = pygame.transform.scale(right_arm,(350, 250))

text_surface= test_font.render("Micky Clocky", False, 'Black')

pivot_x, pivot_y =500, 250
hand_length = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill('White')

#               our surface, position
    screen.blit(clock_surface,(250,50))
    screen.blit(text_surface, (380,40))
    
    current_s = time.localtime().tm_sec
    angle_s = current_s * 6

    current_m = time.localtime().tm_min
    angle_m = current_m * 6

    rotate_s= pygame.transform.rotate(left_arm, -angle_s)
    rotate_m= pygame.transform.rotate(right_arm, -angle_m)

    hand_rect_s=rotate_s.get_rect(center=( pivot_x + hand_length * cos(radians(angle_s - 90)),  # -90 aligns it correctly
        pivot_y + hand_length * sin(radians(angle_s - 90))
    )) 
    pygame.draw.circle(screen, (0, 0, 0), (pivot_x, pivot_y), 5)  # Small dot for pivot
    screen.blit(rotate_s, hand_rect_s.topleft)

    hand_rect_m=rotate_m.get_rect(center=( pivot_x + hand_length * cos(radians(angle_m - 90)),  # -90 aligns it correctly
        pivot_y + hand_length * sin(radians(angle_m - 90))
    ))
    pygame.draw.circle(screen, (0, 0, 0), (pivot_x, pivot_y), 5)  # Small dot for pivot
    screen.blit(rotate_m, hand_rect_m.topleft)

    pygame.display.update()
    clock.tick(60)