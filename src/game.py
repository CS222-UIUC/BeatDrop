"""Initialize Pygame"""
#pylint: disable=no-member
#pylint: disable=trailing-whitespace
#pylint: disable=too-few-public-methods
#pylint: disable=too-many-locals
import random
import pygame

from pygame import mixer

SCREEN_WIDTH = 1333
SCREEN_HEIGHT = 533

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
COLOR_LIST = [RED, GREEN, BLUE]

#Class Cloud
class Cloud:
    """Initialize Cloud Class"""
    cloud_image = pygame.image.load('assets/cloud3.png')
    cloud = pygame.transform.scale(cloud_image, (SCREEN_WIDTH/6.5, SCREEN_HEIGHT/6.5))
    cloud_x = 0
    cloud_y = 0
    cloud_x_change = 0.5
    
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

    #Create Background Music
    mixer.music.load('assets/sample_audio_files/righteous.ogg')
    mixer.music.play(-1)
    
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
    
    #Score
    score_val = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
    text_x = 10
    test_y = 10
    flash = False
    color_index = 0
    
    #Default Game Loop
    running = True
    while running:
        #Clock/Time
        clock = pygame.time.get_ticks() 
        
        screen.fill((0, 0, 0))
        #Background Image
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #Update and Display Score
        if (flash is False):
            score_val += 1
        score = font.render("Score: " + str(score_val), True, (255, 255, 255))
        screen.blit(score, (text_x, test_y))            
        if (score_val % 1000 == 0):
            flash = True
            if (color_index == 2):
                color_index = 0
                flash = False
            score = font.render("Score: " + str(score_val), True, COLOR_LIST[color_index])
            screen.blit(score, (text_x, test_y))
            color_index += 1
             

        #Update Cloud Graphics/Position
        copy = list_of_clouds.copy()
        for cloud in copy:
            screen.blit(cloud.cloud, (cloud.cloud_x, cloud.cloud_y))

        #Change Cloud X Position and Check if Cloud is Off Screen
        for cloud in copy:
            cloud.move_left()
            if cloud.cloud_x <= 0 - SCREEN_WIDTH/6.5:
                cloud.cloud_x = 1333
                cloud.cloud_y = random.randint(30, 220)

        pygame.display.update()        

def main() :
    """Main Method"""
    initialize()   
if __name__ == "__main__":
    main()
