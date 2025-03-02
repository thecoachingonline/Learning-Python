#!/usr/bin/env python3

class Human:
    name = ""

class Coder:
    skills = 3

class Pythonista(Human, Coder):
    version = 3

obj = Pythonista()
obj.name = "Alice"

print(obj.name)
print(obj.version)
print(obj.skills)