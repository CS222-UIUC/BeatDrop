"""Determines platform gaps from audio beats.

Our algorithm to determine where to place gaps in the platforms."""
# pylint: disable=E0401
import numpy as np
import matplotlib.pyplot as plt

import audio_analysis

def generate_level(load_path, save_path="", beat_type=2, min_onset_strength=0.3,
    min_onset_gap=0.75):
    """Generates level and outputs to file.

    Args:
        load_path (string): Path to audio file to identify beats from.
        save_path (string, optional): Path to save to. Will not export data if not provided.
        beat_type (int, optional): Whether to use beats (0), onset (1), or blend (2). Defaults to 2.
        min_onset_strength (float, optional): Defaults to 0.3.
            Minimum onset strength to be considered for a gap.
        min_onset_gap (float, optional): Defaults to 0.75.
            Minimum time between gaps.
    Returns:
        np.ndarray: 2d array with gap timestamps and lengths
    """
    gaps = get_gaps(load_path, beat_type, min_onset_strength, min_onset_gap)
    if not save_path:
        save_to_file(save_path, gaps)
    return gaps

def get_gaps(load_path, beat_type, min_onset_strength, min_onset_gap):
    """Get gaps for each platform from given audio file filename.

    Args:
        load_path (string): Path to audio file to identify beats from.
        beat_type (int, optional): Whether to use beats (0), onset (1), or blend (2). Defaults to 2.
        min_onset_strength (float, optional): Minimum onset strength to be considered for a gap.
        min_onset_gap (float, optional): Minimum time between gaps.
    Returns:
        np.ndarray: 2d array with gap timestamps and lengths
    """
    # currently runs only with onset beat_type (beat_type = 1)
    beat_times = audio_analysis.get_beat_info(load_path, beat_type,
        min_onset_strength, min_onset_gap)
    return convert_beats_to_gaps(beat_times)

def convert_beats_to_gaps(beat_times):
    """Converts beat times to level gaps.

    Args:
        beat_times (np.ndarray) Onset times in milliseconds.
    Returns:
        np.ndarray: 2d array with gap timestamps and lengths
    """
    gap_timestamps = np.array([])
    for time in beat_times:
        # dummy conversion; to be replaced with something functional with physics engine
        gap_timestamps = np.append(gap_timestamps, time)
    return gap_timestamps

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
    gap_start = 0
    for gap_timestamp, gap_strength in gaps:
        plt.plot([gap_start, gap_timestamp], [0, 0], color='r')
        gap_start = gap_timestamp + 1*gap_strength
    plt.plot([gap_start, gap_start + 2], [0, 0], color='r')
    return plt

def main():
    """Main function.
    """
    gaps = get_gaps('./assets/sample_audio_files_break_free_cut.ogg', beat_type=2,
        min_onset_strength=0.4, min_onset_gap=1)
    visualize_gaps(gaps)

if __name__ == "__main__":
    main()
