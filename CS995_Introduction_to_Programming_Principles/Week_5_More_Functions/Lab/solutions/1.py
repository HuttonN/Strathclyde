"""
Python: More functions: Q1
"""


def count_chars(input_text):
    """
    A function to count characters within an input string.
    The counts are returned within a dictionary.
    """
    counts = {}

    # Loop over the characters.
    for c in input_text:

        # If this character has not been seen before.
        if c not in counts.keys():

            # Create the key in the dictionary and set the value to zero.
            counts[c] = 0

        # Count this character.
        counts[c] += 1
    return counts


"""
A program to count the number of vowels in an input string.
"""

# A test input string.
input_string = "This game is played at social occasions known as a beetle "
input_string += "drive, in which many rounds of the game are played."

# Get the number of times that a character is present.
result = count_chars(input_string)

# Print out the counts for the vowels.
vowels = [
    "a",
    "e",
    "i",
    "o",
    "u"
]
for vowel in vowels:
    # Be careful using keys.  Either use if or try and except
    # to avoid using a key that does not exist.
    try:
        n = result[vowel]
    except KeyError:
        n = 0
    print(f"{vowel}: {n}")
