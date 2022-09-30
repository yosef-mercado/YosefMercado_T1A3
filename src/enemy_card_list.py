from card import Card
from card import Cost
from card import Effect
from card import Rarity

# unique preset Cards for the Ninja
# Ninja Card 1: Kunai
ninja_card_1 = Card(
    "Kunai",
    Rarity.COMMON,
    Cost.MIN_FOUR
    )

ninja_card_1.add_effect([Effect.DAMAGE_2, Effect.DAMAGE_2.value[0]])

# Ninja Card 2: Ninja Log
ninja_card_2 = Card(
    "Ninja Log",
    Rarity.COMMON,
    Cost.ODD
)

ninja_card_2.add_effect([Effect.SHIELD, Effect.SHIELD.value[1]])

# unique preset Cards for the Pirate
# Pirate Card 1: Cutlass
pirate_card_1 = Card(
    "Cutlass",
    Rarity.COMMON,
    Cost.ANY,
    )

pirate_card_1.add_effect([Effect.DAMAGE_1, Effect.DAMAGE_1.value[3]])

# unique preset Cards for the Zombie
# Zombie Card 1: Scratch
zombie_card_1 = Card(
    "Scratch",
    Rarity.COMMON,
    Cost.EVEN
    )

zombie_card_1.add_effect([Effect.DAMAGE_1, Effect.DAMAGE_1.value[3]])

# Zombie Card 2: Bite
zombie_card_2 = Card(
    "Bite",
    Rarity.COMMON,
    Cost.ODD
    )

zombie_card_2.add_effect([Effect.HEAL, Effect.HEAL.value[0]])

# enemy decks
ninja_deck = [ninja_card_1, ninja_card_2]
pirate_deck = [pirate_card_1, pirate_card_1]
zombie_deck = [zombie_card_1, zombie_card_2]
final_boss_deck = [ninja_card_1, pirate_card_1, zombie_card_2]
