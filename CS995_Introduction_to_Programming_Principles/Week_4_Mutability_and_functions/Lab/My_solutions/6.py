"""Write a program that includes a function that converts text characters into numbers, according to a
mapping that is given in a dictionary. For example, the key "a" could be mapped to the value 1. The
function should accept a text string and return a text string of numbers. For example, "abz" could become
"1|2|26". The function should accept a mapping dictionary as an input parameter. A for loop should be
used to loop over the character in the input string."""

def convert_to_numbers(input_string, mapping_dict):
    number_string=""
    for char in input_string:
        number_string += f"{mapping_dict[char]}|"

    return number_string.rstrip('|')

my_string = "abc"
mapping_dict = {
    "a": 1,
    "b": 2,
    "c": 3
}

result = convert_to_numbers(my_string,mapping_dict)

print(result)