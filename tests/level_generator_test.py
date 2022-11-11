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

def test_generate_level():
    load_path = os.path.join("tests", "test_file.wav")

    # beat_type = 0
    actual = level_generator.generate_level(load_path, beat_type=0, min_onset_strength=0.3, min_onset_distance=0.75)
    expected = np.load("tests/tick_0_level.npy")
    print(expected, actual)
    assert (expected == actual).all()

    # beat_type = 1
    actual = level_generator.generate_level(load_path, beat_type=1, min_onset_strength=0.3, min_onset_distance=0.75)
    expected = np.load("tests/tick_1_level.npy")
    assert (expected == actual).all()

    # beat_type = 2
    actual = level_generator.generate_level(load_path, beat_type=2, min_onset_strength=0.3, min_onset_distance=0.75)
    expected = np.load("tests/tick_2_level.npy")
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