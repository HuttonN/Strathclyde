"""
Python: Functions: Q6
"""


def char_to_int(mapping, input_str):
    """
    A function to convert an input string to integers,
    using an input mapping dictionary.
    """
    output_str = ""
    for c in input_str:
        if c not in mapping.keys():
            continue
        i = mapping[c]
        if len(output_str) > 0:
            output_str += "|"
        output_str += str(i)
    return output_str


mapping = {
    "a": 1,
    "b": 2,
    "z": 26,
}
s = char_to_int(mapping, "abz")
print(s)
