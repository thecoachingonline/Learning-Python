"""
x = int(input("X: "))
y = int(input("Y: "))

z = x / y
print(f"{z:.50f}")
"""

def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Not an integer")

def main():
    x = get_int("x: ")
    y = get_int("y: ")

    print(x + y)

main()