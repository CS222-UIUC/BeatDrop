"""Initialize Pygame"""
#from math import fabs
import pygame
# pylint: disable=no-member
# pylint: disable=R0903

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = pygame.Color('white')
FPS = 10
INIT_GROUND_LVL = 200
JUMP_SPEED = 15

# class for dino sprite
class DinoSprite(pygame.sprite.Sprite):
    """Initialize DinoSprite"""
    # pylint: disable=C0303
    # pylint: disable=R0903

    # jump speed
    jump_speed = JUMP_SPEED
    # state: running, jumping, falling, dead
    state = "running"
    fall_lock = False
    # ground level
    ground_lvl = INIT_GROUND_LVL

    def __init__(self):
        super().__init__()
        #adding all the images to sprite array
        self.images = []
        orig_img = pygame.image.load('./assets/dino0.png')
        self.images.append(pygame.transform.scale(orig_img, (100, 100)))
        orig_img = pygame.image.load('./assets/dino1.png')
        self.images.append(pygame.transform.scale(orig_img, (100, 100)))

        #index value to get the image from the array
        self.index = 0
        self.image = self.images[self.index]

        # creating a rect at position x,y (45, ground lvl) of size (100,100)
        self.rect = pygame.Rect(45, self.ground_lvl, 100, 100)

   
    def update(self):
        """Update the sprite"""
        if self.state == "running":
            self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
    # functions for jumping up and falling
    def jump(self):
        """Jump Up"""
        self.rect.y -= self.jump_speed
    def fall(self):
        """Fall Down"""
        self.rect.y += self.jump_speed   

class Platform(pygame.sprite.Sprite):
    """Create Platform"""
    def __init__(self):
        super().__init__()
        image1 = pygame.image.load('./assets/grass platform.png')
        self.image = pygame.transform.scale(image1, (100,50))
        self.rect = pygame.Rect(50, 300, 100, 50)

def main():
    """Initialize the game"""
    # pylint: disable=R0801
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dino_sprite = DinoSprite()
    group = pygame.sprite.Group(dino_sprite)

    pt1 = Platform()
    # plats = pygame.sprite.Group(pt1)
    group.add(pt1)


    clock = pygame.time.Clock()

    # running = True
    # jumping = 0
    # jumping_counter = 0
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_SPACE]:
    #         jumping = True
    #     if jumping:
    #         if jumping_counter >= 3:
    #             dino_sprite.fall()
    #             jumping = False
    #             jumping_counter = 0
    #         else:
    #             dino_sprite.jump()
    #             jumping_counter += 1
    #     else:
    #         dino_sprite.fall()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        jump_limit = dino_sprite.ground_lvl - 100
        keys = pygame.key.get_pressed()

        # # toggle jump state
        # fall_lock = False
        # if keys[pygame.K_SPACE] and dino_sprite.rect.y >= jump_limit & fall_lock == False:
        #     dino_sprite.state = "jumping"
        # else:
        #     if dino_sprite.rect.y < dino_sprite.ground_lvl:
        #         dino_sprite.state = "falling"
        #         fall_lock = True
        #     else:
        #         dino_sprite.state = "running"

        # # toggle states based on collisions and other factors
        # if dino_sprite.state == "jumping":
        #     # if sprite reaches jump limit, it will start falling
        #     if dino_sprite.rect.y <= jump_limit:
        #         dino_sprite.state = "falling"
        #     else:
        #         dino_sprite.jump()
        # elif dino_sprite.state == "falling":
        #     # if sprite collides with platform, it will stop falling
        #     if dino_sprite.rect.colliderect(pt1):
        #         fall_lock = False
        #         dino_sprite.state = "running"
        #     else:
        #         dino_sprite.fall()

        # press key , if not fall_lock'ed and within jump_limit -> set state to jump
        # if key is released while in jump state, set state to falling, turn on fall_lock
        # if it touches the platform, set state to running, turn off fall_lock

        if keys[pygame.K_SPACE] and dino_sprite.rect.y > jump_limit and not dino_sprite.fall_lock:
            dino_sprite.state = "jumping"
        elif dino_sprite.rect.y <= jump_limit:
            dino_sprite.state = "falling"
            dino_sprite.fall_lock = True
        elif (not keys[pygame.K_SPACE] and dino_sprite.state == "jumping"):
            dino_sprite.state = "falling"
            dino_sprite.fall_lock = True
        elif dino_sprite.rect.bottom == pt1.rect.top:
            dino_sprite.ground_lvl = dino_sprite.rect.y
            print("touching grass: " + str(dino_sprite.rect.bottom) + " " + str(pt1.rect.top))
            dino_sprite.state = "running"
            dino_sprite.fall_lock = False
        elif not dino_sprite.rect.colliderect(pt1):
            print("not")
            dino_sprite.state = "falling"
            dino_sprite.fall_lock = True

        if dino_sprite.state == "jumping":
            dino_sprite.jump()
        if dino_sprite.state == "falling":
            dino_sprite.fall()

        group.update()
        screen.fill(BACKGROUND_COLOR)
        group.draw(screen)
        pygame.display.update()
        clock.tick(10)
if __name__ == "__main__":
    main()
