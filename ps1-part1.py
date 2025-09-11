# Ask the user for the first number, store the value in a variable

firstnum = input("Enter an integer between 10 and 100: ")

# Ask the user for the second number, store the value in a variable

secondnum = input("Enter an integer less than 4: ")           

# Repeat back the numbers

print("You entered", firstnum,"and", secondnum)

# Perform calculations. Be careful about string formatting for autograders.

print(firstnum, "+", secondnum, "=", int(firstnum) + int(secondnum))
print(firstnum, "*", secondnum, "=", int(firstnum) * int(secondnum))
print(firstnum, "**", secondnum, "=", int(firstnum)**int(secondnum))
print(firstnum, "%", secondnum, "=", int(firstnum)%int(secondnum))
