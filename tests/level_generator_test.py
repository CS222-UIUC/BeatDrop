"""Test cases for level generation.
"""
import librosa
import numpy as np
import os
import pytest

import sys
sys.path.insert(1, '..//course-project-group-84//src')

import audio_analysis
import level_generator

def convert_times_strength_tuple_to_np_array(expected_times, expected_strengths):
    """Converts the tuple of times and strengths returned by audio analysis to
    an np array in the format given by generate_level

    Args:
        expected_times (np.1darray): Expected beat times in milliseconds.
        expected_strengths (np.1darray): Expected normalized beat strengths.
    Returns:
        np.2darray: 2d array with gap timestamps and lengths
    """
    return np.array([[time / 1000, strength] for time, strength in zip(expected_times, expected_strengths)])

def test_generate_level():
    load_path = os.path.join("tests", "test_file.wav")

    # beat_type = 0
    actual = level_generator.generate_level(load_path, beat_type=0, min_onset_strength=0.3, min_onset_gap=0.75)
    expected_times, expected_strengths = audio_analysis.get_beat_info(load_path, beat_type=0, min_onset_strength=0.3, min_onset_gap=0.75)
    expected = convert_times_strength_tuple_to_np_array(expected_times, expected_strengths)
    print(expected, actual)
    assert (expected == actual).all()

    # beat_type = 1
    actual = level_generator.generate_level(load_path, beat_type=1, min_onset_strength=0.3, min_onset_gap=0.75)
    expected_times, expected_strengths = audio_analysis.get_beat_info(load_path, beat_type=1, min_onset_strength=0.3, min_onset_gap=0.75)
    expected = convert_times_strength_tuple_to_np_array(expected_times, expected_strengths)
    assert (expected == actual).all()

    # beat_type = 2
    actual = level_generator.generate_level(load_path, beat_type=2, min_onset_strength=0.3, min_onset_gap=0.75)
    expected_times, expected_strengths = audio_analysis.get_beat_info(load_path, beat_type=2, min_onset_strength=0.3, min_onset_gap=0.75)
    expected = convert_times_strength_tuple_to_np_array(expected_times, expected_strengths)
    assert (expected == actual).all()

def test_visualize_gaps():
    gaps = zip([0], [1])
    fig, axes = level_generator.visualize_gaps(gaps)
    assert len(fig.axes) == 1

def test_save_to_file():
    save_path = os.path.join("tests", "test_save_to_file")
    load_path = save_path + ".npy"
    expected = np.array([i for i in range(10)])
    level_generator.save_to_file(save_path, expected)

    actual = np.load(load_path)
    assert (expected == actual).all()