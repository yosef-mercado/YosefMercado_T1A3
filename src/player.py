import player_card_list

from character import Job
from character import Player
from input_validator import input_str

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
        player_card_list.fighter_deck
    )

    return fighter

def new_mage():
    mage = Player(
        player_name(),
        Job.MAGE,
        18,
        6,
        3,
        player_card_list.mage_deck
    )

    return mage

def new_thief():
    thief = Player(
        player_name(),
        Job.THIEF,
        24,
        0,
        3,
        player_card_list.thief_deck
    )

    return thief