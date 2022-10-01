import pygame
import pytest
import sys

sys.path.insert(1, '..//course-project-group-84//src')

from src.character import DinoSprite
from src.character import main

@pytest.fixture
def test_init():
    dino = DinoSprite()
    assert dino.index == 0
    assert dino.rect == pygame.Rect(5, 5, 134, 134)

def test_update():
    dino = DinoSprite()
    dino.update()
    assert dino.index == 1
    # dino.update()
    # assert dino.index == 0
