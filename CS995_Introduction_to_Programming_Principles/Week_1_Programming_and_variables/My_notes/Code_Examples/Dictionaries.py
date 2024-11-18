# List Methods

# clear()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)

# Output: {}

# copy()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)

# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# fromkeys()

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

# Output: {'key1': 0, 'key2': 0, 'key3': 0}

x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)

# Output: {'key1': None, 'key2': None, 'key3': None}

# get()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

# Output: Mustang

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)

# Output: 15000

# items()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)

# Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)

# Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])

# keys()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)

# Output: dict_keys(['brand', 'model', 'year'])

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

car["color"] = "white"

print(x)

# Output: dict_keys(['brand', 'model', 'year', 'color'])

# pop()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

# Output: {'brand': 'Ford', 'year': 1964}

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")

print(x)

# Output: Mustang

# popitem()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)

# Output: {'brand': 'Ford', 'model': 'Mustang'}

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()

print(x)

# Output: ('year', 1964)