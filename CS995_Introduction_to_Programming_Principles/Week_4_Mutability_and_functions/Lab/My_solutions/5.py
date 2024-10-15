"""Write a program that includes a function that accepts a dictionary as an input parameter. The function
should clear the dictionary and add three key and value pairs, which are colour names and integer values
respectively."""

def colour_dictionary(dictionary):
    dictionary.clear()
    dictionary.update({"red": 1})
    dictionary.update({"green": 2})
    dictionary.update({"blue": 3})

original_dictionary = {
    "a": 1,
    "b": 2,
}
print(original_dictionary)

colour_dictionary(original_dictionary)
print(original_dictionary)