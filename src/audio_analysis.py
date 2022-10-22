"""Provides audio beat analysis using librosa.

For use in CS 222 Group 84, "Beat Drop." Beat Drop relies heavily on audio
analysis to generate the game levels. These functions provide these features,
including tempo and beat detection.
"""
# pylint: disable=E0401
import librosa
import numpy as np
import matplotlib.pyplot as plt

def get_beat_info(filename, beat_type=2, default_beat_strength=0.5, min_onset_strength=0.3,
    min_onset_gap=0.2):
    """ Estimates the beat times in a given audio file.

    Args:
        filename (string): Path to audio file to identify beats from.
        beat_type (int, optional): Whether to use beats (0), onset (1), or blend (2). Defaults to 2.
        default_beat_strength (float, optional): Beat strength for non-onset beats. Defaults to 0.5.
            Will be ignored if not using beats or blended.
        min_onset_strength (float, optional): Minimum onset threshold. Will be ignored if not using
            onset.
        min_onset_gap (float, optional): Minimum gap between onset spikes. Will be ignored if not
            using onset.

    Returns:
        np.ndarray: Beat times in milliseconds.
        np.ndarray: Normalized beat strengths.
    """
    if beat_type == 0:
        return get_beat_times(filename, default_beat_strength)
    if beat_type == 1:
        return get_onset_times(filename, min_onset_strength, min_onset_gap)
    if beat_type == 2:
        return get_blend_times(filename, default_beat_strength, min_onset_strength, min_onset_gap)
    raise ValueError(f"{beat_type} is an invalid beat type.")

def open_audio(filename):
    """Opens and returns an audio file.

    Args:
        filename (string): Path to audio file to identify beats from.
    Return:
        np.ndarray: Audio time series.
        float: Sampling rate of audio.
    """
    audio, sample_rate = librosa.load(filename)
    return audio, sample_rate

def get_beat_times(filename, default_beat_strength):
    """ Estimates the beat times in a given audio file.

    Args:
        filename (string): Path to audio file to identify beats from.
        default_beat_strength (float): Beat strength for non-onset beats.
    Returns:
        np.ndarray: Beat times in milliseconds.
        np.ndarray: Normalized beat strength.
    """
    audio, sample_rate = open_audio(filename)
    _tempo, beat_frames = librosa.beat.beat_track(y=audio, sr=sample_rate)
    beat_times = librosa.frames_to_time(beat_frames, sr=sample_rate)
    beat_strengths = np.full(beat_times.shape, default_beat_strength)
    return beat_times, beat_strengths

def get_onset_times(filename, min_onset_strength, min_onset_gap):
    """ Estimates the beat times in a given audio file.

    Args:
        filename (string): Path to audio file to identify beats from.
        min_onset_strength (float): Minimum onset threshold. Will be ignored if not using onset.
        min_onset_gap (float): Minimum gap between onset spikes. Will be ignored if not using onset.
    Returns:
        np.ndarray: Onset times in milliseconds.
        np.ndarray: Normalized onset strengths.
    """
    audio, sample_rate = open_audio(filename)
    strengths = np.array(librosa.onset.onset_strength(y=audio, sr=sample_rate, aggregate=np.median))
    times = np.array(librosa.times_like(strengths, sr=sample_rate))
    filtered_times = filter_onset_times(times, strengths, min_onset_strength, min_onset_gap)
    filtered_strengths = strengths[np.isin(times, filtered_times)]
    return filtered_times, filtered_strengths

def filter_onset_times(times, strength, min_onset_strength, min_onset_gap):
    """_summary_

    Args:
        times (np.ndarray): Array of onset times.
        strength (np.ndarray): Array of corresponding strengths to onset times.
        min_onset_strength (float): Minimum onset threshold. Will be ignored if not using onset.
        min_onset_gap (float): Minimum gap between onset spikes. Will be ignored if not using onset.
    Returns:
        np.ndarray: Filtered onset times in millseconds.
    """
    filtered = filter_by_strength(times, strength, min_onset_strength)
    filtered = filter_by_time(filtered, min_onset_gap)
    return filtered

def filter_by_strength(times, strength, min_onset_strength):
    """ Returns a new list of times with minimum strength.

    Args:
        times (np.ndarray): Array of onset times.
        strength (np.ndarray): Array of corresponding strengths to onset times.
        min_onset_strength (float): Minimum onset threshold.
    Returns:
        np.ndarray: Strength-filtered onset times in millseconds.
    """
    return times[strength >= min_onset_strength]

def filter_by_time(times, min_onset_gap):
    """ Returns a new list of times a minimum distance apart.

    Args:
        times (np.ndarray): Array of onset times. Cannot begin with 0.
        min_onset_gap (float): Minimum gap between onset spikes. Will be ignored if not using onset.
    Returns:
        np.ndarray: Time-filtered onset times in millseconds.
    """
    if times[0] == 0:
        raise ValueError("Times cannot begin with 0.")

    filtered = np.array([0])
    for time in times:
        if time - filtered[-1] >= min_onset_gap:
            filtered = np.append(filtered, time)
    return filtered[1:] # remove the temporary zero element

def get_blend_times(filename, default_beat_strength, min_onset_strength, min_onset_gap):
    """ Estimates the beat times in a given audio file using a blend of beat and onset analysis.

    Args:
        filename (string): Path to audio file to identify beats from.
        default_beat_strength (float): Beat strength for non-onset beats.
        min_onset_strength (float): Minimum onset threshold. Will be ignored if not using onset.
        min_onset_gap (float): Minimum gap between onset spikes. Will be ignored if not using onset.

    Returns:
        np.ndarray: Blended times in milliseconds.
        np.ndarray: Normalized blended strenghts.
    """
    beat_times, beat_strengths = get_beat_times(filename, default_beat_strength)
    onset_times, onset_strengths = get_onset_times(filename, min_onset_strength, min_onset_gap)

    return blend_beat_onset_times(beat_times, beat_strengths, onset_times, onset_strengths,
        min_onset_gap)

def blend_beat_onset_times(beat_times, beat_strengths, onset_times, onset_strengths, min_onset_gap):
    """Smartly combines beat and onset times.

    Args:
        beat_times (np.ndarray): Filtered beat times in milliseconds.
        beat_strengths (np.ndarray): Filtered normalized beat strengths.
        onset_times (np.ndarray): Onset times in milliseconds.
        onset_strengths (np.ndarray): Filtered normalized onset strengths.
        min_onset_gap (float): Minimum gap between onset spikes. Will be ignored if not using onset.

    Returns:
        np.ndarray: Blended times in milliseconds.
        np.ndarray: Normalized blended strengths.
    """
    filtered_beat_times, filtered_beat_strengths = filter_beat_times(beat_times,
        beat_strengths, onset_times, min_onset_gap)
    blend_times = np.concatenate((filtered_beat_times, onset_times))
    blend_strenghts = np.concatenate((filtered_beat_strengths, onset_strengths))

    sort_idxs = blend_times.argsort()
    blend_times = blend_times[sort_idxs]
    blend_strenghts = blend_strenghts[sort_idxs]
    return blend_times, blend_strenghts

def filter_beat_times(beat_times, beat_strengths, onset_times, min_onset_gap):
    """ Returns a new array with beat times that have a gap from onset times.

    Args:
        beat_times (np.ndarray): Beat times in milliseconds.
        onset_times (np.ndarray): Onset times in milliseconds.
        min_onset_gap (float): Minimum gap between onset spikes. Will be ignored if not using onset.
    Returns:
        np.ndarray: Filtered beat times in milliseconds.
        np.ndarray: Filtered normalized beat stregnths.
    """
    filtered_beat_times = np.array([beat_time for beat_time in beat_times
        if (abs(beat_time - onset_times) >= min_onset_gap).all()])
    filtered_beat_strengths = beat_strengths[np.isin(beat_times, filtered_beat_times)]
    return filtered_beat_times, filtered_beat_strengths

def visualization_plot(filename):
    """A visualization plot with onset strength, beat timings, and blended beats.

    Args:
        filename (string): Path to audio file to identify beats from.
    Returns:
        plt.Figure: Visualization of beats
    """
    beat_times = get_beat_info(filename, 0)
    onset_times = get_beat_info(filename, 1)
    blend_times = get_beat_info(filename, 2)

    fig, axes = plt.subplots()
    # ax.plot(onset_times, onset_env, label='Onset strength')
    axes.vlines(blend_times, 0, 1, alpha=0.5, color='b', linestyle='-', label='Blended')
    axes.vlines(beat_times, 0, 1, alpha=0.5, color='r', linestyle='--', label='Beats')
    axes.vlines(onset_times, 0, 1, alpha=0.5, color='g', linestyle=':', label='Onsets')
    axes.legend()
    return fig
