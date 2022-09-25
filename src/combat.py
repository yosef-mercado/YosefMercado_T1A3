import dice
import time

from player import spawn_player
from player import new_mage
from enemy import spawn_enemy
from input_validator import input_index
from input_validator import input_selection

import card_display

PRINT_DELAY = 1



def status_health(character):
    print(f"{character.name}'s status: ")
    print(f"HP: {character.current_hp} / {character.hp}")

    if character.current_shield > 0:
        print(f"Shield: {character.current_shield}")

def status_dice(character):
    dice_with_index = []

    for index, dice in enumerate(character.current_dice):
        dice_with_index.append(f"{index}. {dice}")

    print(f"{character.name}'s dice: ")
    print(dice_with_index)

def status_deck(character):
    cards_with_index = []

    for index, card in enumerate(character.current_deck):
        cards_with_index.append(f"{index}. {card.name} ({card_display.read_cost[card.cost]})")

    print(f"{character.name}'s deck: ")
    print(cards_with_index)

def combat_menu(player):
    COMBAT_MENU = ["use card", "my status", "enemy status", "end turn"]
    STATUS_MENU = ["health", "dice", "deck"]

    print(f"What will {player.name} do?")
    time.sleep(PRINT_DELAY)

    print(COMBAT_MENU)

    command = input_selection("Enter command: ", COMBAT_MENU)

    if command == "use card":
        pass
    elif command == "my status":
        print(STATUS_MENU)
        command = input_selection("Enter command: ", STATUS_MENU)

        if command == "health":
            status_health(player)
        elif command == "dice":
            status_dice(player)
        elif command == "deck":
            status_deck(player)
    elif command == "enemy status":
        print(STATUS_MENU)
    elif command == "end turn":
        pass

# calls
current_player = new_mage("Noice Mage")

# begin encounter
current_enemy = spawn_enemy()

print(f"A wild {current_enemy.name} appears!")
time.sleep(PRINT_DELAY)

# player turn
current_player.turn_deck()

print(f"{current_player.name}'s turn.")
time.sleep(PRINT_DELAY)

current_player.turn_dice()
print(f"{current_player.name} rolls their dice.")
time.sleep(PRINT_DELAY)

status_dice(current_player)
time.sleep(PRINT_DELAY)

print(f"{current_player.name} checks their deck.")
time.sleep(PRINT_DELAY)

status_deck(current_player)
time.sleep(PRINT_DELAY)

combat_menu(current_player)