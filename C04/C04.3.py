# CREATING A STRING
print("CREATING A STRING")

# Printing a string
print("Hello World")

print("Testing \nStrings \nin \nPython")
print("\n")

# INDEXING STRINGS
print("INDEXING STRINGS")

s = 'Data Science Academy'
print(s)
print(s[0])
print(s[1])

# Print everything after the first character
print(s[1:])

# Prints a slice of the string
print(s[2:10])

# Prints everything before the position 3 (so it prints pos 0, 1 and 2)
print(s[:3])

# Starts from the end and goes backwards
print(s[-1])

print(s[:-1])

# Jumps the specified number os characters
print(s[::2])

print(s[::-1])

# STRING PROPERTIES
print("STRING PROPERTIES")

# Does not change the s variable
print(s + " some random text.")
print(s)

# Changes the s variable
s = s + " some random text."
print(s)

# Concatenates the string 3 times
letter = 'w'
print(letter * 3)

# BUILT-IN STRING FUNCTIONS
print("BUILT-IN STRING FUNCTIONS")

print(s)
print(s.upper())
print(s.lower())
print(s.split())
print(s.split('y'))

# SCRIPT FUNCTIONS
print("SCRIPT FUNCTIONS")

print(s)

# Converts the first character to uppercase
print(s.capitalize())

# Counts the number of 'a' in the string
print(s.count('a'))

# Checks if the string is alphanumeric
print(s.isalnum())

# Checks if the string is all lowercase
print(s.islower())

# Checks if the string is all empty space
print(s.isspace())

print(s.endswith('o'))

# COMPARING STRINGS
print("COMPARING STRINGS")

print("Python" == "R")
print("Python" == "Python")