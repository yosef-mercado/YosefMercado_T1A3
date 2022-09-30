from combat import combat_loop
from enemy import spawn_enemy
from input_validator import print_delay
from player import spawn_player

current_player = spawn_player()
current_enemy = spawn_enemy()

for encounters in range(5):
    result = combat_loop(current_player, current_enemy)

    if result:
        print("Victory!")
    else:
        print("Game Over!")
        print_delay()

        print("Thank you for playing.")
        print_delay()
        break