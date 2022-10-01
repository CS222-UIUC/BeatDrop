"""Music visualizer using pygame.

Visualizes music beats using elementary pygame display tools. This file will
likely be heavily modified or deprecated in favor of more complex features. As
it stands, it functions as a foreshadowing of the audio-based game mechanics
of Beat Drop and potential graphical features.
"""
from random import randint
from pygame import mixer, display, color, draw, Rect, time

import audio_analysis

def play_music(filename, volume):
    """Plays music using pygame's mixer.

    Args:
        filename (string): Path to audio file to identify beats from.
        volume (float): Volume level, between 0 and 1 inclusive.
    """
    # check volume within [0,1]"
    if volume < 0 or volume > 1:
        raise ValueError("{volume} is invalid volume level. Must be between 0"
            "and 1, inclusive.")

    # play music
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(volume)
    mixer.music.play()

def prepare_audio(sample_idx, volume=1):
    """Gets audio beat info and plays audio.

    Args:
        sample_idx (int): Sample audio file index.
        volume (float): Volume level, between 0 and 1 inclusive.

    Returns:
        float: Audio tempo in bpm.
        np.ndarray: Beat times in milliseconds.
    """
    directory = "assets/sample_audio_files/"
    sample_audio_files = ["break_free.ogg", "tick.wav"]

    # check volume within [0,1]"
    if sample_idx < 0 or sample_idx > len(sample_audio_files):
        raise ValueError("{sample_idx} is invalid sample audio index.")

    filename = directory + sample_audio_files[sample_idx]

    tempo, beat_times = audio_analysis.get_beat_info(filename)
    play_music(filename, volume)
    return tempo, beat_times

def get_current_time(start_ticks):
    """Returns the runtime in seconds since starting main loop.

    Args:
        start_ticks (float): Number of ticks at start of main loop.

    Returns:
        float: Time progressed since start in seconds.
    """
    return (time.get_ticks() - start_ticks) / 1000

def next_beat(beat_idx, beat_times, start_ticks):
    """Returns true if the next beat has passed.

    Args:
        beat_idx (int): Index of the next beat in beat_times.
        beat_times (np.ndarray): Beat times in milliseconds.
        start_ticks (float): Number of ticks at start of main loop.

    Returns:
        bool: Whether or not the next beat has passed.
    """
    if beat_idx >= len(beat_times):
        return False

    return get_current_time(start_ticks) > beat_times[beat_idx]

def draw_random_color_rect(screen, size):
    """Draws a randomly-colored rectangle in the top-left corner.

    Args:
        screen (_type_): Surface to draw on.
        size (int): Width/Length of the rectangle.
    """
    # pylint: disable=I1101
    rand_color = color.Color(randint(0, 255), randint(0, 255), randint(0, 255))
    draw.rect(screen, rand_color, Rect(0,0,size,size))
    display.flip()

def main_loop(screen, tempo, beat_times):
    """Main loop.

    Args:
        screen (pygame.display): Surface to draw on.
        beat_times (np.ndarray): Beat times in milliseconds.
    """
    clock = time.Clock()
    start_offset = 0.1 * tempo
    start_ticks = time.get_ticks() + start_offset
    beat_idx = 0

    while True:
        if next_beat(beat_idx, beat_times, start_ticks):
            draw_random_color_rect(screen, size=40)
            beat_idx += 1

        if not mixer.music.get_busy():
            break

        clock.tick(60)

def main():
    """Visualizes audio beats.
    """
    tempo, beat_times = prepare_audio(1)
    screen = display.set_mode((640, 480))
    main_loop(screen, tempo, beat_times)

if __name__ == '__main__':
    main()
