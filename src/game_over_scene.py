"""Visual tools for a game over screen. Note that this class is only for drawing the screen, not
determining when game over occurs.
"""

import pygame

def render(screen):
    """Draws a gameover overlay.

    Args:
        screen (pygame): Screen to draw on.
    """
    # text
    font = pygame.font.Font('freesansbold.ttf', 32)
    game_over_disp = font.render("Game Over", True, (255, 255, 255))
    game_over_rect = game_over_disp.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

    # screen darken
    darken = pygame.Surface(screen.get_size(), 32)
    darken_amount = 10
    darken_curr = 0

    #Default Game Loop
    running = True
    while running:
        # draw text
        screen.blit(game_over_disp, game_over_rect)        

        # draw darken
        darken.set_alpha(darken_curr / 2)
        if darken_curr < darken_amount:
            darken_curr += 0.1
            screen.blit(darken, (0, 0))
        
        #Handle Events/Quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()      