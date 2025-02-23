#!/usr/bin/env python3

filename = "list.py"

with open(filename) as f:
    content = f.readlines()

print(content)

filename = "list.py"

infile = open(filename, 'r')
data = infile.read()
infile.close()

print(data)