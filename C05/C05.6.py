# LIST COMPREHENSION
print("LIST COMPREHENSION")

# [expression for item in iterable if condition = True]

# List comprehension that prints the numbers from 0 to 9
numbers_list = [x for x in range(10)]
print(numbers_list)

# Adding conditions
numbers_list = [x for x in range(10) if x < 5]
print(numbers_list)

fruits_list = ["banana", "apple", "orange", "pineapple", "cherry"]
new_list = []

# Traditional way
for x in fruits_list:
    if "b" in x:
        new_list.append(x)
        
print(new_list)

# Same as before, but using list comprehension
new_list = [x for x in fruits_list if "b" in x]
print(new_list)

# DICTIONARY COMPREHENSION
print("DICTIONARY COMPREHENSION")

students_dict = {"Pedro": 24, "Ana": 22, "Gabriela": 19, "Janaina": 25, "Matheus": 24}

dict_students_status = {k:v for (k, v) in students_dict.items()}
print(dict_students_status)

dict_students_status = {k: ("Approved" if v > 22 else "Reproved") for (k, v) in students_dict.items()}
print(dict_students_status)