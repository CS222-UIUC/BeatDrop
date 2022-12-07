"""Determines platform gaps from audio beats.

Our algorithm to determine where to place gaps in the platforms."""
# pylint: disable=E0401
import numpy as np
import matplotlib.pyplot as plt

import audio_analysis

# constants
GAP_STRENGTH_MULTIPLIER = 0.5
MAX_GAP_LENGTH = 0.25
MIN_GAP_LENGTH = 0.05

def generate_level(load_path, save_path="", beat_type=2, min_onset_strength=0.3,
    min_onset_distance=0.75):
    """Generates level and outputs to file.

    Args:
        load_path (string): Path to audio file to identify beats from.
        save_path (string, optional): Path to save to. Will not export data if not provided.
        beat_type (int, optional): Whether to use beats (0), onset (1), or blend (2). Defaults to 2.
        default_beat_strength (float, optional): Beat strength for non-onset beats. Defaults to 0.5.
            Will be ignored if not using beats or blended.
        min_onset_strength (float, optional): Defaults to 0.3.
            Minimum onset strength to be considered for a gap.
        min_onset_distance (float, optional): Defaults to 0.75.
            Minimum time between gaps.
    Returns:
        np.ndarray: 2d array with gap timestamps in seconds and lengths
    """
    default_beat_strength = 0.5
    gaps = get_gaps(load_path, beat_type, default_beat_strength, min_onset_strength,
        min_onset_distance)
    if save_path != "":
        save_to_file(save_path, gaps)
    return gaps

def get_gaps(load_path, beat_type, default_beat_strength, min_onset_strength, min_onset_distance):
    """Get gaps for each platform from given audio file filename.

    Args:
        load_path (string): Path to audio file to identify beats from.
        beat_type (int, optional): Whether to use beats (0), onset (1), or blend (2). Defaults to 2.
        default_beat_strength (float, optional): Beat strength for non-onset beats. Defaults to 0.5.
            Will be ignored if not using beats or blended.
        min_onset_strength (float, optional): Minimum onset strength to be considered for a gap.
        min_onset_distance (float, optional): Minimum time between gaps.
    Returns:
        np.ndarray: 2d array with gap timestamps in seconds and lengths
    """
    beat_times, beat_strengths = audio_analysis.get_beat_info(load_path, beat_type,
        default_beat_strength, min_onset_strength, min_onset_distance)
    return convert_beats_to_gaps(beat_times, beat_strengths, min_onset_distance)

def convert_beats_to_gaps(beat_times, beat_strengths, min_onset_distance):
    """Converts beat times to level gaps.

    Args:
        beat_times (np.ndarray): Beat times in milliseconds.
        beat_strengths (np.ndarray): Normalized beat strengths.
    Returns:
        np.ndarray: 2d array with gap timestamps in seconds and lengths
    """
    gaps = np.array([])
    for time, strength in zip(beat_times, beat_strengths):
        # dummy conversion; to be replaced with something functional with physics engine
        gaps = np.append(gaps,
            np.array([time, onset_strength_to_gap_strength(strength, min_onset_distance)]))
    return gaps.reshape((-1,2))

def onset_strength_to_gap_strength(strength, min_onset_distance):
    """converts onset strength to gap strength

    Args:
        strength (float): onset strength
        min_onset_distance (float): minimum gap length

    Returns:
        _type_: gap length
    """

    gap_strength = min(GAP_STRENGTH_MULTIPLIER * strength * min_onset_distance, MAX_GAP_LENGTH)
    gap_strength = max (gap_strength, MIN_GAP_LENGTH)
    return gap_strength

def save_to_file(save_path, gaps):
    """Outputs np.array to given directory using built-in numpy save function.

    Args:
        save_path (string): Path to save to.
        gaps (np.ndarray): 2d array with gap timestamps and lengths
    """
    np.save(save_path, gaps)

def visualize_gaps(gaps):
    """Visualize gaps on a plot.

    Args:
        gaps (np.ndarray): 2d array with timestamps and strengths
    Return:
        matplotlib.pyplot: Gaps visualization
    """
    fig, axes = plt.subplots()

    gap_start = 0
    for gap_timestamp, gap_strength in gaps:
        plt.plot([gap_start, gap_timestamp], [0, 0], color='r')
        gap_start = gap_timestamp + 1*gap_strength
    plt.plot([gap_start, gap_start + 2], [0, 0], color='r')
    return fig, axes
    