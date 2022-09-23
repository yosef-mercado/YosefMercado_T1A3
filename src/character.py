from enum import Enum

class Job(Enum):
    FIGHTER = "Fighter"
    MAGE = "Mage"
    THIEF = "Thief"

class Character():
    def __init__(self, name, hp, shield, dice, deck):
        self.name = name
        self.hp = hp
        self.current_hp = hp
        self.shield = shield
        self.current_shield = shield
        self.dice = dice
        self.deck = deck

class Player(Character):
    DECK_SIZE = 5

    def __init__(self, name, job, hp, shield, dice, deck):
        super().__init__(name, hp, shield, dice, deck)
        self.job = job

class Enemy(Character):
    pass