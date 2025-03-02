#!/usr/bin/env python3

class Fruit:
    name = 'Fruitas'

    @classmethod
    def printName(cls):
        print('The name is:', cls.name)

Fruit.printName()

apple = Fruit()
berry = Fruit()

Fruit.printName()
apple.printName()
berry.printName()

apple.name="Apple"
Fruit.printName()
apple.printName()
berry.printName()

Fruit.name="Apple"
Fruit.printName()
apple.printName()
berry.printName()

class Fruit:
    name = 'Fruitas'

    def printName(cls):
            print('The name is:', cls.name)

Fruit.printAge = classmethod(Fruit.printName)
Fruit.printAge()