import pygame
from sys import exit
import math 

pygame.init()

width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Paint")
active_size = 20
active_color = 'white'
active_shape= 'rectangle'
drawing_shape= False
painting = []
shapes_drawn =[]

def draw_menu(size, color):
    pygame.draw.rect(screen, (240, 240, 250), [0, 0, width, 100])

    blue=pygame.draw.rect(screen, (0,0,240), [width-50, 20, 25, 25] )
    red=pygame.draw.rect(screen, (240,0,0), [width-50, 45, 25, 25] )
    green=pygame.draw.rect(screen, (0,240,0), [width-75, 20, 25, 25] )
    yellow=pygame.draw.rect(screen, (240,240,0), [width-75, 45, 25, 25] )
    white=pygame.draw.rect(screen, (255,255,255), [width-100, 20, 25, 25] )
    black=pygame.draw.rect(screen, (0,0,0), [width-100, 45, 25, 25] )
    pink=pygame.draw.rect(screen, (255,120,160), [width-125, 20, 25, 25] )
    purple=pygame.draw.rect(screen, (150,0,205), [width-125, 45, 25, 25])
    color_rect = [blue, red, green, yellow, white, black, pink, purple]
    rgb_list = [(0,0,240),(240,0,0), (0,240,0), (240,240,0), (255,255,255), (0,0,0), (255,120,160), (150,0,205)]

    pygame.draw.circle(screen, color, (400, 35), 30)
    pygame.draw.circle(screen, 'dark gray', (400, 35), 30, 3)

    brush=pygame.draw.circle(screen, (100, 100, 100), (250, 40), 20)

    rectangle = pygame.draw.rect(screen, (20, 20, 20), (10, 10, 45, 30))
    right_triangle = pygame.draw.polygon(screen, (20, 20, 20), [(10,45), (40, 45), (10,85)], 2)
    thrice_triangle = pygame.draw.polygon(screen, (20, 20, 20), [(100, 8), (100-23, 40), (100+23, 40)])
    circle = pygame.draw.circle(screen, (20, 20, 20), (100, 65),20)
    square = pygame.draw.rect(screen, (20, 20, 20), (150, 10, 30, 30))
    rhombus = pygame.draw.polygon(screen, (20, 20, 20),[(165, 45),(180, 65),(165 , 85),(150, 65)])
    shape_rect= [rectangle, right_triangle, thrice_triangle, circle, square, rhombus]

    return color_rect, shape_rect, rgb_list, brush

def draw_shape(screen, tool, start, end, color):
    x1, y1 = start
    x2, y2 = end
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    left = min(x1, x2)
    top = min(y1, y2)

    if tool == "rectangle":
        pygame.draw.rect(screen, color, (left, top, width, height), 2)
    elif tool == "square":
        side = min(width, height)
        pygame.draw.rect(screen, color, (left, top, side, side), 2)
    elif tool == "circle":
        radius = int(math.hypot(x2 - x1, y2 - y1))
        pygame.draw.circle(screen, color, start, radius, 2)
    elif tool == "right_triangle":
        pygame.draw.polygon(screen, color, [start, (x2, y1), end], 2)
    elif tool == "equilateral_triangle":
        side = width
        height_eq = int((math.sqrt(3) / 2) * side)
        points = [start, (x1 + side, y1), (x1 + side // 2, y1 - height_eq)]
        pygame.draw.polygon(screen, color, points, 2)
    elif tool == "rhombus":
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        dx = abs(x2 - x1) // 2
        dy = abs(y2 - y1) // 2
        points = [
            (center_x, center_y - dy),
            (center_x + dx, center_y),
            (center_x, center_y + dy),
            (center_x - dx, center_y)
        ]
        pygame.draw.polygon(screen, color, points, 2)

def draw_painting(paint):
    for i in range(len(paint)):
        pygame.draw.circle(screen, paint[i][0], paint[i][1], paint[i][2])

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = event.pos
            end = event.pos 
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color=rgbs[i]
            if brush.collidepoint(event.pos):
                drawing_shape=False
                clicked_ui = True
            shapes_name=["rectangle", "right_triangle", "equilateral_triangle", "circle", "square", "rhombus"]
            for i in range(len(shapes)):
                if shapes[i].collidepoint(event.pos):
                    active_shape=shapes_name[i]
                    drawing_shape=True
            if event.button==4:
                active_size+=1
            if event.button==5:
                active_size-=1
            if event.button==3:
                active_color='white'
            
        if event.type == pygame.MOUSEBUTTONUP:
            end= event.pos
            if drawing_shape and start[1]>100 and end[1]>100:
                shapes_drawn.append(( active_shape, start, end, active_color))
        
        
                    
    screen.fill('white')

    colors, shapes, rgbs, brush = draw_menu(active_size, active_color)
    mouse=pygame.mouse.get_pos()
    left_click= pygame.mouse.get_pressed()[0]
    
    for shape in shapes_drawn:
        draw_shape(screen, shape[0], shape[1], shape[2], shape[3])
    draw_painting(painting)
    if mouse[1]>120:
        pygame.draw.circle(screen, active_color, mouse, active_size)
    if left_click and mouse[1]>120 and not drawing_shape:
        painting.append((active_color, mouse, active_size))

    
    pygame.display.update()
    clock.tick(60)
