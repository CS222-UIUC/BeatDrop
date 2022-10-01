"""Utility functions for beat and onset strength tracking."""
import librosa
import matplotlib.pyplot as plt
import numpy as np
# pylint: disable=W0621
# pylint: disable=C0103

def beat_timestamps(y, sr):
    """get beat timestamps from filename path to song

    Args:
        y (np.ndarray): audio signal
        sr (int): sample rate

    Returns:
        np.ndarray: timestamps of beats
    """
    #pylint: disable=W0612
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    return beat_times

def onset_strength_timestamps(y, sr):
    """finds onset strengths and their timestamps from audio

    Args:
        y (np.ndarray): audio signal
        sr (int): sample rate

    Returns:
        (np.ndarray, np.ndarray): timestamps and onset strengths
    """
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, aggregate=np.median)
    times = librosa.times_like(onset_env, sr=sr)
    return times, librosa.util.normalize(onset_env)


def visualization_plot(y, sr):
    """a visualization plot with onset strength and beat timings

    Args:
        y (np.ndarray): audio signal
        sr (int): sample rate
    Returns:
        plt.Figure: figure object
    """
    # pylint: disable=W0612
    times, onset_env = onset_strength_timestamps(y, sr)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    fig, ax = plt.subplots()
    ax.plot(times, onset_env, label='Onset strength')
    ax.vlines(times[beat_frames], 0, 1, alpha=0.5, color='r', linestyle='--', label='Beats')
    ax.legend()
    plt.show()
    return fig

y, sr = librosa.load('./assets/example_music.wav')
fig = visualization_plot(y, sr)
beat_times = beat_timestamps(y, sr)
print(beat_times)
times, onset_env = onset_strength_timestamps(y, sr)
print(times)
print(onset_env)
# plt.show()
