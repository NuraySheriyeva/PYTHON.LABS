import pygame
from pygame.locals import *
from sys import exit
import random
import os 
import time

pygame.init()

displaysurf = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()
pygame.display.set_caption("Racist")
# Ensure Python starts from the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
test_font0 = pygame.font.SysFont("Monospace", 50)
test_font1 = pygame.font.SysFont("Monospace", 20)
score_font = pygame.font.SysFont("Monospace", 20)
coin_font = pygame.font.SysFont("Monospace", 20)

width = 400
height = 600
speed = 5
text0 = test_font0.render("GAME OVER", False, 'White' )
text1 = test_font1.render("Points: ", False, 'Black' )
"""text2 = test_font1.render("Coins: ", False, 'Black' )"""
score = 0
"""global picked_coins
picked_coins = 0"""


background = pygame.image.load('../images/AnimatedStreet.png')

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../images/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.top>600):
            global score
            score +=1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../images/coin.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width-40), random.randint(10, height-200))

    def move(self):
        self.rect.move_ip(0, 3)
        if (self.rect.top>600):
            self.rect.top = random.randint(10, height)
            self.rect.center = (random.randint(30, 370), random.randint(10, height-400))
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../images/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    
    def move(self):
        key= pygame.key.get_pressed()
        if self.rect.left >0:
            if key[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right <width:
            if key[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()
C1 = Coins()

enemies = pygame.sprite.Group()
enemies.add(E1)
"""coinies = pygame.sprite.Group()
coinies.add(C1)"""
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
"""all_sprites.add(C1)"""

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

while True:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    

    displaysurf.fill('White')
    displaysurf.blit(background, (0,0))
    P1.draw(displaysurf)
    E1.draw(displaysurf)
    scores = score_font.render(str(score), True, 'Black')
    displaysurf.blit(scores, (10,10))
    """C1.draw(displaysurf)
    all_coins = coin_font.render(str(picked_coins), True, 'Black')
    displaysurf.blit(all_coins, (width-30,10))"""

    for entity in all_sprites:
        displaysurf.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('../audio/crash.wav').play()
        time.sleep(0.3)
        displaysurf.fill((220, 20, 60))
        displaysurf.blit(text0, (70, 265))
        displaysurf.blit(text1, (70, 320))
        displaysurf.blit(scores, (170,320))
        """displaysurf.blit(text2, (250, 320))
        displaysurf.blit(all_coins, (330,320))"""
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        exit()
    
    """if pygame.sprite.spritecollideany(P1, coinies):
        pygame.mixer.Sound('../audio/mario.mp3').play()
        C1.rect.center = (random.randint(30, 370), random.randint(10, height-400))
        picked_coins +=1"""
        

    pygame.display.update()
    clock.tick(60)
