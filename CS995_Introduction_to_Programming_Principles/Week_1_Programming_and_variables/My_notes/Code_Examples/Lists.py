# List Methods

# append()

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"] 
a.append(b)

print(a)

# Output: ["apple", "banana", "cherry"], ["Ford", "BMW", "Volvo"] ]

# clear()

fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()

print(fruits)

# Output: []

# copy()

fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()

print(x)

# Output: ['apple', 'banana', 'cherry', 'orange']

# count()

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)

print(x)

# Output: 2

# extend()

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

# Output: ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# index()

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)

# Output: 2

# insert()

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)

# Output: ['apple', 'orange', 'banana', 'cherry']

# pop()

fruits = ['apple', 'banana', 'cherry']
fruits.pop()
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# Output: ['apple', 'banana']
# Output: ['apple', 'cherry']