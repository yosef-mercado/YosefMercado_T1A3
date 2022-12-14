from card import Cost
from card import Rarity
from card import Effect

read_cost = {
    Cost.ANY: "Any",
    Cost.ODD: "Odd",
    Cost.EVEN: "Even",
    Cost.ONE: "1",
    Cost.TWO: "2",
    Cost.MIN_TWO: "MIN 2",
    Cost.MAX_TWO: "MAX 2",
    Cost.THREE: "3",
    Cost.MIN_THREE: "MIN 3",
    Cost.MAX_THREE: "MAX 3",
    Cost.FOUR: "4",
    Cost.MIN_FOUR: "MIN 4",
    Cost.MAX_FOUR: "MAX 4",
    Cost.FIVE: "5",
    Cost.MIN_FIVE: "MIN 5",
    Cost.MAX_FIVE: "MAX 5",
    Cost.SIX: "6"
    }

read_rarity = {
    Rarity.COMMON: "Common",
    Rarity.RARE: "Rare",
    Rarity.SUPER_RARE: "Super Rare"
}

def display_name(card):
    print(f"[ {read_rarity[card.rarity]} ] {card.name}")

def display_cost(card):
    print(read_cost[card.cost])

def display_effect(card):
    for effect in card.effect:
        if effect[0] == Effect.DAMAGE_1:
            print(f"Deal {effect[1]} damage")
        elif effect[0] == Effect.DAMAGE_2:
            print(f"Deal X + {effect[1]} damage")
        elif effect[0] == Effect.HEAL:
            print(f"Restore {effect[1]} HP")
        elif effect[0] == Effect.SHIELD:
            print(f"Gain {effect[1]} Shield")

def display_card(card):
    print("----------")
    display_name(card)
    print("Cost:")
    display_cost(card)
    print("Effect: ")
    display_effect(card)
    print("----------")
