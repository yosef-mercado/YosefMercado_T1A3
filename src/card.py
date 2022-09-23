import random

from character import Job
from enum import Enum

COSTS = {
    "Any": [1, 2, 3, 4, 5, 6],
    "Odd": [1, 3, 5],
    "Even": [2, 4, 6],
    "1": 1,
    "2": 2,
    "Min2": [2, 3, 4, 5, 6],
    "Max2": [1, 2],
    "3": 3,
    "Min3": [3, 4, 5, 6],
    "Max3": [1, 2, 3],
    "4": 4,
    "Min4": [4, 5, 6],
    "Max4": [1, 2, 3, 4],
    "5": 5,
    "Min5": [5, 6],
    "Max5": [1, 2, 3, 4, 5],
    "6": 6,
    }

class Rarity(Enum):
    UNIQUE = "Unique"
    COMMON = "Common"
    RARE = "Rare"
    SUPER_RARE = "Super Rare"

class Card():
    def __init__(self, name, rarity, cost, effect):
        self.name = name
        self.rarity = rarity
        self.cost = cost
        self.effect = effect

def random_card_name(player_job):
    ADJECTIVES = (
        "Ordinary", "Magical",
        "Brand New", "Antiquated",
        "Authentic", "Fake",
        "Shiny", "Rusted",
        "Angelic", "Hellish",
        )
    FIGHTER_WEAPONS = ("Axe", "Mace", "Sword")
    MAGE_WEAPONS = ("Rod", "Staff", "Wand")
    THIEF_WEAPONS = ("Crossbow", "Dagger", "Short Sword")

    adjective = random.choice(ADJECTIVES)

    if player_job == Job.FIGHTER:
        weapon = random.choice(FIGHTER_WEAPONS)
    elif player_job == Job.MAGE:
        weapon = random.choice(MAGE_WEAPONS)
    elif player_job == Job.THIEF:
        weapon = random.choice(THIEF_WEAPONS)

    return adjective + " " + weapon