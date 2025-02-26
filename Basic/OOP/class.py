#!/usr/bin/env python3

class dog:
    name = ""
    age = 0

    def bark(self):
        print('Bark')

class Website:
    def __init__(self,title):
        self.title = title

    def showTitle(self):
        print(self.title)

obj = Website('https://www.linkedin.com/in/nanthachai-technology-business-healthcare')
obj.showTitle()