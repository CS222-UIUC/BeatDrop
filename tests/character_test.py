import pygame
import pytest
import sys

sys.path.insert(1, '..//course-project-group-84//src')

from character import DinoSprite


@pytest.fixture
def test_init():
    dino = DinoSprite()
    assert dino.index == 0
    assert dino.rect == pygame.Rect(5, 5, 134, 134)

def test_update():
    dino = DinoSprite()
    dino.update()
    assert dino.index == 1
    dino.update()
    assert dino.index == 0

def test_jump_up():
    dino = DinoSprite()
    dino.jump()
    assert dino.rect.y <= 45
