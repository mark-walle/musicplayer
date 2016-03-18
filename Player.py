"""
PLANNING
I envision these objects:
Library(contains Artists)
Artist (contains Albums)
Album (contains Songs)
Playlist (contains Artist)
Player (interfaces with Library and mp3 program)

User interaction will occur through the Player object which will interact with Library/Playlist
A database connection will be required
Playlist can export to m3u

Stage 1:
enable playing of a single file

Stage 2:
enable list of files to play

Stage 3:
enable library of files

Stage 4:
play files through Playlist objects
"""

import pygame as pg

class Player:
    def __new__(file):
        freq = 44100     # audio CD quality
        bitsize = -16    # unsigned 16 bit
        channels = 2     # 1 is mono, 2 is stereo
        buffer = 2048    # number of samples (experiment to get best sound)
        pg.mixer.init(freq, bitsize, channels, buffer)
        # volume value 0.0 to 1.0
        pg.mixer.music.set_volume(1.0)
        clock = pg.time.Clock()
        try:
            pg.mixer.music.load(file)
            print("Music file {} loaded!".format(music_file))
        except pg.error:
            print("File {} not found! ({})".format(music_file, pg.get_error()))
            return
        
    def play():
        pg.mixer.music.play()
        while pg.mixer.music.get_busy():
            # check if playback has finished
            clock.tick(30)
    
player = Player("12 - Redemption Song.mp3")
player.play()
