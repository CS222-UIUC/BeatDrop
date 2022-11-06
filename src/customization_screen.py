"""Initialize"""
#from math import fabs
# pylint: disable=C0413
# pylint: disable=E0401
import sys
import pygame
sys.path.insert(1, '..//course-project-group-84//src')
from character import DinoSprite
# pylint: disable=E1101


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = pygame.Color('pink')
FPS = 10

def main():
    """Initialize the screen"""
    # pylint: disable=R0801
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    orig = DinoSprite()
    group = pygame.sprite.Group(orig)
    orig.state = "still"

    skin1 = DinoSprite()
    group.add(skin1)
    skin1.state = "still"
    skin1.rect.x = skin1.rect.x + 200

    skin2 = DinoSprite()
    group.add(skin2)
    skin2.state = "still"
    skin2.rect.x = skin1.rect.x + 200

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        group.update()
        screen.fill(BACKGROUND_COLOR)
        group.draw(screen)
        pygame.display.update()
        clock.tick(10)
if __name__ == "__main__":
    main()
