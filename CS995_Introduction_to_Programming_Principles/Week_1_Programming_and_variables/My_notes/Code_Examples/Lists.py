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

# sort()

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# Output: ['BMW', 'Ford', 'Volvo']

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

# Output: ['Volvo', 'Ford', 'BMW']

def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)

# Output: ['VW', 'BMW','Ford', 'Mitsubishi']

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)

# Output: [
#  {'car': 'Ford', 'year': 2005},
#  {'car': 'Mitsubishi', 'year': 2000},
#  {'car': 'BMW', 'year': 2019},
#  {'car': 'VW', 'year': 2011}
#]

def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)

# Output: ['Mitsubishi', 'Ford', 'BMW', 'VW'] 

#reverse()

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# Output: ['cherry', 'banana', 'apple']

# remove()

fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

# Output: ['apple', 'cherry']

# pop()

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# Output: ['apple', 'cherry']

fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)

# Output: 'banana'

# insert()

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# Output: ['apple', 'orange', 'banana', 'cherry']

# index()

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# Output: 2

fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)

# Output: 3

# extend()

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# Output: ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

# Output: ['apple', 'banana', 'cherry', 1, 4, 5, 9]