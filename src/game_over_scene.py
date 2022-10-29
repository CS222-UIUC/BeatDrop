"""Visual tools for a game over screen. Note that this class is only for drawing the screen, not
determining when game over occurs.
"""
#pylint: disable=global-statement
import pygame

DARKEN_AMOUNT = 160
DARKEN_RATE = 1

DARKEN_CURR = 0

def render_text(screen, screen_available):
    """Renders "'Game Over' text

    Args:
        screen (pygame display): Screen to draw on.
        screen_available (bool): If screen is available. This should always be True except when
            running Github actions.
    """
    font = pygame.font.Font('freesansbold.ttf', 32)
    game_over_disp = font.render("Game Over", True, (255, 255, 255))
    game_over_rect = game_over_disp.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    if screen_available:
        screen.blit(game_over_disp, game_over_rect)

def make_darken(size):
    """Make darken effect for screen dimming.

    Args:
        size (tuple of ints): Dimensions of darken effect.
    Returns:
        pygame.Surface: Darkening effect to render.
    """
    global DARKEN_CURR
    darken = pygame.Surface(size, 32)
    darken.set_alpha(DARKEN_CURR)

    if DARKEN_CURR < DARKEN_AMOUNT:
        DARKEN_CURR += DARKEN_RATE
    return darken

def render_darken(screen, screen_available):
    """Dims screen slowly

    Args:
        screen (pygame display): Screen to draw on.
        screen_available (bool): If screen is available. This should always be True except when
            running Github actions.
    """
    darken = make_darken(screen.get_size())
    if screen_available:
        screen.blit(darken, (0, 0))

def render(screen, screen_available=True):
    """Draws a gameover overlay.

    Args:
        screen (pygame): Screen to draw on.
        screen_available (bool): If screen is available. This should always be True except when
            running Github actions. Defaults to True.
    """
    render_darken(screen, screen_available)
    render_text(screen, screen_available)
    