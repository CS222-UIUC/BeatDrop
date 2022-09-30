# import librosa
from .src import musicvisualizer
import pytest

@pytest.fixture
def get_beat_info_fixture():
    # expected_tempo = 

    filename = librosa.example('nutcracker')
    tempo, beat_times = musicvisualizer.get_beat_info(filename)

    assert tempo == 2

filename = librosa.example('nutcracker')


# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print(beat_times)