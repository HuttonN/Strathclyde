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
"""
import random

def play_beetle():
    
    beetle_dict = {
        "body": 0,
        "head": 0,
        "wing": 0,
        "leg": 0,
        "eye": 0,
        "antenna": 0
    }
    
    while beetle_dict["body"] == 0:
        question = input("Roll the dice? (Y/N)")
        if question == "Y":
            roll = random.randint(1,6)
            if roll == 6:
                beetle_dict["body"] +=1
                print("Congratulations! You drew a body")
                break
            else:
                print (f"You rolled a {roll}. Nothing was drawn. Please try again")

    while beetle_dict["head"] == beetle_dict["leg"] == beetle_dict["wing"] ==0:
        question = input("Roll the dice? (Y/N)")
        if question == "Y":
            roll = random.randint(1,6)

play_beetle()
"""

import random

def play_beetle():
    
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

    while not beetle_dict["Drawn?"]:

