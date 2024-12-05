"""
Python: Functions: Q7
"""


def int_to_char(mapping, input_str):
    """
    A function to convert an input series of numbers
    into a character string.
    """
    output_str = ""
    for s in input_str.split("|"):
        try:
            i = int(s)
        except ValueError:
            continue

        if i not in mapping.keys():
            continue
        c = mapping[i]
        output_str += c
    return output_str


mapping = {
    1: "a",
    2: "b",
    26: "z",
}
s = int_to_char(mapping, "1|2|26")
print(s)
