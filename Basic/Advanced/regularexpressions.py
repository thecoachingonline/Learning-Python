#!/usr/bin/env python3

import re

string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"

matches = re.findall(r'woo\w*', string)
print(matches)

if re.search(r'woo\w*', string):
    print('woo\w* foud!')
else:
    print('not found')