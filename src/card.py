from enum import Enum
import random

class Rarities(Enum):
    UNIQUE = "Unique"
    COMMON = "Common"
    RARE = "Rare"
    SUPER_RARE = "Super Rare"

costs = {
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

class Card():
    def __init__(self, name, rarity, cost, effect):
        self.name = name
        self.rarity = rarity
        self.cost = cost
        self.effect = effect