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
import random
import sys
import pygame

from pygame import mixer
sys.path.insert(1, '..//course-project-group-84//src')
import game_over_scene
import score
import level_generator
import platforms

SCREEN_WIDTH = 1333
SCREEN_HEIGHT = 533

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
COLOR_LIST = [RED, GREEN, BLUE]

# States
GAME_OVER = False

#Class Button
class Button():
    """Initialize Button Class"""
    def __init__(self, x_pos, y_pos, image, scale):
        self.image = pygame.transform.scale(image,
                                            (int(SCREEN_WIDTH * scale), int(SCREEN_HEIGHT * scale)))
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

#Start Menu
def start_menu(screen):
    """Start Menu"""
    #Start and Exit Buttons
    start_img = pygame.image.load('assets/start.png').convert_alpha()
    exit_img = pygame.image.load('assets/exit.png').convert_alpha()
    start_button = Button(SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 - 60, start_img, 0.25)
    exit_button = Button(SCREEN_WIDTH/2 - 130, SCREEN_HEIGHT/2 + 100, exit_img, 0.22)
    icon = pygame.image.load('assets/gameicon.png')
    icon_load = pygame.transform.scale(icon, (SCREEN_WIDTH/5, SCREEN_HEIGHT/2.5))

    start_game = False
    while start_game is False:
        screen.fill((202, 228, 241))
        screen.blit(icon_load, (SCREEN_WIDTH/2 - 125, SCREEN_HEIGHT/2 - 270))
        if start_button.draw(screen):
            print('START')
            start_game = True
        if exit_button.draw(screen):
            print('EXIT')
            pygame.quit()
        
        for event in pygame.event.get():
            #Quit Game
            if event.type == pygame.QUIT:
                start_game = True
        pygame.display.update()        

    return start_game

#Initialize Pygame
def initialize():
    """Initialize Method"""
    pygame.init()
    
    #Create Display
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("BeatDrop")     

    #Create Background Variable
    picture = pygame.image.load('assets/background.jpg')
    background = pygame.transform.scale(picture, (SCREEN_WIDTH, SCREEN_HEIGHT))

    #Create Background Music
    mixer.music.load('assets/sample_audio_files/break_free_cut.ogg')
    
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
    score_one = score.Score()
    font = pygame.font.Font('freesansbold.ttf', 32)
    text_x = 10
    test_y = 10
    flash = False
    color_index = 0
    
    #Generate Level
    level = level_generator.generate_level(load_path = 
                                           'assets/sample_audio_files/break_free_cut.ogg',
                                           save_path='assets/level.npy')
    
    #Platforms
    platform_controller = platforms.PlatformController(gaps_filepath='assets/level.npy')
    
    #Default Game Loop
    running = True
    start_music = True
    if start_menu(screen):
        score_one.start_timer()
        platform_controller.start_timer()
        while running:
            #Start Music
            if start_music:
                mixer.music.play(-1)
                start_music = False
                
            #Clock/Time
            clock = pygame.time.get_ticks() 
            
            screen.fill((0, 0, 0))
            #Background Image
            screen.blit(background, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            #Update and Display Score
            score_disp = font.render("Score: " + str(score_one.get_score()), True, (255, 255, 255))
            screen.blit(score_disp, (text_x, test_y))
            if score_one.get_score() % 10 == 0 and score_one.get_score() != 0:
                flash = True
                if color_index == 2:
                    color_index = 0
                    flash = False
                score_disp = font.render("Score: " + str(score_one.get_score()),
                                         True, COLOR_LIST[color_index])
                screen.blit(score_disp, (text_x, test_y))
                color_index += 1
            
            #Update Cloud Graphics/Position
            copy = list_of_clouds.copy()
            for cloud in copy:
                screen.blit(cloud.cloud, (cloud.cloud_x, cloud.cloud_y))

            #Update Platform Graphics/Position
            platform_controller.update()
            platform_controller.draw(screen)
            
            #Change Cloud X Position and Check if Cloud is Off Screen
            for cloud in copy:
                cloud.move_left()
                if cloud.cloud_x <= 0 - SCREEN_WIDTH/6.5:
                    cloud.cloud_x = 1333
                    cloud.cloud_y = random.randint(30, 220)

            #Draw other scenes if applicable
            global GAME_OVER
            if GAME_OVER:
                game_over_scene.render(screen)
            
            #Handle Events/Quitting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    GAME_OVER = True
                
            pygame.display.update()        

def main() :
    """Main Method"""
    initialize()   
if __name__ == "__main__":
    main()
