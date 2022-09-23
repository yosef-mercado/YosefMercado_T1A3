from input_validator import input_str

from character import Job
from character import Player

def player_name():
    CHARACTER_LIMIT = 16
    
    while True:
        name = input_str("Please enter your name: ")

        if not name.isalnum() or len(name) > CHARACTER_LIMIT:
            print("Invalid input. Name must be alphanumeric and a maximum of 16 characters.")
            continue

        return name

def new_fighter():
    fighter = Player(
        player_name(),
        Job.FIGHTER,
        30,
        0,
        2,
        []
    )

    return fighter

def new_mage():
    mage = Player(
        player_name(),
        Job.MAGE,
        18,
        6,
        3,
        []
    )

    return mage

def new_thief():
    thief = Player(
        player_name(),
        Job.THIEF,
        24,
        0,
        3,
        []
    )

    return thief