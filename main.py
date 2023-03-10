print("Hello Learning")

# Variables
wallet = 41
print(wallet)

wallet = 32
print(wallet)

#Numbers: Ints and floats
day = 21
temp = -15
weight = 190.435623

print(day + 3)
print(weight - 2)
print(day * temp)

#Srings
age = 32
shirt = 'blue'
store = 'Nink\'s Pizza Shop, '

print(store + age + shirt)

#Using variables in strings
day = 21
month = 'October'
temp = 65
day_name = 'Tuesday'

print(f"Today is {day_name} {month} {day} and it's {temp} degrees outside")

#Booleans and if statements
light_is_on = False

if light_is_on:
    print("The light is on!")

print("Hello")

#Comparison and else

light_is_on = True

if light_is_on:
    print("The light is on!")
else:
    print("We're in the dark")

weight = 190.4

if weight != 195:
    print("You're under weight :)")

age = 17

if age >= 18:
    print("Adult")
else:
    print("Child")