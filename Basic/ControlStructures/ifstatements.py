#!/usr/bin/env python3
x = 4
if x < 5:
    print("x is smaller than five")
    print("this means it's not equal to five either")
    print("x is an integer")


gender = input("Gender? ")
gender = gender.lower()
if gender == "male":
    print("Your cat is male")
elif gender == "female":
    print("Your cat is female")
else:
    print("Invalid input")

age = int(input("Age of your cat? "))
if age < 5:
    print("Your cat is young.")
else:
    print("Your cat is adult.")