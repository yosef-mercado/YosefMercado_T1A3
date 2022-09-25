import dice
import random
import time

from player import spawn_player
from player import new_fighter
from player import new_mage
from enemy import spawn_enemy
from input_validator import input_index
from input_validator import input_selection

import card_display

PRINT_DELAY = 1

COMBAT_MENU = ["use card", "my status", "my deck", "enemy status", "enemy deck", "end turn"]

def status_health(character):
    print(f"{character.name}'s status: ")
    time.sleep(PRINT_DELAY)

    print(f"HP: {character.current_hp} / {character.hp}")

    if character.current_shield > 0:
        time.sleep(PRINT_DELAY)
        print(f"Shield: {character.current_shield}")

def status_dice(character, dice_pool):
    dice_with_index = []

    for index, dice in enumerate(dice_pool):
        dice_with_index.append(f"{index}. {dice}")

    print(f"{character.name}'s dice: ")
    time.sleep(PRINT_DELAY)

    print(dice_with_index)

def status_deck(character, deck):
    cards_with_index = []

    for index, card in enumerate(deck):
        cards_with_index.append(f"{index}. {card.name} ({card_display.read_cost[card.cost]})")

    print(f"{character.name}'s deck: ")
    time.sleep(PRINT_DELAY)

    print(cards_with_index)

# calls

current_player = new_fighter("Test Player")

# begin encounter
current_enemy = spawn_enemy()

print(f"A wild {current_enemy.name} appears!")
time.sleep(PRINT_DELAY)

# player turn
current_deck = current_player.deck.copy()

print(f"{current_player.name}'s turn.")
time.sleep(PRINT_DELAY)

current_dice_pool = dice.roll(f"{current_player.dice}d6")

print(f"{current_player.name} rolls their dice.")
time.sleep(PRINT_DELAY)

status_dice(current_player, current_dice_pool)
time.sleep(PRINT_DELAY)

print(f"{current_player.name} checks their deck.")
time.sleep(PRINT_DELAY)

status_deck(current_player, current_deck)
time.sleep(PRINT_DELAY)

print(f"What will {current_player.name} do?")
print(COMBAT_MENU)