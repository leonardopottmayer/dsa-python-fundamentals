print("************************* Python Calculator *************************")

print("")

print("Type the number of the operation you want to perform:")

print("")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

print("")

operation = input("Type the number of the operation (1/2/3/4): ")

print("")

num1 = input("Type the first number: ")

print("")

num2 = input("Type the second number: ")

result = ""

if operation == "1":
    result = num1 + num2
elif operation == "2":
    result = num1 + num2
elif operation == "3":
    result = num1 + num2
elif operation == "4":
    result = num1 + num2
else:
    print("Invalid operation")

print("")

print("The result is: " + str(result))