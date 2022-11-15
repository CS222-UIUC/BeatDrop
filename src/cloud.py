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
import pygame

#Class Cloud
class Cloud:
    """Initialize Cloud Class"""
    def __init__(self, cloud_x = 1333, screen_width = 1333, screen_height = 533):
        self.cloud_x = cloud_x
        self.cloud_y = random.randint(30, 220)
        self.cloud_image = pygame.image.load('assets/cloud3.png')
        self.cloud = pygame.transform.scale(self.cloud_image, (screen_width/6.5, screen_height/6.5))
        self.cloud_x_change = 0.5

    def move_left(self):
        """Move Cloud Left"""
        self.cloud_x -= self.cloud_x_change
        