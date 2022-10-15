import pytest
import sys

sys.path.insert(1, '..//course-project-group-84//src')

import librosa
# from algorithm import *

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