import pygame
from sys import exit
import os

pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
pygame.display.set_caption('Musicing')
test_font = pygame.font.Font(None, 50)

# Ensure Python starts from the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

play = pygame.image.load('../images/play.png')
pause = pygame.image.load('../images/pause.png')
next = pygame.image.load('../images/next.png')
prev = pygame.image.load('../images/previous.png')

play = pygame.transform.scale(play, (50, 50))
pause = pygame.transform.scale(pause, (50, 50))
next = pygame.transform.scale(next, (50, 50))
prev = pygame.transform.scale(prev, (50, 50))

screen.fill("White")
circle_x=250
circle_y=292

text = test_font.render('Calming Lo-fi', True, 'Black')

calm = '../audio/calm.mp3'
jazz = '../audio/jazz.mp3'

lofi = pygame.image.load('../images/lofi.jpg')
lofi = pygame.transform.scale(lofi, (200, 200))
juzzing = pygame.image.load('../images/jazzician.jpg')
juzzing = pygame.transform.scale(juzzing, (200, 200))
line = pygame.image.load('../images/line.jpg')
line = pygame.transform.scale(line, (300, 20))
ball = pygame.image.load('../images/grey.png')
ball = pygame.transform.scale(ball, (10, 10))

now=calm
def current(me):
    pygame.mixer.music.load(me)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(play, (240, 320))
    #screen.blit(pause, (220, 320))
    screen.blit(next, (420, 320))
    screen.blit(prev, (520, 320))
    screen.blit(text, (280, 40))
    screen.blit(lofi, (300,80))
    screen.blit(line, (250, 290))
    screen.blit(ball, (circle_x, circle_y))
    
    key = pygame.key.get_pressed()
    

    if key[pygame.K_SPACE]:
        circle_x=250
        current(now)
        pygame.mixer.music.play()
    if key[pygame.K_RETURN]:
        pygame.mixer.music.stop()
    if key[pygame.K_RIGHT]:
        circle_x=250
        current(jazz)
        now=jazz
        pygame.mixer.music.play()
    if key[pygame.K_LEFT]:
        circle_x=250
        current(calm)
        now=calm
        pygame.mixer.music.play()
    
    circle_x+=0.03

    pygame.display.update()
    clock.tick(60)