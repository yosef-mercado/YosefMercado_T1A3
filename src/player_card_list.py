from card import Card
from card import Cost
from card import Effect
from card import Rarity

# unique preset Cards for the Fighter job
# Fighter job card 1: Adventurer's Sword
fighter_card_1 = Card(
    "Adventurer's Sword",
    Rarity.SUPER_RARE,
    Cost.MAX_FOUR,
    )

fighter_card_1.add_effect([Effect.DAMAGE_2, Effect.DAMAGE_2.value[0]])

# Fighter job card 2: Adventurer's Potion
fighter_card_2 = Card(
    "Adventurer's Potion",
    Rarity.SUPER_RARE,
    Cost.ODD,
)

fighter_card_2.add_effect([Effect.HEAL, Effect.HEAL.value[1]])

# unique preset Cards for the Mage job
# Mage job card 1: Adventurer's Wand
mage_card_1 = Card(
    "Adventurer's Wand",
    Rarity.SUPER_RARE,
    Cost.ANY
    )

mage_card_1.add_effect([Effect.DAMAGE_1, Effect.DAMAGE_1.value[1]])

# Mage job card 1: Adventurer's Fireball
mage_card_2 = Card(
    "Adventurer's Fireball",
    Rarity.SUPER_RARE,
    Cost.MIN_FOUR
    )

mage_card_2.add_effect([Effect.DAMAGE_1, Effect.DAMAGE_1.value[3]])

# unique preset Cards for the Thief job
# Thief job card 1: Adventurer's Dagger
thief_card_1 = Card(
    "Adventurer's Dagger",
    Rarity.SUPER_RARE,
    Cost.ANY
    )

thief_card_1.add_effect([Effect.DAMAGE_1, Effect.DAMAGE_1.value[3]])

# Thief job card 2: Adventurer's Rock
thief_card_2 = Card(
    "Adventurer's Rock",
    Rarity.SUPER_RARE,
    Cost.ANY
)

thief_card_2.add_effect([Effect.DAMAGE_1, Effect.DAMAGE_1.value[0]])

# job starting decks
fighter_deck = [fighter_card_1, fighter_card_2]
mage_deck = [mage_card_1, mage_card_2]
thief_deck = [thief_card_1, thief_card_2]