import random

from aenum import Enum, NoAlias
from character import Job

class Cost(Enum):
    ANY = (1, 2, 3, 4, 5, 6)
    ODD = (1, 3, 5)
    EVEN = (2, 4, 6)
    ONE = 1
    TWO = 2
    MIN_TWO = (2, 3, 4, 5, 6)
    MAX_TWO = (1, 2)
    THREE = 3
    MIN_THREE = (3, 4, 5, 6)
    MAX_THREE = (1, 2, 3)
    FOUR = 4
    MIN_FOUR = (4, 5, 6)
    MAX_FOUR = (1, 2, 3, 4)
    FIVE = 5
    MIN_FIVE = (5, 6)
    MAX_FIVE = (1, 2, 3, 4, 5)
    SIX = 6

class Effect(Enum):
    _settings_ = NoAlias
    DAMAGE_1 = (1, 2, 3, "X")
    DAMAGE_2 = (1, 2, 3,)
    HEAL = (1, 2, 3, "X")
    SHIELD = (1, 2, 3, "X")
    DICE = ("same", "new")

class Rarity(Enum):
    COMMON = 1
    RARE = 2
    SUPER_RARE = 3

class Card():
    def __init__(self, name, rarity, cost):
        self.name = name
        self.rarity = rarity
        self.cost = cost
        self.effect = []

    def add_effect(self, new_effect):
        self.effect.append(new_effect)

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

def new_random_card(player_job):
    random_rarity = random.choice(list(Rarity))
    random_cost = random.choice(list(Cost))

    new_card = Card(
        random_card_name(player_job),
        random_rarity,
        random_cost,
        )

    for i in range(new_card.rarity.value):
        random_effect = random.choice(list(Effect))
        random_value = random_effect.value[random.randint(0, len(random_effect.value) - 1)]

        new_card.add_effect([random_effect, random_value])

    return new_card