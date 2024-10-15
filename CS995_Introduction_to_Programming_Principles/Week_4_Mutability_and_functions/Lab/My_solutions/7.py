"""Write a program that includes a function that converts the text string from the previous function back into
alphabetic characters. For example, "1|2|26" should be returned as "abz". The function should accept a
mapping dictionary as an input parameter, as well as the input string. The function split("|") should be
used to split the text, before comparing it with the mapping dictionary. A for loop should be used to iterate
over the strings returned by the split function."""

def convert_to_letters(input_string, mapping_dict):
    letter_string=""
    for char in input_string.split("|"):
        letter_string += mapping_dict[char]

    return letter_string

my_string = "1|2|3"
mapping_dict = {
    "1": "a",
    "2": "b",
    "3": "c"
}

result = convert_to_letters(my_string,mapping_dict)

print(result)