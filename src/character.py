"""Initialize Pygame"""
#from math import fabs
import pygame
# pylint: disable=no-member
# pylint: disable=R0903
# pylint: disable=W0612
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = pygame.Color('black')
FPS = 10
INIT_GROUND_LVL = 200
JUMP_SPEED = 25

ACCELERATION = 9
GRAVITY = 2

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
        skin_val = "Q"
        self.change_skin(skin_val)

        #index value to get the image from the array
        self.index = 0
        self.image = self.images[self.index]

        # creating a rect at position x,y (45, ground lvl) of size (100,100)
        self.rect = pygame.Rect(45, self.ground_lvl, 100, 100)
        
        self.vel_y = 0
        self.continuous_jump = 0
    
    def change_skin(self, skin):
        """Change the character's skin"""
        self.images = []
        if skin == "Q": # duck skin
            for i in range(20):
                orig_img = pygame.image.load('./assets/duck3.png')
                self.images.append(pygame.transform.scale(orig_img, (100, 100)))
            for i in range(20):
                orig_img = pygame.image.load('./assets/duck0.png')
                self.images.append(pygame.transform.scale(orig_img, (100, 100)))
            for i in range(20):
                orig_img = pygame.image.load('./assets/duck1.png')
                self.images.append(pygame.transform.scale(orig_img, (100, 100)))
            for i in range(20):
                orig_img = pygame.image.load('./assets/duck2.png')
                self.images.append(pygame.transform.scale(orig_img, (100, 100)))
        else: # default skin
            orig_img = pygame.image.load('./assets/dino0.png')
            self.images.append(pygame.transform.scale(orig_img, (100, 100)))
            orig_img = pygame.image.load('./assets/dino1.png')
            self.images.append(pygame.transform.scale(orig_img, (100, 100)))

   
    def update(self):
        """Update the sprite"""
        if self.state == "running":
            self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        
        # update the velocity and position of rect
        self.update_y(GRAVITY)
        print('vel_y', self.vel_y)
        print('continuous_jump', self.continuous_jump)
    
    def update_y(self, y_accel):
        """Update the y pos and vel"""
        self.vel_y += y_accel
        self.rect.y += self.vel_y
        if self.rect.y > self.ground_lvl:
            self.rect.y = self.ground_lvl
            self.vel_y = 0
    
    def smooth_jump(self):
        """Does smooth parabolic jump"""
        if self.vel_y == 0:
            self.continuous_jump = 0
            self.update_y(-ACCELERATION)
        elif self.vel_y < 0:
            self.update_y(-min(self.continuous_jump*ACCELERATION/5, ACCELERATION))
        self.continuous_jump += 1
    
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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.KEYDOWN:
                # if dino_sprite.vel_y == 0 and event.key == pygame.K_SPACE:
                #     dino_sprite.smooth_jump()
                # if event.key == pygame.K_SPACE:
                    # dino_sprite.smooth_jump()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            dino_sprite.smooth_jump()
            dino_sprite.state = "jumping"
        # jump_limit = dino_sprite.ground_lvl - 100
        # keys = pygame.key.get_pressed()

        # # press key , if not fall_lock'ed and within jump_limit -> set state to jump
        # # if key is released while in jump state, set state to falling, turn on fall_lock
        # # if it touches the platform, set state to running, turn off fall_lock

        # if keys[pygame.K_SPACE] and dino_sprite.rect.y > jump_limit and not dino_sprite.fall_lock:

        group.update()
        screen.fill(BACKGROUND_COLOR)
        group.draw(screen)
        pygame.display.update()
        clock.tick(10)
if __name__ == "__main__":
    main()
    