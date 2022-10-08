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

# def test_play_music_plays(sample_audio_filename):
#     # this test case cannot be properly run on Github actions because it
#     # requires an audio device. thus, it is commented out for merging.
#     visualizer.play_music(sample_audio_filename, 0)
#     assert pygame.mixer.music.get_busy()

def test_play_music_volume(sample_audio_filename):
    with pytest.raises(Exception):
        visualizer.play_music(sample_audio_filename, -1)
    with pytest.raises(Exception):
        visualizer.play_music(sample_audio_filename, 1.1)

# def test_prepare_audio():
#     # this test case cannot be properly run on Github actions because it
#     # requires an audio device. thus, it is commented out for merging.
#     actual = visualizer.prepare_audio(2)
#     pygame.mixer.music.stop()
#     for i in range(len(actual) - 1):
#         assert actual[i] < actual[i+1]

def test_prepare_audio_illegal_arguments():
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
    # note: because run speeds vary with processor, this test gives room for
    # slight amounts of error
    beat_idx = 0
    beat_times = [0.012]
    start_ticks = pygame.time.get_ticks()

    pygame.time.wait(10)
    print("44", visualizer.get_current_time(start_ticks))
    assert visualizer.next_beat(beat_idx, beat_times, start_ticks) == False

    pygame.time.wait(3)
    print("48", visualizer.get_current_time(start_ticks))
    assert visualizer.next_beat(beat_idx, beat_times, start_ticks) == True

    beat_idx += 1
    assert visualizer.next_beat(1, beat_times, start_ticks) == False

# def test_draw_random_color_rect():
#     screen = pygame.display.set_mode((640, 480))
#     visualizer.draw_random_color_rect(screen, size=20)

# def test_main_loop():
#     # this test case cannot be properly run on Github actions because it
#     # requires an audio device. thus, it is commented out for merging.
#     screen = pygame.display.set_mode((640, 480))
#     beat_times = [0.01, 0.02] # dummy array since we aren't testing next_beat here

#     pygame.mixer.init()
#     start_ticks = pygame.time.get_ticks()
#     visualizer.main_loop(screen, beat_times)

#     expected_time = 1
#     actual_time = visualizer.get_current_time(start_ticks)
#     assert actual_time - expected_time < 0.01
