import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = pygame.Color('white')
FPS = 10

# class for dino sprite
class DinoSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(DinoSprite, self).__init__()
        #adding all the images to sprite array
        self.images = []
        self.images.append(pygame.image.load('./assets/dino0.png'))
        self.images.append(pygame.image.load('./assets/dino1.png'))

        #index value to get the image from the array
        self.index = 0
        self.image = self.images[self.index]

        # creating a rect at position x,y (5,5) of size (134,134)
        self.rect = pygame.Rect(5, 5, 134, 134)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dino_sprite = DinoSprite()
    group = pygame.sprite.Group(dino_sprite)

    clock = pygame.time.Clock()

    while True:
        event = pygame.event.get()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        group.update()
        screen.fill(BACKGROUND_COLOR)
        group.draw(screen)
        pygame.display.update()
        clock.tick(10)
if __name__ == "__main__":
    main()