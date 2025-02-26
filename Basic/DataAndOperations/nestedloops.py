#!/usr/bin/env python3

persons = [ "John", "Marissa", "Pete", "Dayton", "Nanthachai" ]
restaurants = [ "Japanese", "American", "Mexican", "French", "Thailand" ]

for person in persons:
    for restaurant in restaurants:
        print(person + " eats " + restaurant)