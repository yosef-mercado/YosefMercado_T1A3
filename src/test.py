import dice
import random
import time

import player
import enemy

from card_display import display_card

def spawn_enemy():
    possible_enemies = [enemy.new_ninja, enemy.new_pirate, enemy.new_zombie]

    new_enemy = random.choice(possible_enemies)()

    return new_enemy

new_enemy = spawn_enemy()

print("A wild " + new_enemy.name + " appears!")


print("What will you do?")