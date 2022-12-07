# BeatDrop
## Premise
Beat Drop combines music and games to turn the songs you love into a fun, interactive gaming experience. 

Beat Drop will automatically generate a platformer game by analyzing the beats of a song.

## Pitch
1. Control a character of your choice using the keyboard.
2. Generate a song of your choice and play an auto-generated level to that song. Obstacles (gaps) match the timing of the beats/melodies of the song.
3. Character customization and other bonus features included!

## Alternatives
There's a variety of music-based games and platformer games, but few intersect these two areas. Further, the ones that do lack the ability to auto generate levels. BeatDrop focuses on this niche, providing a novel gaming and musical experience.

# Technical Architecture
Our project is split up into two major sections, beat analysis/level generation and gameplay.

One is beat analysis and level generation. This includes analyzing song/audio files and conducting onset and beat extraction. From there, we specially select where to put our platforms and gaps so that gameplay will match the song. The result of this section is a level description file that we can pass onto the second step of our project: Gameplay.

Gameplay involves all aspects related to actual gameplay such as character movement, platform location, rendering, menu screens/death screens, etc. It is important to note that this part of the project is not playable without the level generation file that we created from the first section. We many popular libraries to create this project; the most notable are NumPy, Librosa, Pygame, and Matplotlib.

# Installation Instructions
1. Clone this repository
2. Install relevant packages using:
```python
pip install numpy pygame librosa soundfile matplotlib
```
3. Use python to run the file `game.py`
4. Add additional songs of your choice in `/assets` as an `.ogg` or `.wav` file.

# Group Members
- Jonathan Gao (Audio Analysis, Level Generation, Victory/Game Over)
- Krishna Konda (Song Selection, Start Menu, Cloud Generation, Background, Score)
- Praveen Kalva (Audio Analysis, Level Generation, Platforms, Score)
- Rachel Shum (Character Selection, Kinematics, Character/Gameplay Incorporation)

Our Full Proposal: https://docs.google.com/document/d/1udcH7Xqnmw-_0XHljnJX-sy47B47Ecf-AsB71gnQjTc/edit#
