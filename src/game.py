from combat import combat_loop
from enemy import spawn_enemy
from input_validator import print_delay
from player import spawn_player
from loot_rest import loot_or_rest

current_player = spawn_player()
current_enemy = spawn_enemy()

for encounters in range(5):
    result = combat_loop(current_player, current_enemy)

    if result:
        loot_or_rest(current_player)

        print("You soldier forth onto the next battle...")
        print_delay()
    else:
        print("Game Over!")
        print_delay()

        print("Thank you for playing.")
        print_delay()
        break