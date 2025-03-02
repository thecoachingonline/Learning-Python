#!/usr/bin/env python3

class App:
    def start(self):
       print('starting')

class Android(App):
    def getVersion(self):
       print('Android version')

app = Android()
app.start()
app.getVersion()