import pytest
import sys

sys.path.insert(1, '..//course-project-group-84//src')

import librosa
from beat_tracker_utils import *

@pytest.fixture
def test_beat_timestamps():
    y, sr = librosa.load('./assets/example_music.wav')
    beat_times = beat_timestamps(y, sr)
    return beat_times[0]

@pytest.fixture
def test_onset_strength_timestamps():
    y, sr = librosa.load('./assets/example_music.wav')
    times, onset_env = onset_strength_timestamps(y, sr)
    return times[0], onset_env[0]

def test_with_fixture(test_beat_timestamps, test_onset_strength_timestamps):
    assert test_beat_timestamps < 3.0 and test_beat_timestamps > 2.0
    time, onset_env = test_onset_strength_timestamps
    assert time < 0.5
    assert onset_env < 0.5
