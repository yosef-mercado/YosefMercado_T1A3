from combat import combat_loop
from enemy import spawn_enemy
from enemy import new_final_boss
from input_validator import print_delay
from player import spawn_player
from loot_rest import loot_or_rest

current_player = spawn_player()

NUMBER_OF_ENCOUNTERS = 5

# regular encounters
for encounters in range(NUMBER_OF_ENCOUNTERS):
    current_enemy = spawn_enemy()

    print("----------")
    print(f"Encounter {encounters + 1} / {NUMBER_OF_ENCOUNTERS}")
    print("----------")
    print_delay()

    result = combat_loop(current_player, current_enemy)

    if result:
        loot_or_rest(current_player)

        print(f"{current_player.name} soldiers forth onto the next battle...")
        print_delay()
    else:
        print("Game Over!")
        print_delay()

        print("You didn't even make it to the final boss...")
        print_delay()
        break

# final boss encounter
final_boss = new_final_boss()

print("----------")
print("The Final Boss")
print("----------")
print_delay()

result = combat_loop(current_player, final_boss)

if result:
    print(f"{current_player.name} has conquered the dungeon!")
    print_delay()

    print("Thank you for playing.")
else:
    print("Game Over!")
    print_delay()

    print("So close, yet so far...")
    