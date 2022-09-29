import pygame

#Initialize Pygame
pygame.init()

#Create Display
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("BeatDrop")
icon = pygame.image.load('assets/gameicon.png')
pygame.display.set_icon(icon)

#Default Game Loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    screen.fill((75, 0, 130))
    pygame.display.update()
    