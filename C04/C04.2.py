# VARIABLES
print("VARIABLES")

test_var = 1
print(test_var)

test_var = 2
print(test_var)

print(type(test_var))

test_var = 9.5
print(test_var)

print(type(test_var))

# MULTIPLE DECLARATION
print("MULTIPLE DECLARATION")

person1, person2, person3 = "Bob", "Mary", "Any"
print(person1)
print(person2)
print(person3)

animal1 = animal2 = animal3 = "Dog"
print(animal1)
print(animal2)
print(animal3)

# VARIABLES ASSIGNED TO OTHER VARIABLES
print("VARIABLES ASSIGNED TO OTHER VARIABLES")

width = 2
height = 4
area = width * height
print(area)

perimeter = 2 * width + 2 * height
print(perimeter)

# The operators order is the same as in math
perimeter = 2 * (width + 2) * height

print(perimeter)

# OPERATIONS WITH VARIABLES
print("OPERATIONS WITH VARIABLES")

age1 = 25
age2 = 35

print(age1 + age2)
print(age2 - age1)
print(age2 * age1)
print(age2 / age1)
print(age2 % age1)

# VARIABLE CONCATENATION
print("VARIABLE CONCATENATION")

firstName = "Bob"
lastName = "Marley"

fullName = firstName + " " + lastName

print(fullName)