# FOR LOOP
print("FOR LOOP")

# Creating a tuple and printing each of its items
tp = (2,3,4)
for i in tp:
    print(i)

# Creating a list and printing each of its items
listOfStrings = ["Data", "Science", "Academy"]
for i in listOfStrings:
    print(i)
    
# Printing the values in the interval between 0 and 5 (exclusive)
for counter in range(0, 5):
    print(counter)
    
# Printing the even numbers in the list of numbers
list = [1,2,3,4,5,6,7,8,9,10]
for num in list:
    if num % 2 == 0:
        print(num)
        
# Printing numbers in interval between 0 and 101, incrementing by 2
for i in range(0, 101, 2):
    print(i)
    
# Strings are sequences too
for char in "Python is a great language.":
    print(char)
    
# NESTES FOR LOOPS
print("NESTED FOR LOOPS")

list1 = [0,1,2,3,4]
list2 = [1,2,3]

# External loop
for list1_element in list1:
    
    # Internal loop
    for list2_element in list2:
        
        print('\n', list1_element * list2_element)
        
    print("-----")
    
# Sum the even numbers in the first list with the even numbers in the second list
list1 = [10, 16, 24, 39, 47]
list2 = [32, 89, 47, 76, 12]
sum = 0

for list in [list1, list2]:
    
    for num in list:
        
        if num % 2 == 0:
            sum += num
            
print("The sum of the even numbers is", sum)

# Loop in list of lists (matrix) to find the greatest number
matrix = [[42, 23, 34], [100, 214, 114], [10.1, 98.7, 12.3]]
greatest_number = 0

for line in matrix:
    
    for num in line:
        
        if num > greatest_number:
            greatest_number = num

print("The greatest number is", greatest_number)

# Printing keys in a dictionary
dict = {"k1": "Python", "k2": "R", "k3": "Scala"}
for item in dict:
    print(item)
    
# Printing key and value of a dictionary
for k,v in dict.items():
    print(k,v)
    
# WHILE LOOP
print("WHILE LOOP")

value = 0
while value < 10:
    print(value)
    value = value + 1
    
value = 11
while value < 10:
    print(v)
    value = value + 1

# Using while with else    
x = 0
while x < 10:
    print("The value of x in the loop is", x)
    print("x is still less than 10, adding 1 to x")
    x += 1
else:
    print("Loop finished!")
print(x)

# Pass, break, continue
value = 0
while value < 10:
    if value == 4:
        break
    else:
        pass
    print(value)
    value = value + 1
    
# Remove letter z while printing the string
for letter in "Python is incredible!":
    if letter == "z":
        continue
    print(letter)
