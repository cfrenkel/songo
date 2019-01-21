import pygame
from pygame import mixer
from moviepy.editor import *


def play_music(music_name):

    mixer.init()
    mixer.music.load(music_name)
    mixer.music.play()

def set_volume_start(vol):
    mixer.music.set_volume(vol)


def set_volume(vol):
    curr_vol = mixer.music.get_volume()
    print("{} currr".format(curr_vol))
    if curr_vol >= vol:
        while curr_vol > vol:
            print(curr_vol)
            mixer.music.set_volume(curr_vol)
            curr_vol -= 0.1

    else:
        while curr_vol > vol:
            print(curr_vol)
            mixer.music.set_volume(curr_vol)
            curr_vol += 0.1

    mixer.music.set_volume(vol)

def get_busy():

    # print(mixer.music.get_busy())
    return mixer.music.get_busy()
