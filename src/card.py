import random

rarities = [
    "Unique",
    "Common",
    "Rare",
    "Super Rare"
    ]

x = random.randint(1, 6)

costs = {
    "Any": [1, 2, 3, 4, 5, 6],
    "Odd": [1, 3, 5],
    "Even": [2, 4, 6],
    str(x): x,
    "Min " + str(x): [],
    "Max " + str(x): []
    }

class Card():
    def __init__(self, name, rarity, cost, effect):
        self.name = name
        self.rarity = rarity
        self.cost = cost
        self.effect = effect


print(costs)