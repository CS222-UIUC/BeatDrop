"""Provides audio beat analysis using librosa.

For use in CS 222 Group 84, "Beat Drop." Beat Drop relies heavily on audio
analysis to generate the game levels. These functions provide these features,
including tempo and beat detection.
"""
import librosa

def get_beat_info(filename):
    """ Estimates the beat times in a given audio file.

    Args:
        filename (string): Path to audio file to identify beats from.

    Returns:
        float: Audio tempo in bpm.
        np.ndarray: Beat times in milliseconds.
    """
    audio, sample_rate = librosa.load(filename)

    tempo, beat_frames = librosa.beat.beat_track(y=audio, sr=sample_rate)
    beat_times = librosa.frames_to_time(beat_frames, sr=sample_rate)
    return tempo, beat_times
