from input_validator import input_str
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
    player = Player(
        player_name(),
        "Fighter",
        30,
        0,
        2,
        [],
        5
    )

    return player

# def new_mage():


# def new_thief():