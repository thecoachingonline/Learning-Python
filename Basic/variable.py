#!/usr/bin/python 

myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}


print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# myint = "abc"
# print(myint)

print(mylist[2])
print(mytuple[1])

print(mylist[1:5])
print(mylist[1:5:2])

print(mylist[::-1])

print(mydict["one"])

print("string type" + str(123))

def someFunction():
    global mystr
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)

del mystr
print(mystr)

# Variables and Types
x = 3
f = 3.1415926
name = "Python"

print(x)
print(f)
print(name)

combination = name + " " + name
print(combination)

sum = f + f
print(sum)