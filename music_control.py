import pygame
from pygame import mixer
from moviepy.editor import *


def play_music(music_name):

    mixer.init()
    mixer.music.load(music_name)
    mixer.music.play()


def set_volume(vol):
    mixer.music.set_volume(vol)
