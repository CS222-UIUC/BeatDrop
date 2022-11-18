"""Initialize"""
#from math import fabs
# pylint: disable=C0413
# pylint: disable=E0401
# pylint: disable=R0914
import sys
import pygame
sys.path.insert(1, '..//course-project-group-84//src')
from character import DinoSprite
# pylint: disable=E1101


SCREEN_WIDTH = 1333
SCREEN_HEIGHT = 533
BACKGROUND_COLOR = pygame.Color('black')
FPS = 10

CUSTOMIZATION_KEY_OPTIONS = {
  pygame.K_q: "Q",
  pygame.K_w: "W",
  pygame.K_e: "E",
  pygame.K_ESCAPE: "QUIT"
}

def customization():
    """Create the Character Customization Screen"""
    # pylint: disable=R0801
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    orig = DinoSprite()
    group = pygame.sprite.Group(orig)
    orig.state = "still"

    skin1 = DinoSprite()
    skin1.change_skin(2)
    group.add(skin1)
    skin1.state = "still"
    skin1.rect.x = skin1.rect.x + 300

    skin2 = DinoSprite()
    skin2.change_skin(1)
    group.add(skin2)
    skin2.state = "still"
    skin2.rect.x = skin1.rect.x + 300

    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.SysFont('impact', 35)

    magenta = (255, 125, 215)
    white = (240, 240, 240)
    text_choose = font.render('Choose Your Character', True, white)
    text_q = font.render('Q', True, magenta)
    text_w = font.render('W', True, magenta)
    text_e = font.render('E', True, magenta)
    # screen.blit(text, (15, 15))
    # text_rect = text.get_rect()
    # text_rect.center = (orig.rect.x, orig.rect.y + 200)

    blink = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key in CUSTOMIZATION_KEY_OPTIONS:
                running = False
                if CUSTOMIZATION_KEY_OPTIONS[event.key] == "QUIT":
                    pygame.quit()
                return CUSTOMIZATION_KEY_OPTIONS[event.key]
            if event.type == pygame.QUIT:
                running = False
                return CUSTOMIZATION_KEY_OPTIONS[pygame.K_ESCAPE]
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_e]:
        #     screen.blit()

        group.update()
        # screen.blit(text, text_rect)
        screen.fill(BACKGROUND_COLOR)
        if blink:
            screen.blit(text_choose, (20, 20))
        screen.blit(text_q, (orig.rect.centerx, orig.rect.bottom + 15))
        screen.blit(text_w, (skin1.rect.centerx, skin1.rect.bottom + 15))
        screen.blit(text_e, (skin2.rect.centerx, skin2.rect.bottom + 15))
        blink = not blink

        group.draw(screen)
        pygame.display.update()
        clock.tick(1)
if __name__ == "__main__":
    customization()
