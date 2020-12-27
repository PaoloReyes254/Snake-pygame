import pygame, random
from pygame.math import Vector2

class FRUIT(object):
    def __init__(self):
        self.x = random.randint(0 ,cell_number - 1)
        self.y = random.randint(0 ,cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 0, 0), fruit_rect)

#Game dimensions
cell_size = 40
cell_number = 20

#Pygame initialization
pygame.init()

#Basic parameters of pygame
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
pygame.display.set_caption("Snake.py")
logo_surface = pygame.image.load("assets/logo.png").convert()
pygame.display.set_icon(logo_surface)
clock = pygame.time.Clock()

#Surfaces

#Objects
fruit = FRUIT()

#Game loop
run = True
while run:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #Screen 
    screen.fill((175, 215, 70))

    #Fruit
    fruit.draw_fruit()

    #FPS
    pygame.display.update()
    clock.tick(60)
    print(clock.get_fps())

#Pygame quit
pygame.quit()