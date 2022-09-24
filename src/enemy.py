import enemy_card_list

from character import Enemy

def new_ninja():
    ninja = Enemy(
        "Ninja",
        16,
        0,
        3,
        enemy_card_list.ninja_deck
        )

    return ninja

def new_pirate():
    pirate = Enemy(
        "Pirate",
        12,
        0,
        2,
        enemy_card_list.pirate_deck
        )
    
    return pirate

def new_zombie():
    zombie = Enemy(
        "Zombie",
        8,
        0,
        1,
        enemy_card_list.zombie_deck
        )

    return zombie