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
#pylint: disable=R1703

import random
import sys

import pygame
from pygame import mixer

sys.path.insert(1, '..//course-project-group-84//src')
import button
import customization_screen
import cloud
import quit_scene
import level_generator
import platforms
import score
from character import DinoSprite

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

#Choose Song Menu
def choose_song(screen):
    """Choose Song Menu"""
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    
    input_rect = pygame.Rect(200, 200, 140, 32)
    
    color_active = pygame.Color('purple')
    
    color_passive = pygame.Color('gray15')
    color = color_passive
    
    active = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
        
        screen.fill((0, 128, 255))
    
        if active:
            color = color_active
        else:
            color = color_passive
            
        pygame.draw.rect(screen, color, input_rect)
    
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        
        screen.blit(text_surface, (input_rect.x+SCREEN_WIDTH/4, input_rect.y+SCREEN_HEIGHT/4))
        
        input_rect.w = max(100, text_surface.get_width()+10)
        
        pygame.display.flip()
        
    return True

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

    #Create Background Music and Sound Effects
    mixer.music.load('assets/sample_audio_files/tick.wav')
    mixer.music.set_volume(0.5)
    score_sound = mixer.Sound('assets/sample_audio_files/score.ogg')
    score_sound.set_volume(0.25)
    
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
                                           'assets/sample_audio_files/tick.wav',
                                           save_path='assets/level.npy',
                                           min_onset_strength=0.3,
                                           min_onset_distance=0.5)
    
    #Platforms
    platform_controller = platforms.PlatformController(gaps_filepath='assets/level.npy')
    
    #Default Game Loop
    running = True
    start_music = True
    frames = 0
    #choose_song(screen)
    if start_menu(screen):
        # _choice = customization_screen.customization() # do something with choice
        # if _choice == "QUIT":
        #     return
            
        # game loop
        score_one.start_timer()
        platform_controller.start_timer()
        # initialize character
        character = DinoSprite()
        # update character skin to user's choice
        # character.change_skin(_choice)
        sprite_group = pygame.sprite.Group(character)
            
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
                pygame.mixer.Sound.play(score_sound)
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

            #Update Character
            if frames % 4 == 0:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    character.smooth_jump()
                sprite_group.update()
            sprite_group.draw(screen)
            
            #Change Cloud X Position and Check if Cloud is Off Screen
            for cloud_obj in copy:
                cloud_obj.move_left()
                if cloud_obj.cloud_x <= 0 - SCREEN_WIDTH/6.5:
                    cloud_obj.cloud_x = 1333
                    cloud_obj.cloud_y = random.randint(30, 220)

            #Draw other scenes if applicable
            global GAME_OVER
            if platform_controller.finished:
                quit_scene.render_win_scene(screen)
                if button.Button.draw_exit_button(screen):
                    pygame.quit()
                    sys.exit()
                    break
            elif GAME_OVER:
                quit_scene.render_game_over_scene(screen)
                if button.Button.draw_exit_button(screen):
                    pygame.quit()
                    sys.exit()
                    break

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
