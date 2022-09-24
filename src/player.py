import player_card_list

from character import Job
from character import Player
from input_validator import input_name
from input_validator import input_str
from input_validator import input_selection

def new_fighter(player_name):
    fighter = Player(
        player_name,
        Job.FIGHTER,
        30,
        0,
        2,
        player_card_list.fighter_deck
    )

    return fighter

def new_mage(player_name):
    mage = Player(
        player_name,
        Job.MAGE,
        18,
        6,
        3,
        player_card_list.mage_deck
    )

    return mage

def new_thief(player_name):
    thief = Player(
        player_name,
        Job.THIEF,
        24,
        0,
        3,
        player_card_list.thief_deck
    )

    return thief

def new_player():
    print("Welcome adventurer!")
    print("What is your name?")

    # Player Name loop
    while True:
        player_name = input_name()
        print("Your name is " + player_name + ". Is this correct?")
    
        options = ["yes", "no"]

        selection = input_selection(options)

        if selection == options[0]: # if yes, break loop
            break
        if selection == options[1]: # if no, continue loop
            continue

    print("Excellent! Now, please select one of the following jobs to specialise as: ")

    # Job Selection loop
    options = [job_type.value for job_type in Job]

    selection = input_selection(options)

    if selection == options[0]: # if fighter, instantiate Player object with values of Fighter job
        player = new_fighter(player_name)


new_player()
