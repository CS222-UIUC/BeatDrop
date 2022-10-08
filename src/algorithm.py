"""Our algorithm to determine where to place gaps in the platforms."""
# pylint: disable=E0401
# pylint: disable=W0621
# pylint: disable=C0103
# pylint: disable=C0303
import librosa
import numpy as np
import matplotlib.pyplot as plt
from beat_tracker_utils import beat_timestamps, onset_strength_timestamps


def get_gaps(filename, min_onset_strength=0.3, min_time_between_gaps=0.75):
    """get gaps from filepath to audio file

    Args:
        filename (str): path to audio file
        min_onset_strength (float, optional): Defaults to 0.3.
            minimum onset strength to be considered for a gap
        min_time_between_gaps (float, optional): Defaults to 0.75.
            minimum time between gaps
    
    Returns:
        np.ndarray: 2d array with timestamps and strengths
    """
    y, sr = librosa.load(filename)
    return get_gaps_from_audio(y, sr, min_onset_strength, min_time_between_gaps)


def get_gaps_from_audio(y, sr, min_onset_strength, min_time_between_gaps):
    """get gaps from audio

    Args:
        y (np.ndarray): audio
        sr (int): sample rate
        min_onset_strength (float): minimum onset strength to be considered for a gap
        min_time_between_gaps (float): minimum time between gaps
    
    Returns:
        np.ndarray: 2d array with timestamps and strengths
    """
    # pylint: disable=W0612
    min_onset_strength = min(min_onset_strength, 0.9)
    min_onset_strength = max(min_onset_strength, 0.1)
    min_time_between_gaps = min(min_time_between_gaps, 8)
    min_time_between_gaps = max(min_time_between_gaps, 0.2)
    beat_times = beat_timestamps(y, sr)
    times, onset_env = onset_strength_timestamps(y, sr)
    gap_timestamps = []
    gap_strengths = []
    for time, onset_strength in zip(times, onset_env):
        if onset_strength > min_onset_strength:
            if len(gap_timestamps) == 0:
                gap_timestamps.append(time)
                gap_strengths.append(onset_strength)
            elif time - gap_timestamps[-1] > min_time_between_gaps:
                gap_timestamps.append(time)
                gap_strengths.append(onset_strength)
    return np.array([gap_timestamps, gap_strengths])
    
   
def draw_gaps(gaps):
    """draw gaps on a plot

    Args:
        gaps (np.ndarray): 2d array with timestamps and strengths
    """
    gap_timestamps, gap_strengths = gaps[0], gaps[1]
    start = 0
    for gap_timestamp, gap_strength in zip(gap_timestamps, gap_strengths):
        plt.plot([start, gap_timestamp], [0, 0], color='r')
        start = gap_timestamp + 1*gap_strength
    plt.plot([start, start + 2], [0, 0], color='r')
    plt.show()

if __name__ == "__main__":
    # pylint: disable=W0621
    gaps = get_gaps('./assets/example_music.wav', 0.4, 1)
    draw_gaps(gaps)
