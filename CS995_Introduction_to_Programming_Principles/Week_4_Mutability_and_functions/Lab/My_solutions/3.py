"""Write a program that includes a function to simulate rolling several dice. The function should accept the
number of dice to be rolled and the number of sides that are on the dice. The function should use the
random.randint function from the random module and add the result from each die roll. The total result
should be returned."""

import random

def roll_dice(number_of_dice, number_of_sides_on_dice):
    dice_total = 0
    for _ in range(number_of_dice):
        dice_total += random.randint(1,number_of_sides_on_dice)
    return dice_total

roll_session = roll_dice(5,6)
print(roll_session)