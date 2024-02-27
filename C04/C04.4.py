# WORKING WITH LISTS
print("WORKING WITH LISTS")

list_1 = ["rice, chicken, tomato, milk"]
print(type(list_1))

list_2 = ["rice", "chicken", "tomato", "milk"]
print(type(list_2))

list_3 = [23, 100, "Data scientist"]
print(type(list_3))

item1 = list_3[0]
item2 = list_3[1]
item3 = list_3[2]

print(item1, item2, item3)

# UPDATING AN ITEM IN A LIST
print("UPDATING AN ITEM IN A LIST")

list_2[2] = "chocolate"
print(list_2)

# DELETING AN ITEM IN A LIST
print("DELETING AN ITEM IN A LIST")

del list_2[3]
print(list_2)

# NESTED LISTS (list of lists)
print("NESTED LISTS")

lists = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]
print(lists)

a = lists[0]
print(a)

b = a[0]
print(b)

# OPERATIONS WITH LISTS
print("OPERATIONS WITH LISTS")

# Accesses the first item in the first list
print(lists[0][0])

c = lists[0][2] + 10
print(c)

d = 10
e = d * lists[2][0]
print(e)

# CONCATENATING LISTS
print("CONCATENATING LISTS")

list_s1 = [34, 32, 56]
list_s2 = [21, 90, 51]

total_list = list_s1 + list_s2
print(total_list)

# IN OPERATOR
print("IN OPERATOR")

# Checks if an item is in a list
test_op_list = [100, 2, -5, 3.4]
print(10 in test_op_list)

# BUILT-IN FUNCTIONS
print("BUILT-IN FUNCTIONS")

numbers_list = [10, 20, 50, -3.4]
print(len(numbers_list))

# Returns the maximum value
print(max(numbers_list))

# Returns the minimum value
print(min(numbers_list))

dsa_courses_list = ["Data analist", "Data scientist", "Data engineer"]

# Adding an item to a list
dsa_courses_list.append("AI engineer")
dsa_courses_list.append("AI engineer")

print(dsa_courses_list)
print(dsa_courses_list.count("AI engineer"))

a = []
a.append(10)
a.append(50)

print(a)

old_list = [1, 2, 5, 10]
new_list = []

for item in old_list:
    new_list.append(item)

print(new_list)

# Other way to add items to a list
cities = ["Recife", "Manaus", "Salvador"]
cities.extend(["Fortaleza", "Palmas"])
print(cities)

# Getting an index of the list by content
print(cities.index("Salvador"))

# Adds the 110 number to index 2, and pushed the rest of the list to the right
cities.insert(2, 110)
print(cities)

cities.reverse()
print(cities)

# Sorts the list
x = [3, 4, 2, 1]
x.sort()
print(x)