"""Import Statements"""
#pylint: disable=no-member
#pylint: disable=trailing-whitespace
#pylint: disable=too-few-public-methods
#pylint: disable=too-many-locals
#pylint: disable=wrong-import-position
#pylint: disable=import-error
#pylint: disable=unused-variable
#pylint: disable=global-statement
#pylint: disable=too-many-branches
#pylint: disable=too-many-statements
#pylint: disable=too-many-arguments
#pylint: disable=bad-classmethod-argument
import pygame

#Class Button
class Button():
    """Initialize Button Class"""
    def __init__(self, x_pos, y_pos, image, scale, screen_width, screen_height):
        self.image = pygame.transform.scale(image,
                                            (int(screen_width * scale), int(screen_height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.clicked = False    
    def draw(self, screen):
        """Draw button on screen"""
        action = False
        #Mouse Position
        pos = pygame.mouse.get_pos()  
        #Check mouse position and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True                  
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #Draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
    
    @classmethod
    @staticmethod
    def draw_exit_button(screen):
        """Draws an exit button which, upon click, calls quit event.
        Args:
            screen (pygame.display): Screen to draw on.
        Returns:
            bool: If game should quit.
        """
        exit_img = pygame.image.load('assets/exit.png').convert_alpha()
        exit_button = Button(screen.get_width()/2 - 150, 
                             screen.get_height()/2 + 50, 
                             exit_img,
                             0.22,
                             screen.get_width(), 
                             screen.get_height())

        return exit_button.draw(screen)
    