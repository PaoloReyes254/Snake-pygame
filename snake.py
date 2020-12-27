import pygame, random
from pygame.math import Vector2

class SNAKE(object):
    def __init__(self):
        self.body = [Vector2(8, 10), Vector2(7, 10), Vector2(6, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 200, 200), block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

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
snake = SNAKE()
fruit = FRUIT()

#Events
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

#Game loop
run = True
while run:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)
    
    #Screen 
    screen.fill((175, 215, 70))

    #Fruit
    fruit.draw_fruit()

    #Snake
    snake.draw_snake()

    #FPS
    pygame.display.update()
    clock.tick(60)
    print(clock.get_fps())

#Pygame quit
pygame.quit()