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

    actual = level_generator.generate_level(load_path, beat_type=1, min_onset_strength=0.3, min_onset_gap=0.75)
    expected = audio_analysis.get_beat_info(load_path, beat_type=1, min_onset_strength=0.3, min_onset_gap=0.75)
    assert (actual == expected).all()

# def test_visualize_gaps():
#     gaps = zip([0], [1])
#     plt = level_generator.visualize_gaps(gaps)
#     assert len(plt.axes()) == 1

def test_save_to_file():
    save_path = os.path.join("tests", "test_save_to_file")
    load_path = save_path + ".npy"
    expected = np.array([i for i in range(10)])
    level_generator.save_to_file(save_path, expected)

    actual = np.load(load_path)
    assert (expected == actual).all()