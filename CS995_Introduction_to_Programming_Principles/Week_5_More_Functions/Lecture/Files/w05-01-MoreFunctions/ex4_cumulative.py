def cumulative_total(input_list,
                     output_total):
    """
    A function to calculate the cumulative
    total value for integers in an input
    list.
    """
    output_total.clear()
    n = len(input_list)
    output_total += [0]*n
    for i in range(n):
        output_total[i] = input_list[i]
        if i > 0:
            output_total[i] += output_total[i-1]


"""
A program to demonstrate calculating the cumulative
total.
"""
values = [
    1,
    2,
    3
]
output = []
cumulative_total(values, output)
print(output)
