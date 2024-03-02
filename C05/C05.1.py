# CONDITIONAL STATEMENTS
print("CONDITIONAL STATEMENTS")

# If
if 5 > 2:
    print("Five is greater than two!")

# If and else
if 5 < 2:
    print("Five is less than two!")
else:
    print("Five is not less than two!")

# If and else with variables
day = 'Tuesday'
if day == "Tuesday":
    print("Today is Tuesday!")
else:
    print("Today is not Tuesday!")

# If, elif and else
if day == "Monday":
    print("Today is Monday!")
elif day == "Tuesday":
    print("Today is Tuesday!")
else:
    print("Today is not Monday, Tuesday or Wednesday!")

# RELATIONAL OPERATORS
print("RELATIONAL OPERATORS")

print(6 > 3)
print(3 > 7)
print(4 < 8)
print(4 >= 8)

if 5 == 5:
    print("Testing Python!")
    
if True:
    print("Python is cool!")
    
if 4 > 3:
    print("4 is greater than 3!")

# NESTES CONDITIONALS
print("NESTED CONDITIONALS")

age = 18
if age > 17:
    print("You can get a drivers license!")
    
name = "Bob"
if age > 13:
    if name == "Bob":
        print("Ok Bob, you can come in!")
    else:
        print("Sorry, you can't come in!")
        
age = 13
if age >= 13 and name == "Bob":
    print("Ok Bob, you can come in!")

age = 12
if (age >= 13) or (name == "Bob"):
    print("Ok Bob, you can come in!")
    
# LOGICAL OPERATORS
print("LOGICAL OPERATORS")

age = 18
name = "Bob"
if age > 17 and name == "Bob":
    print("You can drive!")

age = 18
if age > 17 and name == "Bob":
    print("Authorized!")

# AND operator
number = 4
if (number > 2) and (number % 2 == 0):
    print("The number is even and greater than 2!")
    
if (number > 5) and (number % 2 == 0):
    print("The number is even and greater than 5!")
else:
    print("The number is not even or less than 5!")
    
# OR operator
if (number > 5) or (number % 2 == 0):
    print("This is beeing printed because either the number is even or greater than 5!")
    
# NOT operator
if not(number > 5) and (number % 2 == 0):
    print("This is beeing printed becaus both conditions are true!")

# AND, OR and NOT operator
if (not(number > 5) and (number % 2 == 0)) or (number == 4):
    print("This is beeing printed becaus two first conditions are true OR the third is true!")
    
# Example using variables
subject = "Data Science"
final_grade = 70

if subject == "Data Science" and final_grade >= 70:
    print("Congratulations, you passed!")
else:
    print("Sorry, you failed.")
    
# Using more than one condition in if and using placeholders
final_grade = 90
semester = 2

if subject == "Data Science" and final_grade >= 80 and semester != 1:
    print("You've been approved in %s with final grade of %r!" %(subject, final_grade))