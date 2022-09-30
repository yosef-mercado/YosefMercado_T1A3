import time
import random

import card_display

from enemy import spawn_enemy
from game import PRINT_DELAY
from input_validator import input_index
from input_validator import input_selection
from player import new_mage

class EndCombat(Exception):
    pass

def enemy_logic(enemy, player):
    for card in enemy.deck:
        result = []

        print(f"> {enemy.name} attempts to use {card.name}.")
        time.sleep(PRINT_DELAY)

        for dice in range(enemy.dice):
            coin_flip = random.randint(1, 2)
            
            if coin_flip == 1:
                result.append(True)
            else:
                result.append(False)

        if True in result:
            print(f"{enemy.name} was successful!")
            time.sleep(PRINT_DELAY)

            calculate_values(enemy, player, card, random.randint(1, 6))
        else:
            print(f"{enemy.name} was unsuccessful.")
            time.sleep(PRINT_DELAY)

def calculate_values(current_character, opposing_character, card, dice):
    print(f"> {current_character.name} uses {card.name}.")
    time.sleep(PRINT_DELAY)

    # get damage value from effects
    damage = card.read_effect(dice)[0]
    # get heal value from effects
    heal = card.read_effect(dice)[1]
    # get shield value from effects
    shield = card.read_effect(dice)[2]

    if damage > 0:
        # check if damage does more than current shield first
        remainder = abs(opposing_character.current_shield - damage)
        # then deduct damage from current shield
        opposing_character.current_shield = max(0, opposing_character.current_shield - damage)
        # then deduct damage from current hp if no shield remaining
        if opposing_character.current_shield == 0 and remainder > 0:
            opposing_character.current_hp = max(0, (opposing_character.current_hp - remainder))
        print(f"{current_character.name} dealt {damage} damage!")
        time.sleep(PRINT_DELAY)
        print(f"{opposing_character.name} has {opposing_character.current_hp} HP remaining.")
        time.sleep(PRINT_DELAY)

        # end combat if damage reduces opponent to 0 HP
        if opposing_character.current_hp == 0:
            raise EndCombat
    if heal > 0:
        # prevent healing above character's maximum hp
        current_character.current_hp = min(current_character.hp, current_character.current_hp + heal)
        print(f"{current_character.name} restores {heal} health!")
        time.sleep(PRINT_DELAY)
        print(f"{current_character.name} has {current_character.current_hp} HP remaining.")
        time.sleep(PRINT_DELAY)
    if shield > 0:
        current_character.current_shield = current_character.current_shield + shield
        time.sleep(PRINT_DELAY)
        print(f"{current_character.name} gains {shield} shield!")
        time.sleep(PRINT_DELAY)

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
            menu_use_card(player, enemy)
        # my status command
        elif command == "my status":
            menu_player_status(player)
        # enemy status command
        elif command == "enemy status":
            menu_enemy_status(enemy)
        # end turn command
        elif command == "end turn":
            break

def menu_use_card(player, enemy):
    print(read_deck(player))
    chosen_card = input_index("> Enter index of card to use: ", player.current_deck)

    print(read_dice(player))
    chosen_dice = input_index("> Enter index of dice to use: ", player.current_dice)

    if chosen_dice not in chosen_card.cost.value:
        print(f"Cannot use this dice on this card. {chosen_card.name} ({card_display.read_cost[chosen_card.cost]}) only accepts dice values of {chosen_card.cost.value}")
    else:
        calculate_values(player, enemy, chosen_card, chosen_dice)
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

def combat_loop(player, enemy):
    print(f"A wild {enemy.name} appears!")
    time.sleep(PRINT_DELAY)

    try:
        while True:
            # player turn
            player.turn_dice() # refresh player dice
            player.turn_deck() # refresh player deck

            print(f"{player.name}'s turn.")
            time.sleep(PRINT_DELAY)

            print(f"> {player.name} rolls their dice.")
            time.sleep(PRINT_DELAY)

            status_dice(player)
            time.sleep(PRINT_DELAY)

            menu_combat(player, enemy)

            print(f"{player.name} ends their turn.")
            time.sleep(PRINT_DELAY)

            # enemy turn
            print(f"{enemy.name}'s turn.")
            time.sleep(PRINT_DELAY)

            enemy_logic(enemy, player)

            print(f"{enemy.name} ends their turn.")
            time.sleep(PRINT_DELAY)
    except EndCombat:
        if enemy.current_hp == 0:
            return True
        else:
            return False