print("Welcome to the calculator!")

# Ask the user to enter the first number
first_number = float(input("Please enter the first number: "))

# Ask the user to enter the operator
operator = input("Please enter the operator: ")

# Ask the user to enter the second number
second_number = float(input("Please enter the second number: "))

# Calculate the result
if operator == "+":
    print("The sum of the numbers is", first_number + second_number)
elif operator == "-":
    print("The difference of the numbers is", first_number - second_number)
elif operator == "*":
    print("The product of the numbers is", first_number * second_number)
elif operator == "/":
    print("The quotient of the numbers is", first_number / second_number)
else:
    print("Invalid operator.")