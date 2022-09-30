import random

from card import new_random_card
from card_display import display_card
from combat import read_deck
from player import Player

from input_validator import print_delay
from input_validator import input_index
from input_validator import input_selection

class ExceededDeckSize(Exception):
    pass

def loot(player):
    OPTIONS = ["first", "second"]

    i = 0
    cards = []
    

    for i in range(2):
        cards.append(new_random_card(player.job))

    print("Found the following Cards: ")
    print_delay()

    for card in cards:
        display_card(card)
        print_delay()
        
    print(OPTIONS)
    card_selection = input_selection("> Enter the card you want to add to your deck: ", OPTIONS)

    if card_selection == "first":
        player.deck.append(cards[0])

        print(f"{cards[0].name} added to your deck.")
        print_delay()
    elif card_selection == "second":
        player.deck.append(cards[1])

        print(f"{cards[1].name} added to your deck.")
        print_delay()

    try:
        if len(player.deck) > player.DECK_SIZE:
            raise ExceededDeckSize
    except ExceededDeckSize:
        print(f"Exceeded deck size of {player.DECK_SIZE}.")
        print_delay()

        print(read_deck(player))
        discard_card = input_index("> Enter index of card to discard: ", player.current_deck)
        player.deck.remove(discard_card)

        print(f"Discarded {discard_card.name}.")
        print_delay()

def rest(player):
    rest_hp = random.randint(6, 12)
    player.current_hp = min(player.hp, player.current_hp + rest_hp)
    print(f"After a brief respite, {player.name} recovers {rest_hp} health!")
    print_delay()

def loot_or_rest(player):
    OPTIONS = ["loot", "rest"]

    print("Emerging victorious from combat, you may choose to loot your enemy or rest to heal your wounds.")
    print_delay()

    print(OPTIONS)
    selection = input_selection("> Enter what you would like to do: ", OPTIONS)

    if selection == "loot":
        loot(player)
    elif selection == "rest":
        rest(player)