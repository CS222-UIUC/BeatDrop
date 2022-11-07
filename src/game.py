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
#pylint: disable=too-many-function-args
#pylint: disable=unused-import
import random
import sys
import pygame

from pygame import mixer
sys.path.insert(1, '..//course-project-group-84//src')
import game_over_scene
import score
import level_generator
import platforms
import cloud
import button

#Global Variables
SCREEN_WIDTH = 1333
SCREEN_HEIGHT = 533

RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
COLOR_LIST = [RED, GREEN, BLUE]

GAME_OVER = False

#Start Menu
def start_menu(screen):
    """Start Menu"""
    #Start and Exit Buttons
    start_img = pygame.image.load('assets/start.png').convert_alpha()
    exit_img = pygame.image.load('assets/exit.png').convert_alpha()
    start_button = button.Button(SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 - 60, 
                                 start_img, 0.25,SCREEN_WIDTH, SCREEN_HEIGHT)
    exit_button = button.Button(SCREEN_WIDTH/2 - 130, SCREEN_HEIGHT/2 + 100,
                                exit_img, 0.22, SCREEN_WIDTH, SCREEN_HEIGHT)
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
    mixer.music.load('assets/sample_audio_files/laugh_now_cry_later.ogg')
    
    #Title and Icon
    pygame.display.set_caption("BeatDrop")
    icon = pygame.image.load('assets/gameicon.png')
    pygame.display.set_icon(icon)
        
    #Clouds
    list_of_clouds = []
    cloud_one = cloud.Cloud()
    cloud_two = cloud.Cloud(random.randint(1700, 2000))
    cloud_three = cloud.Cloud(random.randint(2200, 2500))
    list_of_clouds.append(cloud_one)
    list_of_clouds.append(cloud_two)
    list_of_clouds.append(cloud_three)    
    
    #Score
    score_one = score.Score()
    font = pygame.font.Font('freesansbold.ttf', 32)
    text_x = 10
    test_y = 10
    color_index = 0
    flash = False
    
    #Generate Level
    level = level_generator.generate_level(load_path = 
                                           'assets/sample_audio_files/laugh_now_cry_later.ogg',
                                           save_path='assets/level.npy',
                                           min_onset_strength=0.3,
                                           min_onset_gap=0.75)
    
    #Platforms
    platform_controller = platforms.PlatformController(gaps_filepath='assets/level.npy')
    
    #Default Game Loop
    running = True
    start_music = True
    frames = 0
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
            for cloud_obj in copy:
                screen.blit(cloud_obj.cloud, (cloud_obj.cloud_x, cloud_obj.cloud_y))

            #Update Platform Graphics/Position
            if frames % 8 == 0:
                platform_controller.update()
            platform_controller.draw(screen)
            # platform_controller.update()
            frames += 1
            
            #Change Cloud X Position and Check if Cloud is Off Screen
            for cloud_obj in copy:
                cloud_obj.move_left()
                if cloud_obj.cloud_x <= 0 - SCREEN_WIDTH/6.5:
                    cloud_obj.cloud_x = 1333
                    cloud_obj.cloud_y = random.randint(30, 220)

            #Draw other scenes if applicable
            global GAME_OVER
            # if GAME_OVER:
            #     game_over_scene.render(screen)
            #     if button.Button.draw_exit_button(screen):
            #         pygame.quit()
            #         sys.exit()
            #         break

            #Handle Events/Quitting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("EXITED 233")
                    running = False
                    sys.exit(0)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    GAME_OVER = True
            
            pygame.display.update()

def main() :
    """Main Method"""
    initialize()   
if __name__ == "__main__":
    main()
