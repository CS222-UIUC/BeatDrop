import pytest
import sys

sys.path.insert(1, '..//course-project-group-84//src')
import level_generator
import platforms
import game
import cloud
import button

@pytest.fixture
def test_init():
    game.initialize()

#Testing Game Dimensions
def test_game_dimensions():
    assert game.SCREEN_WIDTH == 1333
    assert game.SCREEN_HEIGHT == 533

#Testing Cloud Class
def test_cloud_class():
    Cloud = cloud.Cloud()
    assert Cloud.cloud.get_width() == game.SCREEN_WIDTH//6.5
    assert Cloud.cloud.get_height() == game.SCREEN_HEIGHT//6.5
    assert Cloud.cloud_y >= 30
    assert Cloud.cloud_y <= 220
    
def test_colors():
    assert game.RED == (255, 0, 0)
    assert game.GREEN == (0, 255, 0)
    assert game.BLUE == (0, 0, 255)