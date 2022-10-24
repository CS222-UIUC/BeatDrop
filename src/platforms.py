"""File to deal with the platform logic"""
# import time
# pylint: disable=E0401
# pylint: disable=C0103
# pylint: disable=W0611
import pygame
from game import SCREEN_HEIGHT, SCREEN_WIDTH

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

    def get_x(self):
        """returns the x position of the platform"""
        return self.x

    def get_y(self):
        """returns the y position of the platform"""
        return SCREEN_HEIGHT - self.HEIGHT

    def get_width(self):
        """returns the width of the platform"""
        return self.width

    def move_left(self, x_amount):
        """moves the platform left and returns the new x position"""
        self.x -= x_amount
        return self.get_x()

    def draw(self, screen):
        """draws the platform on the screen"""
        pygame.draw.rect(screen, self.COLOR,
                         (self.get_x(), self.get_y(), self.get_width(), self.HEIGHT))


# class PlatformController:
#     """Class that controls the platforms and deals with platform logic"""
#     SECS_PER_CYCLE = 4

#     def _convert_time_to_x(self, time):
#         """converts time to x position"""
#         return int(time * SCREEN_WIDTH / self.SECS_PER_CYCLE)
