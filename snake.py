import pygame, random
from pygame.math import Vector2

class SNAKE(object):
    def __init__(self):
        self.body = [Vector2(8, 10), Vector2(7, 10), Vector2(6, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (0, 200, 200), block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def add_one(self):
        self.new_block = True

class FRUIT(object):
    def __init__(self):
        self.x = random.randint(0 ,cell_number - 1)
        self.y = random.randint(0 ,cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255, 0, 0), fruit_rect)

class MAIN(object):
    def __init__(self):
        self.fruit = FRUIT()
        self.snake = SNAKE()
        self.run = True
    
    def update(self):
        self.snake.move_snake()
        self.check_collisions()
        self.run = self.check_fail(self.run)
        return self.run

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
    
    def check_collisions(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.__init__()
            self.snake.add_one()

    def check_fail(self, run):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            return False
        else:
            return True

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
main_game = MAIN()

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
            run = main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not main_game.snake.body[0].y - 1 == main_game.snake.body[1].y:
                    main_game.snake.direction = Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                if not main_game.snake.body[0].y + 1 == main_game.snake.body[1].y:
                    main_game.snake.direction = Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                if not main_game.snake.body[0].x - 1 == main_game.snake.body[1].x:
                    main_game.snake.direction = Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                if not main_game.snake.body[0].x + 1 == main_game.snake.body[1].x:
                    main_game.snake.direction = Vector2(1, 0)

    #Helper for checking collitions since for loop not working on main class
    if run == True:
        for block in main_game.snake.body[1:]:
            if block == main_game.snake.body[0]:
                run = False
                break
            else:
                run = True

    #Screen 
    screen.fill((175, 215, 70))

    #Game
    main_game.draw_elements()

    #FPS
    pygame.display.update()
    clock.tick(60)
    #print(clock.get_fps())

#Pygame quit
pygame.quit()