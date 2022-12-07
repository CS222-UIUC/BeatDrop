"""File to deal with the platform logic"""
# pylint: disable=E0401
# pylint: disable=C0103
# pylint: disable=W0611
# pylint: disable=C0200
# pylint: disable=R1716
import time
import pygame
import numpy as np
# from game import SCREEN_HEIGHT, SCREEN_WIDTH
SCREEN_WIDTH = 1333
SCREEN_HEIGHT = 533

class Platform:
    """Class that defines the platform"""
    HEIGHT = 100
    COLOR = (199, 21, 133)
    def __init__(self, start_x, end_x=None, width=None):
        self.x = start_x
        if end_x is None:
            self.width = width
        else:
            self.width = end_x - start_x
        icon = pygame.image.load('assets/grass platform.png')
        self.platform_icon = pygame.transform.scale(icon, (self.width, self.HEIGHT))

    def get_x(self):
        """returns the x position of the platform"""
        return self.x

    def get_y(self):
        """returns the y position of the platform"""
        return SCREEN_HEIGHT - self.HEIGHT

    def get_width(self):
        """returns the width of the platform"""
        return self.width

    def get_end_x(self):
        """returns the x position of the end of the platform(the right side)"""
        return self.x + self.width
    def get_top_y(self):
        """returns the y position of the top of the platform"""
        return self.get_y() - self.HEIGHT

    def move_left(self, x_amount):
        """moves the platform left and returns the new x position"""
        self.x -= x_amount
        return self.x

    def draw(self, screen):
        """draws the platform on the screen"""
        # pygame.draw.rect(screen, self.COLOR,
        #                  (self.get_x(), self.get_y(), self.get_width(), self.HEIGHT))
        screen.blit(self.platform_icon, (self.get_x(), self.get_y()))

    def is_within(self, x_coord):
        """checks if the given x coordinate is within the platform"""
        return self.x <= x_coord <= self.get_end_x()


class PlatformController:
    """Class that controls the platforms and deals with platform logic"""
    SECS_PER_CYCLE = 4
    CHARACTER_X_OFFSET = 100

    def __init__(self, gaps_filepath):
        """initializes the platform controller with the given npy file"""
        self.platforms = []
        self._initialize_platforms(gaps_filepath)
        self.last_update_time = 0
        self.finished = False
        # print(self.platforms)

    def _initialize_platforms(self, gap_filepath):
        """initializes the platforms from the given npy file"""
        gaps = np.load(gap_filepath)
        # assume gaps is a N x 2 array where N is the number of gaps
        # first column is start time of gap, second column is time length of gap
        start_time = 0
        for i in range(2,len(gaps)):
            gap_start_time = gaps[i][0]
            gap_length_time = gaps[i][1]
            self._create_platform(start_time, gap_start_time)
            start_time = gap_start_time + gap_length_time
        self._create_platform(start_time, start_time + self.SECS_PER_CYCLE)

    def _create_platform(self, start_time, end_time):
        """creates a platform from start_time to end_time"""
        start_x = self._convert_time_to_x(start_time) + self.CHARACTER_X_OFFSET
        end_x = self._convert_time_to_x(end_time) + self.CHARACTER_X_OFFSET
        self.platforms.append(Platform(start_x, end_x=end_x))

    def draw(self, screen):
        """Draws the platforms on the given screen."""
        #Only draws platforms that are within screen width
        for platform in self.platforms:
            if platform.get_x() < SCREEN_WIDTH:
                platform.draw(screen)
            else:
                break

    def update(self):
        """updates the platforms by moving left and dropping off the screen"""
        if self.finished:
            return
        current_time = time.time()
        elapsed_time = current_time - self.last_update_time
        self.last_update_time = current_time
        x_amount = self._convert_time_to_x(elapsed_time)
        for platform in self.platforms:
            platform.move_left(x_amount)
        while len(self.platforms) > 0 and self.platforms[0].get_end_x() < 0:
            self.platforms.pop(0)
        if len(self.platforms) == 0:
            self.finished = True

    def start_timer(self):
        """starts the timer"""
        self.last_update_time = time.time()

    def stop_timer(self):
        """stops the timer"""
        self.finished = True

    def _convert_time_to_x(self, time_stamp):
        """converts time to x position"""
        return int(time_stamp * SCREEN_WIDTH / self.SECS_PER_CYCLE)

    def character_within_platform(self, character):
        """checks if the character x-pos is within a platform"""
        for platform in self.platforms:
            if platform.get_x() > self.CHARACTER_X_OFFSET:
                break
            if platform.is_within(self.CHARACTER_X_OFFSET):
                # if (platform.get_top_y() + 5) > character.rect.bottom or (platform.get_top_y() -5 < character.rect.bottom):
                character.ground_lvl = platform.get_top_y()
                # return True
            else:
                character.ground_lvl = 500
        # return False

                    
    