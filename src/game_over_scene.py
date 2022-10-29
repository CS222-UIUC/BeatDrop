"""Visual tools for a game over screen. Note that this class is only for drawing the screen, not
determining when game over occurs.
"""

import pygame

DARKEN_AMOUNT = 160
DARKEN_RATE = 1

DARKEN_CURR = 0

def render_text(screen):
    """Renders "'Game Over' text

    Args:
        screen (pygame display): Screen to draw on
    """
    font = pygame.font.Font('freesansbold.ttf', 32)
    game_over_disp = font.render("Game Over", True, (255, 255, 255))
    game_over_rect = game_over_disp.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(game_over_disp, game_over_rect)

def render_darken(screen):
    """Dims screen slowly

    Args:
        screen (pygame display): Screen to draw on
    """
    global DARKEN_CURR
    print(DARKEN_CURR)
    darken = pygame.Surface(screen.get_size(), 32)

    darken.set_alpha(DARKEN_CURR)
    screen.blit(darken, (0, 0))

    if DARKEN_CURR < DARKEN_AMOUNT:
        DARKEN_CURR += DARKEN_RATE

def render(screen):
    """Draws a gameover overlay.

    Args:
        screen (pygame): Screen to draw on.
    """
    render_darken(screen)
    render_text(screen)
    