names = ["ก", "ข", "ค"]

name = input("Name: ")

for n in names:
    if name == n:
        print("Found")
        break
    else:
        print("Not found")