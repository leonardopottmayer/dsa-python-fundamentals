print("Hello, world!")

# Creates a list with numbers between 1 and 100
numbers = list(range(1, 101))

# Prints the type of the 'numbers' variable
print(type(numbers))

# Loops the list and verifies if the number is even and divisible by 4
for number in numbers:
    if number % 2 == 0 and number % 4 == 0:
        print(number)
