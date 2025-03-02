#!/usr/bin/env python3

import subprocess

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

a = "Say something in natural language."

# create wav file
# w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a  
# execute_unix(w)

# tts using espeak
c = 'espeak -ven+f3 -k5 -s150 --punct="<characters>" "%s" 2>>/dev/null' % a 
execute_unix(c)

# need gTTS and mpg123
# pip install gTTS
# apt install mpg123

from gtts import gTTS
import os

# define variables
s = "escape with plane"
file = "file.mp3"

# initialize tts, create mp3 and play
tts = gTTS(s, 'en')
tts.save(file)
os.system("mpg123 " + file)