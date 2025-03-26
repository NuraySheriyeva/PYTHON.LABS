import pygame
import random
from sys import exit
import os
 
pygame.init()
pygame.mixer.init()

# Ensure Python starts from the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
 
pygame.mixer.music.load('../audio/game.mp3')
pygame.mixer.music.play(-1)
 
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game Demo")
clock = pygame.time.Clock()
 
#Game Font
font = pygame.font.Font(None,30)
 
# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
 
# Snake Settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
speed = 15
level = 1
 
# Food settings
food_count = 1
food_pos = [ [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10] 
            for _ in range(food_count)]
food_spawn = True
 
game_score = 0
total_food_ate =0
isRunning = True
FOOD_TIMER = pygame.USEREVENT +1
pygame.time.set_timer(FOOD_TIMER, 10000)
 
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            exit()  # Fixed sys.quit() to sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"    
        elif event.type == FOOD_TIMER:
            if food_pos:
                food_pos.pop(0)
                food_spawn = False
 
 
    # Move snake based on direction
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10
 
 
    # Insert new position
    snake_body.insert(0, list(snake_pos))  
    
    snake_head_rect = pygame.Rect(snake_pos[0], snake_pos[1], 10, 10)
    
    ate_food = False
    for food in food_pos:
        food_rect = pygame.Rect(food[0], food[1], 10, 10)
        if snake_head_rect.colliderect(food_rect):
            food_pos.remove(food)
            game_score+=random.randint(1,5)
            total_food_ate+=1
            food_spawn = False
            ate_food = True
            pygame.time.set_timer(FOOD_TIMER, 0)
            pygame.time.set_timer(FOOD_TIMER, 10000)
            break

    if not ate_food:
        snake_body.pop()
    
    if not food_spawn:
        food_pos.append([random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10])
        food_spawn = True
        pygame.time.set_timer(FOOD_TIMER,10000)
 
    """# Check for collision with walls
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        isRunning = False"""
    
    if snake_pos[0] <0:
        snake_pos[0]=WIDTH-5
    elif snake_pos[0]>WIDTH:
        snake_pos[0]=-5
    elif snake_pos[1]<0:
        snake_pos[1]=HEIGHT-5
    elif snake_pos[1]>HEIGHT:
        snake_pos[1]=-5
 
    # Check for collision with itself
    for block in snake_body[1:]:
        if snake_pos == block:
            isRunning = False
    
    #levels. each time score is a multiplier of 5 the level increases and the speed goes up and number of foods does too
    if total_food_ate%5==0 and len(food_pos)<(total_food_ate//5)+1:
        speed+=2
        level+=1
        food_pos.append([random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10])
    
    
    # Update screen
    screen.fill(BLACK)
    for p in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))
    for food in food_pos:
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], 10, 10))
 
    game_score_text = font.render(f"Score: {game_score}",True,'white')
    screen.blit(game_score_text,(20,20))
    level_text = font.render(f"Level: {level}",True,'white')
    screen.blit(level_text,(150,20))
    pygame.display.update()
 
    pygame.display.flip()
    clock.tick(speed)
   
 
 
game_over_text = font.render("GAME OVER", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (WIDTH / 2, HEIGHT / 2)
screen.blit(game_over_text,game_over_rectangle)
pygame.display.update()
pygame.time.wait(6000)
pygame.mixer