"""Test cases for musicvisualizer/visualizer.
"""
import pygame
import pytest

import sys
sys.path.insert(1, '..//course-project-group-84//src')

import visualizer

@pytest.fixture
def sample_audio_filename():
    return "assets/sample_audio_files/tick.wav"

def test_play_music_plays(sample_audio_filename):
    visualizer.play_music(sample_audio_filename, 0)
    assert pygame.mixer.music.get_busy()

def test_play_music_volume(sample_audio_filename):
    with pytest.raises(Exception):
        visualizer.play_music(sample_audio_filename, -1)
    with pytest.raises(Exception):
        visualizer.play_music(sample_audio_filename, 1.1)

def test_prepare_audio():
    with pytest.raises(Exception):
        visualizer.prepare_audio(-1)
    with pytest.raises(Exception):
        visualizer.prepare_audio(100)

def test_get_current_time():
    start_ticks = pygame.time.get_ticks()
    wait_time = 10
    pygame.time.wait(wait_time)

    assert visualizer.get_current_time(start_ticks)  - wait_time < 0.01

def test_next_beat():
    # note: this test may be a little iffy since times are not exact.
    beat_idx = 0
    beat_times = [0.011]
    start_ticks = pygame.time.get_ticks()

    pygame.time.wait(10)
    print("44", visualizer.get_current_time(start_ticks))
    assert visualizer.next_beat(beat_idx, beat_times, start_ticks) == False

    pygame.time.wait(1)
    print("48", visualizer.get_current_time(start_ticks))
    assert visualizer.next_beat(beat_idx, beat_times, start_ticks) == True

    beat_idx += 1
    assert visualizer.next_beat(1, beat_times, start_ticks) == False