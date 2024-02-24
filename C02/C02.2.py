print("Hello, world!")

# Creates a list with numbers between 1 and 100
numbers = list(range(1, 101))

# Creates a list with only even numbers divisible by 4, using list comprehension
# You can read it like "for each number in my list of numbers, if it is even and divisible by 4, add it to my even_div4 list".
# The first 'number' variable inside the brackets is the element returned of the numbers list, if it is even and divisible by 4.
even_div4 = [number for number in numbers if number % 2 == 0 and number % 4 == 0]

# Prints the type of the 'even_div4' variable
print(type(even_div4))

# Prints the list
print(even_div4)