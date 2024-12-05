import random
from config_svc import ConfigSvc


def check_config(config):
    """
    A function to check that the configuration file format
    is correct.
    """
    try:
        # Check the dice configuration values.
        dice = config.config()["dice"]
        if not isinstance(dice, list):
            print("\"dice\" must be a list.")
            return False
        for die in dice:
            if not isinstance(die["n_sides"], int):
                print("\"n_sides\" must be an integer.")
                return False
            if die["n_sides"] <= 0:
                print("\"n_sides\" must be greater than zero.")
                return False

        # Check that the number of rolls is valid.
        n_rolls = config.config()["n_rolls"]
        if not isinstance(n_rolls, int):
            print("\"n_rolls\" must be an integer value.")
            return False
        if n_rolls <= 0:
            print("\"n_rolls\" must be greater than zero.")
            return False
    except KeyError as e:
        print("Configuration error:")
        print(e)
        return False
    return True


def average_dice_total(config):
    """
    A function to simulate rolling one or more dice
    a specified number of times.
    """
    
    # Verify the format of the configuration.
    if not check_config(config):
        return None

    dice_config = config.config()["dice"]

    # To avoid using a string key within the simulation loop.
    n_sides_values = []
    for die_config in dice_config:
        n_sides_values.append(die_config["n_sides"])

    n_rolls = config.config()["n_rolls"]
    average = 0
    for _ in range(n_rolls):
        # Roll all of the dice and calculate the total.
        total = 0
        for n_sides in n_sides_values:
            total += random.randint(1, n_sides)
        
        # Form the average over the total number of rolls.
        average += total/n_rolls
    return average


"""
A program to calculate the average value from rolling
several dice with different numbers of sides.
"""
if __name__ == "__main__":
    config = ConfigSvc("dice_config.json")
    average = average_dice_total(config)
    print(config.config())
    print(f"average={average}")
