import player_card_list

from character import Job
from character import Player

from input_validator import input_name
from input_validator import input_selection

def new_fighter(player_name: str):
    '''Instantiates the Player class with the values of the Fighter job.'''
    fighter = Player(
        player_name,
        Job.FIGHTER,
        30,
        0,
        2,
        player_card_list.fighter_deck
    )

    return fighter

def new_mage(player_name: str):
    '''Instantiates the Player class with the values of the Mage job.'''
    mage = Player(
        player_name,
        Job.MAGE,
        18,
        6,
        3,
        player_card_list.mage_deck
    )

    return mage

def new_thief(player_name: str):
    '''Instantiates the Player class with the values of the Thief job.'''
    thief = Player(
        player_name,
        Job.THIEF,
        24,
        0,
        3,
        player_card_list.thief_deck
    )

    return thief

def spawn_player():
    print("Welcome adventurer!")

    player_name = input_name("What is your name? ")

    print("Duly noted. Now, what job do you specialise as?")
           
    job_options = [job_type.value for job_type in Job]
    job_selection = input_selection("Are you a Fighter, a Mage, or a Thief? ", job_options)

    if job_selection == job_options[0]:
        player = new_fighter(player_name)
    elif job_selection == job_options[1]:
        player = new_mage(player_name)
    elif job_selection == job_options[1]:
        player = new_thief(player_name)

    print("So, you're " + player_name + " the " + job_selection.capitalize() + ", eh?")
    print("Go forth, and may the Heart of the Dice be on your side.")

    return player
