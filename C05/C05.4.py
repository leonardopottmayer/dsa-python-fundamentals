import math

# FUNCTIONS
print("FUNCTIONS")

# Simple function
def firstFunc():
    print("Hello World")
    
firstFunc()

# Use variables inside function
def secondFunc():
    name = "Bob"
    print("Hello %s" %(name))
    
secondFunc()

# Add parameters
def thirdFunc(name):
    print("Hello %s" %(name))
    
thirdFunc("Bob")

# Use loops inside functions
def printNumbers():
    for i in range(1, 6):
        print("Number " + str(i))
        
printNumbers()

# Function that sums two numbers
def addNum(firstNum, secondNum):
    print(firstNum + secondNum)
    
addNum(5, 10)

# Passing many arguments with *vartuple
def printVarInfo(arg1, *vartuple):
    print("The parameter is ", arg1)
    
    for item in vartuple:
        print("The parameter was ", item)
    return

printVarInfo(10)
printVarInfo("Chocolate", "Strawberry")

# VARIABLES SCOPE
print("VARIABLES SCOPE")

# This is a global variable
var_global = 10

def multiply_numbers(num1, num2):
    # This is not the global variable, even it has the same name, but it exists only inside the function
    var_global = num1 * num2
    print(var_global)
    
multiply_numbers(5, 25)
print(var_global)

# BUILT-IN FUNCTIONS
print("BUILT-IN FUNCTIONS")

# Extract the absolute value of a number (removeing negative sign)
print(abs(-56))
print(abs(23))

# Converting number to bool, 0 is false, everything else is true
print(bool(0))
print(bool(1))
print(bool(2))

# Convert a decimal number to int (this only removes the decimal part, so 4.99999999 would be 4)
print(int(4.3))

# Convert a number to string
print(str(13))

# Converts a value to float
print(float(5))

# Convert string number to int
print(int("5"))

# Convert string number to float
print(float("123.345"))

# Get the length of an array
print(len([23, 34, 45, 46]))

array = [1, 2, 3]

# Get the greatest value in an array
print(max(array))

# Get the smallest value in an array
print(min(array))

# Sum all the values in an array
list1 = [16, 23, 44, 75]
print(sum(list1))

# CREATING FUNCTIONS USING OTHER FUNCTIONS
print("CREATING FUNCTIONS USING OTHER FUNCTIONS")

def isPrime(num):
    if (num % 2) == 0 and num > 2:
        return "This number is not prime."
    
    for i in range (3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "This number is not prime."
        
    return "This number is prime."

print(isPrime(17))

lower_case = "This Text Should Be Lower Case"

def lowerCase(text):
    return text.lower()

print(lowerCase(lower_case))

# SPLITTING DATA
print("SPLITTING DATA")

def split_string_words(text):
    return text.split(" ")

text = "This function is going to be very useful for me."

print(split_string_words(text))

def split_string_letters(text):
    upperText = text.upper()
    for letter in upperText:
        print(letter)
        
split_string_letters(text)