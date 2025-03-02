#!/usr/bin/env python3

class Music:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")

Music.play()

obj = Music()
obj.stop()