# Write a function that takes two variables and does all the computations asked

def number_fun(a,b):
    print("You entered", a,"and", b)
    print(a, "+", b, "=", int(a) + int(b))
    print(a, "*", b, "=", int(a) * int(b))
    print(a, "**", b, "=", int(a) ** int(b))
    print(a, "%", b, "=", int(a) % int(b))

# Ask the user for the first number, store the value in a variable

firstnum = input("Enter an integer between 10 and 100: ")

# Ask the user for the second number, store the value in a variable

secondnum = input("Enter an integer less than 4: ")

# Perform calculations. Be careful about string formatting for autograders.

number_fun(firstnum,secondnum)

