#!/usr/bin/env python3

# create a sequence
browsers = ['Chrome','Firefox','Opera','Vivaldi']

# create an enumeratable and convert to list
x = list(enumerate(browsers))
print(x)

browsers = ['Chrome','Firefox','Opera','Vivaldi']
eObj = enumerate(browsers)

x = next(eObj)
print(x)
x = next(eObj)
print(x)