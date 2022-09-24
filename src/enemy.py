import enemy_card_list
import random

from character import Enemy

def new_ninja():
    '''Instantiates the Enemy class with the values of the Ninja enemy.'''
    ninja = Enemy(
        "Ninja",
        16,
        0,
        3,
        enemy_card_list.ninja_deck
        )

    return ninja

def new_pirate():
    '''Instantiates the Enemy class with the values of the Pirate enemy.'''
    pirate = Enemy(
        "Pirate",
        12,
        0,
        2,
        enemy_card_list.pirate_deck
        )
    
    return pirate

def new_zombie():
    '''Instantiates the Enemy class with the values of the Zombie enemy.'''
    zombie = Enemy(
        "Zombie",
        8,
        0,
        1,
        enemy_card_list.zombie_deck
        )

    return zombie

def spawn_enemy():
    '''Instantiates the Enemy class with the values of a random enemy.'''
    possible_enemies = [new_ninja, new_pirate, new_zombie]

    new_enemy = random.choice(possible_enemies)()

    return new_enemy