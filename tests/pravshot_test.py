import pytest
import sys

from src.game import SCREEN_HEIGHT

sys.path.insert(1, '..//course-project-group-84//src')

import librosa
import time
# from algorithm import *
from score import *
from platforms import *
from game import *

# @pytest.fixture
# def test_beat_timestamps():
#     y, sr = librosa.load('./assets/example_music.wav')
#     beat_times = beat_timestamps(y, sr)
#     return beat_times[0]

# @pytest.fixture
# def test_onset_strength_timestamps():
#     y, sr = librosa.load('./assets/example_music.wav')
#     times, onset_env = onset_strength_timestamps(y, sr)
#     return times[0], onset_env[0]

# def test_with_fixture(test_beat_timestamps, test_onset_strength_timestamps):
#     assert test_beat_timestamps < 3.0 and test_beat_timestamps > 2.0
#     time, onset_env = test_onset_strength_timestamps
#     assert time < 0.5
#     assert onset_env < 0.5

# def test_algorithm():
#     y, sr = librosa.load('./assets/example_music.wav')
#     gaps = get_gaps_from_audio(y, sr, 0.3, 0.75) 
#     assert np.allclose(get_gaps_from_audio(y, sr, -0.3, 1.75), get_gaps_from_audio(y, sr, 0.1, 1.75), atol=0.1)
#     assert np.allclose(get_gaps('./assets/example_music.wav'), gaps)
#     assert len(gaps.shape) > 1
#     gap_timestamps, gap_strengths = gaps[0], gaps[1]
#     assert np.all(gap_strengths > 0.3)

def test_score():
    score = Score()
    time.sleep(1)
    assert score.get_score() == 0
    score.start_timer()
    time.sleep(1)
    assert score.get_score() > 0 and score.get_score() < 2
    score.stop_timer()
    current_score = score.get_score()
    time.sleep(2)
    assert score.get_score() == current_score
    
def test_platforms():
    platform1 = Platform(start_x=0, width=100)
    platform2 = Platform(start_x=100, end_x=300)
    assert Platform.HEIGHT > 0 and Platform.HEIGHT < SCREEN_HEIGHT
    assert len(Platform.COLOR) == 3
    assert Platform.COLOR[0] >= 0 and Platform.COLOR[0] <= 255
    assert Platform.COLOR[1] >= 0 and Platform.COLOR[1] <= 255
    assert Platform.COLOR[2] >= 0 and Platform.COLOR[2] <= 255
    assert platform1.get_x() == 0
    assert platform2.get_x() == 100
    assert platform1.get_y() == SCREEN_HEIGHT - Platform.HEIGHT
    assert platform2.get_y() == SCREEN_HEIGHT - Platform.HEIGHT
    assert platform1.get_width() == 100
    assert platform2.get_width() == 200
    assert platform1.get_end_x() == 100
    assert platform2.get_end_x() == 300
    assert platform1.move_left(10) == -10
    assert platform1.get_x() == -10
    assert platform2.move_left(-10) == 110
    assert platform2.get_x() == 110

def test_platform_controller():
    pc = PlatformController('./tests/test_gaps_file.npy')
    platforms = pc.platforms
    assert pc.last_update_time == 0
    assert pc.finished == False
    assert len(platforms) == 4
    assert platforms[0].get_x() == 0
    pc.start_timer()
    time.sleep(1)
    pc.update()
    assert pc.last_update_time > 0
    assert len(pc.platforms) < 4
    pc.stop_timer()
    assert pc.finished == True
    
    