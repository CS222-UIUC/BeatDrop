"""Initialize Pygame"""
# pylint: disable=no-member
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Initialize Pygame
def initialize():
    """Initialize Method"""
    pygame.init()

    #Create Display
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    #Title and Icon
    pygame.display.set_caption("BeatDrop")
    icon = pygame.image.load('assets/gameicon.png')
    pygame.display.set_icon(icon)

    #Default Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((75, 0, 130))
        pygame.display.update()
        
initialize()