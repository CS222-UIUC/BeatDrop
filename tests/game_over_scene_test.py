import pygame
import pytest
import sys

from src.quit_scene import DARKEN_RATE

sys.path.insert(1, '..//course-project-group-84//src')
import quit_scene

def test_make_darken():
    size = (640, 480)
    darken = quit_scene.make_darken(size)
    assert darken.get_size() == size
    assert quit_scene.DARKEN_CURR == 0 + DARKEN_RATE