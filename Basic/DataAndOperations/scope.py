#!/usr/bin/env python3

balance = 0

def addAmount(x):
    global balance
    balance = balance + x

addAmount(5)
print(balance)