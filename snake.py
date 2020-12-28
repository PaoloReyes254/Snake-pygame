import pygame, random
from pygame.math import Vector2

#Classes
class SNAKE(object):
    def __init__(self):
        self.body = [Vector2(10, 9), Vector2(9, 9), Vector2(8, 9)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load("assets/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("assets/head_down.png").convert_alpha()
        self.head_left = pygame.image.load("assets/head_left.png").convert_alpha()
        self.head_right = pygame.image.load("assets/head_right.png").convert_alpha()

        self.tail_up = pygame.image.load("assets/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("assets/tail_down.png").convert_alpha()
        self.tail_left = pygame.image.load("assets/tail_left.png").convert_alpha()
        self.tail_right = pygame.image.load("assets/tail_right.png").convert_alpha()

        self.body_vertical = pygame.image.load("assets/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("assets/body_horizontal.png").convert_alpha()

        self.body_tr = pygame.image.load("assets/body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load("assets/body_tl.png").convert_alpha()
        self.body_br = pygame.image.load("assets/body_br.png").convert_alpha()
        self.body_bl = pygame.image.load("assets/body_bl.png").convert_alpha()

    def draw_snake(self):
        for index, block in enumerate(self.body):
            if index == 0:
                difference = self.body[1] - self.body[0]
                if difference == Vector2(1, 0):
                    block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                    screen.blit(self.head_left, block_rect)
                elif difference == Vector2(-1, 0):
                    block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                    screen.blit(self.head_right, block_rect)
                elif difference == Vector2(0, 1):
                    block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                    screen.blit(self.head_up, block_rect)
                elif difference == Vector2(0, -1):
                    block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                    screen.blit(self.head_down, block_rect)
            elif index > 0 and index < len(self.body) - 1:
                if block.x + 1 == self.body[index - 1].x:
                    if block.y + 1 == self.body[index + 1].y:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_br, block_rect)
                    elif block.y - 1 == self.body[index + 1].y:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_tr, block_rect)
                    else:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_horizontal, block_rect)
                elif block.x - 1 == self.body[index - 1].x:
                    if block.y + 1 == self.body[index + 1].y:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_bl, block_rect)
                    elif block.y - 1 == self.body[index + 1].y:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_tl, block_rect)
                    else:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_horizontal, block_rect)
                elif block.y - 1 == self.body[index - 1].y:
                    if block.x + 1 == self.body[index + 1].x:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_tr, block_rect)
                    elif block.x - 1 == self.body[index + 1].x:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_tl, block_rect)
                    else:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_vertical, block_rect)
                elif block.y + 1 == self.body[index - 1].y:
                    if block.x - 1 == self.body[index + 1].x:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_bl, block_rect)
                    elif block.x + 1 == self.body[index + 1].x:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_br, block_rect)
                    else:
                        block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                        screen.blit(self.body_vertical, block_rect)
            else:
                if block.x + 1 == self.body[index - 1].x:
                    block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                    screen.blit(self.tail_left, block_rect)
                elif block.x - 1 == self.body[index - 1].x:
                    block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                    screen.blit(self.tail_right, block_rect)
                elif block.y - 1 == self.body[index - 1].y:
                    block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                    screen.blit(self.tail_down, block_rect)
                elif block.y + 1 == self.body[index - 1].y:
                    block_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
                    screen.blit(self.tail_up, block_rect)

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
        screen.blit(apple_surface, fruit_rect)

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
        self.draw_grass()
        self.valid_fruit_pos()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_text()
    
    def check_collisions(self):
        if self.fruit.pos == self.snake.body[0]:
            point_sound.play()
            self.fruit.__init__()
            self.snake.add_one()
    
    def valid_fruit_pos(self):
        status = False
        for block in self.snake.body:
            if self.fruit.pos == block:
                self.fruit.__init__()
                status = True
        while status:
            for block in self.snake.body:
                if self.fruit.pos == block:
                    self.fruit.__init__()
                if block == self.snake.body[len(self.snake.body) - 1]:
                    if self.fruit.pos == block:
                        self.fruit.__init__()
                    else:
                        status = False

    def check_fail(self, run):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            return False
        else:
            return True

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_text(self):
        score = str(len(self.snake.body) - 3)
        score_surface = game_text.render(score, True, (254, 254, 254))
        score_x = cell_number * cell_size - 60
        score_y = cell_number * cell_size - 40
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple_surface.get_rect(midright = (score_rect.left, score_rect.centery))

        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 10, apple_rect.height)
        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        pygame.draw.rect(screen, (40, 40, 40), bg_rect, 2)

        screen.blit(score_surface, score_rect)
        screen.blit(apple_surface, apple_rect)

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
apple_surface = pygame.image.load("assets/apple.png").convert_alpha()
game_text = pygame.font.Font("assets/PoetsenOne-Regular.ttf", 25)

#Sound
point_sound = pygame.mixer.Sound("assets/crunch.wav")

#Objects
main_game = MAIN()

#Events
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

#Game loop
run = True
reset = True
while run:
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == SCREEN_UPDATE:
            reset = main_game.update()
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
    if reset == False:
        main_game.snake.body = [Vector2(10, 9), Vector2(9, 9), Vector2(8, 9)]
        main_game.snake.direction = Vector2(0, 0)
    for block in main_game.snake.body[1:]:
        if block == main_game.snake.body[0]:
            main_game.snake.body = [Vector2(10, 9), Vector2(9, 9), Vector2(8, 9)]
            main_game.snake.direction = Vector2(0, 0)

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