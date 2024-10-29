"""Write a function to simulate the game of beetle. Then write a program to play 100 games and calculate
the average number of dice rolls need to complete the game.
The rules of the game of beetle are:
• A six-sided die is used.
• A six must be thrown to draw a body.
• A five must be thrown to draw a head. A head cannot be drawn unless a body has been drawn.
• A four must be thrown to draw a wing. A wing cannot be drawn unless a body has been drawn.
• A three must be thrown to draw a leg. A leg cannot be drawn unless a body has been drawn.
• A one must be thrown to drawn an eye. An eye cannot be drawn unless a head has been drawn.
• A two must be thrown to drawn an antenna. An antenna cannot be drawn unless a head has been
drawn.
• A beetle is complete when one head, two wings, six legs, a head, two eyes and two antennae have
been dawn. The game ends when the beetle is complete.
• Additional body members beyond those required are not drawn"""

import random

def play_beetle(interactive=True):
    
    beetle_dict = {
        "anatomy":{
            "body": {
                "dice_value" : 6,
                "dependencies": None,
                "count": 0,
                "max_no": 1
                },
            "head": {
                "dice_value" : 5,
                "dependencies": "body",
                "count": 0,
                "max_no": 1
                },
            "wing": {
                "dice_value" : 4,
                "dependencies": "body",
                "count": 0,
                "max_no": 2
                },
            "leg": {
                "dice_value" : 3,
                "dependencies": "body",
                "count": 0,
                "max_no": 6
                },
            "eye": {
                "dice_value" : 1,
                "dependencies": "head",
                "count": 0,
                "max_no": 2
                },
            "antenna": {
                "dice_value" : 2,
                "dependencies": "head",
                "count": 0,
                "max_no": 2
                }
        },
        "Drawn?": False
    }

    def can_add_part(part):
        dependency = beetle_dict["anatomy"][part]["dependencies"]
        if dependency is None or beetle_dict["anatomy"][dependency]["count"] == beetle_dict["anatomy"][dependency]["max_no"]:
            return beetle_dict["anatomy"][part]["count"] < beetle_dict["anatomy"][part]["max_no"]
        return False

    def check_completed():
        beetle_dict["Drawn?"] = True
        for part in beetle_dict["anatomy"]:
            part_info = beetle_dict["anatomy"][part]
            if part_info["count"] == part_info["max_no"]:
                continue
            beetle_dict["Drawn?"] = False

    roll_count = 0

    while not beetle_dict["Drawn?"]:
        if interactive:
            input("Press Enter to roll the dice")
        roll = random.randint(1,6)
        roll_count += 1
        if interactive:
            print(f"You rolled a {roll}")

        part_drawn = False

        for part in beetle_dict["anatomy"]:
            part_info = beetle_dict["anatomy"][part]
            if part_info["dice_value"] == roll and can_add_part(part):
                part_info["count"] +=1
                if interactive:
                    print(f"You drew a {part}")
                part_drawn = True
                break
        
        if not part_drawn and interactive:
            print("Nothing was drawn with this roll")
        
        check_completed()

    if interactive:
        print(f"Congratulations. You completed the game of beetle in {roll_count} rolls")

    return roll_count

def simulate_games(num_games):
    total_rolls = 0
    for _ in range(num_games):
        total_rolls += play_beetle(interactive=False)
    average_rolls = total_rolls/num_games
    print(f"The average number of rolls to complete beetle in {num_games} games was {average_rolls}")

play_beetle()
