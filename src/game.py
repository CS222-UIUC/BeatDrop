"""Initialize Pygame"""
#pylint: disable=no-member
#pylint: disable=trailing-whitespace
#pylint: disable=too-few-public-methods
import random
import pygame

SCREEN_WIDTH = 1333
SCREEN_HEIGHT = 533

#Class Cloud
class Cloud:
    """Initialize Cloud Class"""
    cloud_image = pygame.image.load('assets/cloud3.png')
    cloud = pygame.transform.scale(cloud_image, (SCREEN_WIDTH/6.5, SCREEN_HEIGHT/6.5))
    cloud_x = 0
    cloud_y = 0
    cloud_x_change = 0.3
    
    def __init__(self, cloud_x = 1333):
        self.cloud_x = cloud_x
        self.cloud_y = random.randint(30, 220)

    def move_left(self):
        """Move Cloud Left"""
        self.cloud_x -= self.cloud_x_change

#Initialize Pygame
def initialize():
    """Initialize Method"""
    pygame.init()

    #Create Display
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    #Create Background Variable
    picture = pygame.image.load('assets/background.jpg')
    background = pygame.transform.scale(picture, (SCREEN_WIDTH, SCREEN_HEIGHT))

    #Title and Icon
    pygame.display.set_caption("BeatDrop")
    icon = pygame.image.load('assets/gameicon.png')
    pygame.display.set_icon(icon)

        
    #Clouds
    list_of_clouds = []
    cloud_one = Cloud()
    cloud_two = Cloud(random.randint(1700, 2000))
    cloud_three = Cloud(random.randint(2200, 2500))
    list_of_clouds.append(cloud_one)
    list_of_clouds.append(cloud_two)
    list_of_clouds.append(cloud_three)    
    
    #Default Game Loop
    running = True
    while running:
        screen.fill((0, 0, 0))
        #Background Image
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #Update Cloud Graphics/Position
        for cloud in list_of_clouds:
            screen.blit(cloud.cloud, (cloud.cloud_x, cloud.cloud_y))

        #Change Cloud X Position and Check if Cloud is Off Screen
        for cloud in list_of_clouds:
            cloud.move_left()
            if cloud.cloud_x <= 0 - SCREEN_WIDTH/6.5:
                list_of_clouds.remove(cloud)
                cloud = Cloud()
                list_of_clouds.append(cloud)

        pygame.display.update()        

def main() :
    """Main Method"""
    initialize()   
if __name__ == "__main__":
    main()
