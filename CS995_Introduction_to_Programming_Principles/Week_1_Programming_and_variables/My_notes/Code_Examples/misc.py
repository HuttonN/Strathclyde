# type()

x = 5
y = "John"
print(type(x))
print(type(y))

# Output: 
# <class 'int'>
# <class 'str'>

# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Output: 
# "Orange" 
# "Banana"
# "Cherry"

# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Output: 
# "Orange" 
# "Orange" 
# "Orange" 

# Unpack a Collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output: 
# "apple" 
# "banana"
# "cherry"
