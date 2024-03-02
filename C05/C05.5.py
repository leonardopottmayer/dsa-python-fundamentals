# LAMBDA EXPRESSIONS
print("LAMBDA EXPRESSIONS")

def potential(num):
    result = num ** 2
    return result

print(potential(5))

def potential(num):
    return num ** 2

print(potential(5))

def potential(num): return num ** 2

print(potential(5))

# Defining a lambda expression (anonymous function)
potential = lambda num: num ** 2

potential(5)

Par = lambda x: x%2==0
print(Par(3))
print(Par(4))

first = lambda s: s[0]
print(first("Python"))

reverse = lambda s: s[::-1]
print(reverse("Python"))

addNum = lambda x,y : x+y
print(addNum(2,3))

