s = input("Do you agree? ")

s = s.lower()

if s in ["y", "yes"]:
    print("Agree")
elif s in ["n", "no"]:
    print("Not agree")