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