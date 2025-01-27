#Define string
x = "Hello"
print(x)

#String indexing
print(x[0])
print(x[1])

#Sub string
x = "hello world"
s = x[0:3]
print(s)
s = x[:3]
print(s)

#Example
x = "Nanthachai"
print(x)

# Combing numbers and text
s = "My lucky number is %d, what is yours?" % 9
print(s)

# Alternative method of combining numbers and text
s = "My lucky number is " + str(9) + ", what is yours?"
print(s)

# Print character by index
print(x[0])

# Print piece of string
print(x[0:3])