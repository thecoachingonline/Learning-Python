#!/usr/bin/env python3

d = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 }
iterable = d.keys()
print(iterable)

for item in iterable:
    print(item)

d = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 }
iterable = d.keys()
iterator = iter(iterable)
print( next(iterator) )
print( next(iterator) )

items = [ "one","two","three","four" ]
iterator = iter(items)
x = next(iterator) 
print(x)