import time

from enemy import spawn_enemy
from game import PRINT_DELAY
from input_validator import input_index
from input_validator import input_selection
from player import new_mage

import card_display

def read_dice(character):
    dice_with_index = []

    for index, dice in enumerate(character.current_dice):
        dice_with_index.append(f"{index}. {dice}")

    return dice_with_index

def read_deck(character):
    cards_with_index = []

    for index, card in enumerate(character.current_deck):
        cards_with_index.append(f"{index}. {card.name} ({card_display.read_cost[card.cost]})")
    
    return cards_with_index

def status_health(character):
    print(f"{character.name}'s status: ")
    print(f"HP: {character.current_hp} / {character.hp}")

    if character.current_shield > 0:
        print(f"Shield: {character.current_shield}")

def status_dice(character):
    print(f"{character.name}'s dice: ")
    print(read_dice(character))

def status_deck(character):
    print(f"{character.name}'s deck: ")
    print(read_deck(character))

def menu_combat(player, enemy):
    COMBAT_MENU = ["use card", "my status", "enemy status", "end turn"]
    
    while True:
        print(f"What will {player.name} do?")
        time.sleep(PRINT_DELAY)

        # combat menu
        print(COMBAT_MENU)
        command = input_selection("> Enter command: ", COMBAT_MENU)

        # use card command if deck is empty
        if command == "use card" and not player.current_deck:
            print("No more cards remaining in deck.")
            time.sleep(PRINT_DELAY)
        # use card command
        elif command == "use card":
            menu_use_card(player)
        # my status command
        elif command == "my status":
            menu_player_status(player)
        # enemy status command
        elif command == "enemy status":
            menu_enemy_status(enemy)
        # end turn command
        elif command == "end turn":
            break

def menu_use_card(player):
    print(read_deck(player))
    chosen_card = input_index("> Enter index of card to use: ", player.current_deck)

    print(read_dice(player))
    chosen_dice = input_index("> Enter index of dice to use: ", player.current_dice)

    if chosen_dice not in chosen_card.cost.value:
        print(f"Cannot use this dice on this card. {chosen_card.name} ({card_display.read_cost[chosen_card.cost]}) only accepts dice values of {chosen_card.cost.value}")
    else:
        player.current_deck.remove(chosen_card)
        player.current_dice.remove(chosen_dice)

def menu_player_status(player):
    PLAYER_STATUS_MENU = ["health", "dice", "deck", "return"]

    print(PLAYER_STATUS_MENU)
    command = input_selection("> Enter command: ", PLAYER_STATUS_MENU)

    # player health command
    if command == "health":
        status_health(player)
        time.sleep(PRINT_DELAY)
    # player dice command
    elif command == "dice":
        status_dice(player)
        time.sleep(PRINT_DELAY)
    # player deck command if deck is empty
    elif command == "deck" and not player.current_deck:
        print("No more cards remaining in deck.")
        time.sleep(PRINT_DELAY)
    # player deck command
    elif command == "deck":
        status_deck(player)
        time.sleep(PRINT_DELAY)

        menu_card_info(player)
        time.sleep(PRINT_DELAY)
    # return to combat menu
    elif command == "return":
        pass

def menu_enemy_status(enemy):
    ENEMY_STATUS_MENU = ["health", "deck", "return"]

    print(ENEMY_STATUS_MENU)
    command = input_selection("> Enter command: ", ENEMY_STATUS_MENU)

    # enemy health command
    if command == "health":
        status_health(enemy)
        time.sleep(PRINT_DELAY)
    # enemy deck command
    elif command == "deck":
        status_deck(enemy)
        time.sleep(PRINT_DELAY)

        menu_card_info(enemy)
        time.sleep(PRINT_DELAY)
    # return to combat menu
    elif command == "return":
        pass

def menu_card_info(character):
    DECK_MENU = ["card info", "return"]

    print(DECK_MENU)
    command = input_selection("> Enter command: ", DECK_MENU)

    # card info command
    if command == "card info":
        card = input_index("> Enter index of card to view: ", character.current_deck)
        time.sleep(PRINT_DELAY)

        card_display.display_card(card)

    # return to combat menu
    elif command == "return":
        pass

# calls
current_player = new_mage("Novice Mage")

# begin encounter
current_enemy = spawn_enemy()

print(f"A wild {current_enemy.name} appears!")
time.sleep(PRINT_DELAY)

# player turn
current_player.turn_dice() # refresh player dice
current_player.turn_deck() # refresh player deck

print(f"{current_player.name}'s turn.")
time.sleep(PRINT_DELAY)

print(f"> {current_player.name} rolls their dice.")
time.sleep(PRINT_DELAY)

status_dice(current_player)
time.sleep(PRINT_DELAY)

menu_combat(current_player, current_enemy)