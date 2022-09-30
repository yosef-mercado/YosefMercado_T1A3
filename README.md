# T1A3 - Terminal Application by Yosef Mercado

[Trello Board](https://trello.com/invite/b/nto8hYJ9/a5e6a22831e723dc2fc435a957138dac/t1a3-heart-of-the-dice-terminal-application)

[PEP 8 Style Guide](https://peps.python.org/pep-0008/)

# Features

## Unique Character Jobs

When starting a new game, the player has a choice of one of three jobs: Fighter, Mage, or Thief. Each of these jobs has their own unique deck and attributes that will heavily influence the difficulty of the early encounters of the game.

## Random Enemy Encounters

When initiating combat, the player will encounter one of three random enemy types: Ninja, Pirate, or Zombie. Each of these enemies has their own unique deck and attributes that makes them more difficult to defeat.

After defeating five of these enemies, the player will come face-to-face with the final boss: the Ninja Pirate Zombie.

## Turn-Based Combat

Combat is inspired by the turn-based systems seen in classic RPGs like Final Fantasy and Persona.

The player will always act first and must utilise actions known as Cards to affect the enemy and themselves. The cost of these Cards is paid using dice that are automatically rolled at the start of the player's turn. Clever use of these dice and a bit of luck is the key to overcoming the enemy. Once the player determines, they can no longer use any more Cards, they must end their turn and pass control over to the enemy.

The enemy has their own deck of Cards and dice, though operating on a different set of rules compared to the player. All of these dice are rolled on each Card, with a roll either being successful or unsuccessful. If a roll is successful, the enemy uses the Card, while an unsuccessful roll will result in the enemy doing nothing.

## Loot or Rest

If the player emerges victorious from combat, they have the choice to loot the enemy or rest.

Looting allows the player to add one randomised Card from a choice of two to their deck. However, if the player has reached the maximum deck capacity of five, they must choose to discard a card.

Resting allows the player to recover between 6 to 12 HP, with this amount being random.

# Dependencies

* Python 3
* pip

# Installation

Installation of the dependencies of this program are faciliated through the use of a bash script run in the bash shell. To execute this script, ensure you are located in the ```src``` directory and enter the following command:

```
./setup.sh
```

# Usage

After the installation of the depenencies, to execute this program, ensure you are located in the ```src``` directory and enter the following command:

```
./game.sh
```

# Tests

## Test 1: Character Creation

This test will test the player's input during the creation of a new character. By passing this test, a valid Player object will be instantiated, which will be used for the remainder of the game's session.

## Naming the Character

### Test Steps

1. Start the game
2. When the prompt "What is your name?" is given, enter the provided data:

| Test Data          | Expected Result                           | Status       |
| -----------        | -----------                               | -----------  |
| whitespace         | "Invalid input. Please enter something."  | Pass         |
| Coder12345_        | "Invalid input. Name must be alphanumeric and a maximum of 16 characters" | Pass |
| CoderAcademy12345  | "Invalid input. Name must be alphanumeric and a maximum of 16 characters" | Pass |
| Coder12345         | Program continues.                        | Pass         |

3. When the prompt "> Enter your job selection: " is given, enter the provided data:

| Test Data          | Expected Result                           | Status       |
| -----------        | -----------                               | -----------  |
| warrior            | "Invalid input. Please enter one of the following options: "  | Pass |
| f1ghter            | "Invalid input. Please enter one of the following options: "  | Pass |
| fighter            | Program continues                         | Pass         |
| Fighter            | Program continues                         | Pass         |
| FiGhTer            | Program continues.                        | Pass         |

## Test 2: Combat Menu

This test will test the player's input when navigating the combat menu. By passing this test, the player will be able to advance the combat state to the enemy's turn or loop back to the start of the combat menu.

### Test Steps

1. Ensure player is in a freshly initiated combat and given the prompt "What will ```Player``` do?"
2. Enter the provided data:

| Test Data          | Expected Result                           | Status       |
| -----------        | -----------                               | -----------  |
| whitespace         | "Invalid input. Please enter something."  | Pass         |
| usecard            | "Invalid input. Please enter one of the following options: "  | Pass |
| endturn            | "Invalid input. Please enter one of the following options: "  | Pass |
| use card           | Program continues to the use card menu    | Pass |
| end turn           | Program continues to enemy turn           | Pass |

3. When the player has advanced to the use card menu and given the prompt "Enter the index of card to use", enter the provided data:

| Test Data          | Expected Result                           | Status       |
| -----------        | -----------                               | -----------  |
| whitespace         | "Invalid input. Please enter an integer." | Pass         |
| card 1             | "Invalid input. Please enter an integer." | Pass         |
| 6                  | "Invalid input. Please enter a valid index." | Pass      |
| 0                  | Program continues to use dice menu        | Pass         |

4. When the player has advanced to the use dice menu and given the prompt "Enter the index of dices to use", enter the provided data:

| Test Data          | Expected Result                           | Status       |
| -----------        | -----------                               | -----------  |
| whitespace         | "Invalid input. Please enter an integer." | Pass         |
| dice 1             | "Invalid input. Please enter an integer." | Pass         |
| 6                  | "Invalid input. Please enter a valid index." s| Pass      |
| *dice that can pay cost of chosen card* | Program continues to value calculation dialogue | Pass |
| *dice that cannot pay cost of chosen card* | "Cannot use this dice on this card." | Pass |