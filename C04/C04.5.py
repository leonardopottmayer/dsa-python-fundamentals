# WORKING WITH DICTIONARIES
print("WORKING WITH DICTIONARIES")

students_lst = ["Pedro", 24, "Ana", 22, "Ronaldo", 26, "Janaina", 25]
print(students_lst)

# Creating a dictionary
students_dict = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}
print(students_dict)

print(students_dict["Pedro"])

# Removing all the items
# students_dict.clear()
# print(students_dict)

# Deletes the variable from the memory
# del students_dict
# print(students_dict)

print(len(students_dict))

# Getting only the list of keys
print(students_dict.keys())

# Getting only the list of values
print(students_dict.values())

# Getting the list of items
print(students_dict.items())

students_2 = {"Camila": 27, "Adriana": 28, "Julia": 26}

# Adds some new items to the dictionary
students_dict.update(students_2)
print(students_dict)

dic1 = {}
dic1["key_1"] = 2
print(dic1)

dic1[10] = "value_1"
print(dic1)

dic1[9.3] = "Python"
print(dic1)

a = dic1["key_1"]
print(a)

# DICTIONARY OF LISTS
print("DICTIONARY OF LISTS")

dict3 = { 'key1': 1230, 'key2': [22, 453, 73.4], 'key3': ['item1', 'item2'] }

# DICTIONARY OF ANYTHING
print("DICTIONARY OF ANYTHING")

dict4 = { 'key1': 1230, 'key2': [22, 453, 73.4], 'key3': {'key4': 'item1', 'key5': 'item2'} }

# TUPLES
print("TUPLES")

# Tuples are not mutable
tuple1 = ('Dummy', 20, True, 35.2)
print(tuple1)

tuple2 = tuple1

del tuple1

print(tuple2.index('Dummy'))

list_t2 = list(tuple2)
print(list_t2)

list_t2.append("Python")
print(list_t2)

tuple2 = tuple(list_t2)
print(tuple2)