#!/usr/bin/env python3

try: 
    1 / 0
except ZeroDivisionError: 
    print('Divided by zero')

print('Should reach here')

try:
    x = input("Enter number: ")
    x = x + 1
    print(x)
except:
    print("Invalid input")

def fail():
    1 / 0

try:
    fail()
except:
    print('Exception occured')

print('Program continues')

try: 
    f = open("test.txt")
except: 
    print('Could not open file')
finally:
    f.close()

print('Program continue')

class LunchError(Exception):
    pass

raise LunchError("Programmer went to lunch")

class NoMoneyException(Exception):
    pass

class OutOfBudget(Exception):
    pass

balance = int(input("Enter a balance: "))
if balance < 1000:
    raise NoMoneyException
elif balance > 10000:
    raise OutOfBudget