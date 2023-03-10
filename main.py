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

#Picking random numbers
import random

print(random.randint(1,10))

print(random.random())

answer = random.randint(1,3)

if answer == 1:
    print("Yes")
if answer == 2:
    print("No")
if answer == 3:
    print("Maybe")

#Choosing what fortune to show
import random

lucky_number = random.randint(1,100)
fortune_number = random.randint(1,3)
fortune_text = ''

if fortune_number == 1:
    fortune_text = 'You will have a great day!'
if fortune_number == 2:
    fortune_text = 'Today will be tough...but worth it.'
if fortune_number == 3:
    fortune_text = 'You will get married this year!'

print(f'{fortune_text} Your Lucky Number is: {lucky_number}')

#Lists
fav_movies = ["Sandlot", "The Lego Move", "Dune"]

print(fav_movies[2])

fav_numbers = [4,9,33]

print(fav_numbers[0])

#Add, insert, delete
print(len(fav_movies))

fav_movies.append("Iron Man")
print(fav_movies)

fav_movies.insert(1,"Batman")
print(fav_movies)

del(fav_movies[2])
print(fav_movies)

#For loops
for number in range(10):
    print(number)
    print("Hello")

for movie in fav_movies:
    print(movie * 2)