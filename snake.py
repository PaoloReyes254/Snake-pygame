import pygame

width = 640
height = 480

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake.py")
logo_surface = pygame.image.load("assets/logo.png").convert()
pygame.display.set_icon(logo_surface)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
pygame.quit()