"""
Python: More functions: Q2
"""


import random


def play_beetle():
    """
    A function to simulate playing the game of beetle.
    """
    n_rolls = 0

    # Variables to remember if we have thrown a six or five.
    have_body = False
    have_head = False
    n_legs = 0
    n_ants = 0
    n_eyes = 0
    n_wings = 0

    # Continue to roll the die until we have completed the beetle.
    while True:
        # Check if the beetle is complete.
        have_beetle = have_body
        have_beetle &= have_head
        have_beetle &= n_legs == 6
        have_beetle &= n_eyes == 2
        have_beetle &= n_ants == 2
        have_beetle &= n_wings == 2

        # If it is complete, then break out of loop.
        if have_beetle:
            break

        # Roll the dice.
        value = random.randint(1, 6)
        n_rolls += 1

        # Have rolled a 6.
        if value == 6:
            have_body = True
            continue

        # Must roll a six before we can build the beetle.
        if not have_body:
            continue

        # Roll a 5 to draw a head.
        if value == 5:
            have_head = True
            continue

        # Roll a 4 to draw a wing.
        if value == 4:
            # Cannot have more than 2 wings.
            if n_wings < 2:
                n_wings += 1

        # Roll a 3 to draw a leg.
        if value == 3:
            # Cannot have more than 6 legs.
            if n_legs < 6:
                n_legs += 1

        # An eye can only be drawn, after a head has been drawn.
        if value == 1 and have_head:
            # Cannot have more than 2 eyes.
            if n_eyes < 2:
                n_eyes += 1

        # An antenna can only be drawn, after a head has been drawn.
        if value == 2 and have_head:
            # Cannot have more than 2 antennae.
            if n_ants < 2:
                n_ants += 1

    # Return the number of rolls to complete the game of beetle.
    return n_rolls


"""
A program to calculate the average number of rolls to complete
a game of beetle.
"""
average = 0
n_games = 100
for i in range(n_games):
    n = play_beetle()
    average += n
average /= n_games
print("Average number of rolls = ", average)
