import enum

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
    def __init__(self, name, job, hp, shield, dice, deck, deck_size):
        super().__init__(name, hp, shield, dice, deck)
        self.job = job
        self.deck_size = deck_size

class Enemy(Character):
    pass