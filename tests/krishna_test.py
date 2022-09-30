import pytest
import sys

sys.path.insert(1, '..//course-project-group-84//src')

import game

@pytest.fixture
def test_init():
    game.initialize()

def test_with_fixture():
    assert game.SCREEN_WIDTH == 800
    assert game.SCREEN_HEIGHT == 600
