#!/usr/bin/env python3

from playsound import playsound
playsound('audio.mp3')

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("sound.wav")
play(song)

from Tkinter import *
import tkSnack

root = Tk()
tkSnack.initializeSnack(root)

snd = tkSnack.Sound()
snd.read('sound.wav')
snd.play(blocking=1)

# apt install mpg123
import os

file = "file.mp3"
os.system("mpg123 " + file)
