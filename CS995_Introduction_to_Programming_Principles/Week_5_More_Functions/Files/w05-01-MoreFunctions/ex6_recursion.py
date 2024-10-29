def decrement_counter(counter):
    """
    A function to demonstrate recursion.
    The recursive function calls end
    when the counter equals zero.
    """
    print(f"counter: {counter}")
    counter -= 1
    if counter > 0:
        decrement_counter(counter)


# Call the recursive function.
decrement_counter(5)

# Useful for debugging.
pass
