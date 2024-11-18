# Looping through a string

for x in "banana":
    print (x)

# Output: 
# b
# a
# n
# a
# n
# a


# looping through a list

# example 1

numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
   if num%2 == 0:
      print (num)

# Output:
# 34
# 54
# 78
# 44
# 80

# looping through the list items by referring to their index number.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Output: 
# apple
# banana
# cherry

# Break statement example 1

for letter in 'Python':    
   if letter == 'h':
      break
   print ("Current Letter :", letter)
print ("Good bye!")

# Output:
# Current Letter : P
# Current Letter : y
# Current Letter : t
# Good bye!

# Break statement example 2

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

# Output:
# apple
# banana

# Break statement example 3

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# Output:
# apple

