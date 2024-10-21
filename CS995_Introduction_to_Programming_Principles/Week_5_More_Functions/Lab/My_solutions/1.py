"""Write a function to count the frequency of different characters within a text string. Then write a program to
print the frequency for each of the vowels."""

def character_count(input_string):
    character_dictionary = {}

    for character in input_string:
        if character in character_dictionary:
            character_dictionary[character] +=1
        else:
            character_dictionary.update({character : 1})

    return character_dictionary

def vowel_frequency(input_string):
    input_string = input_string.lower()
    character_dictionary = character_count(input_string)
    vowels = "aeiou"
    for char in vowels:
        if char in character_dictionary:
            print(f"frequency of {char} is {character_dictionary[char]}")
        else:
            print(f"frequency of {char} is 0")

vowel_frequency("Are you ok")