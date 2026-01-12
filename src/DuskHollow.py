import os, sys, time
from Player import Player
from Monster import skeleton, rat, wolf
from Weeapon import crossbow
from Diceroll import DiceRoll


def story_prompt():
    """
    Display the opening story prompt for the game.

    Introduces the player character and sets the scene.
    """
    intro_text = [
        "You jolt awake to the creak of wood and the soft clatter of hooves.\n\n"
        "Your horse-drawn carriage slows as it rolls into the sleepy town of "
        "Dusk Hollow, its lanterns flickering weakly against the encroaching dusk.\n\n"
        "Your name is Kael. A monster hunter of local renown. Steel and silver "
        "have earned you coin before, but this job is different.\n\n"
        "A single, unsigned letter summoned you here. Its message was brief, "
        "its warning unmistakable:\n\n"
        "“The old threat has returned.”\n"
    ]

    return intro_text

def typewriter_sliced(text_list, delay) -> None:
    for row in text_list:
        for char in row:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()


def clear_terminal() -> None:
    """
    Clears the terminal of any text

    Designed for both Window and Unix systems
    """
    os.system("cls" if os.name == "NT" else "clear")


def showInstructions() -> None:
    """
    Prints a main menu and the commands
    """
    print("""
    Dusk Hollow Commands
    ========
    Commands:
      go [direction]
      get [item]
      exit
    """)


def status(current_room: str, inventory: list[str], rooms, player) -> None:
    print("------------------")
    player.health_bar.draw()
    print(f"Inventory: {inventory}")
    print(f"Current Room: {current_room}")

    if "item" in rooms[current_room] and rooms[current_room]["item"]:
        room_item: str = rooms[current_room]["item"]
        print(f"You see a {room_item}")

    if "monster" in rooms[current_room] and rooms[current_room]["monster"]:
        room_monster: str = rooms[current_room]["monster"]
        print(f"You see a {room_monster}")

    print("------------------")

def combat(rooms, player: Player, current_room: str) -> None:
    """
    Handle D&D 5e-style turn-based combat between the player and a monster.
    Initiative determines turn order. Attacks use attack rolls vs armour class.
    """
    dice = DiceRoll()
    monster = rooms[current_room]["monster"]

    # Roll initiative
    player_initiative = dice.rollD20() + player.dexterity_modifier
    monster_initiative = dice.rollD20() + monster.dexterity_modifier

    print(f"{player.name} initiative: {player_initiative}")
    print(f"{monster.name} initiative: {monster_initiative}")

    # Determine turn order
    if player_initiative >= monster_initiative:
        turn_order = ("player", "monster")
        print(f"{player.name} acts first!")
    else:
        turn_order = ("monster", "player")
        print(f"{monster.name} acts first!")
    
    while True:
        for actor in turn_order:
            if actor == "player":
                attacker = player
                defender = monster
            else:
                attacker = monster
                defender = player

            # Attack Roll
            attack_roll, is_crit = attacker.roll_attack(dice)
            print(
                f"{attacker.name} attacks! "
                f"(Roll: {attack_roll} vs AC {defender.armour_class})"
            )

            if attack_roll >= defender.armour_class or is_crit:
                damage = attacker.roll_damage(dice, critical=is_crit)
                defender.take_damage(damage)

                if is_crit:
                    print(f"CRITICAL HIT! {attacker.name} deals {damage} damage!")
                else:
                    print(f"{attacker.name} hits for {damage} damage!")
            else:
                print(f"{attacker.name} misses!")

            attacker.health_bar.draw()
            defender.health_bar.draw()
            input()

            # Death checks
            if defender.health <= 0:
                if defender is player:
                    print(f"You have been slain by the {monster.name}.")
                    print("Game over.")
                    sys.exit()
                else:
                    print(f"You have slain the {monster.name}!")
                    del rooms[current_room]["monster"]
                    return


def main() -> None:
    inventory: list[str] = []
    current_room: str = "Hall"
    player = Player(dexterity=14, strength=14, armour_class=12)
    running = True

    rooms = {
        "Garden": {"north": "Dining Room", "item": crossbow.name, "monster": wolf},
        "Dining Room": {"south": "Garden", "west": "Hall", "item": "potion", "monster": rat},
        "Hall": {"south": "Kitchen", "east": "Dining Room", "item": "key"},
        "Kitchen": {"north": "Hall", "item": "Bread", "monster": skeleton},
    }

    typewriter_sliced(story_prompt(), 0.0001) # Set to 0.05 if not testing
    showInstructions()
    
    # Gameplay Loop
    while running:
        status(current_room, inventory, rooms, player)
        move: list[str] = input(">").split(" ", 1)

        clear_terminal()

        if move[0] == "get":
            if move[1] == rooms[current_room]["item"]:
                print(f"You got {move[1]}")
                inventory.append(move[1])
                if rooms[current_room]["item"] == "Crossbow":
                    player.equip(crossbow)
                rooms[current_room]["item"] = ""
            else:
                print(f"You don't see any {move[1]} here")
        elif move[0] == "go":
            if move[1] in rooms[current_room]:
                current_room = rooms[current_room][move[1]]
            else:
                print(f"You can't go {move[1]}")
        elif move[0] == "exit":
            break
        else:
            print("Invalid Command")

        if "key" in inventory and "potion" in inventory and current_room == "Garden":
            print("You have escaped through the garden. You Win")
            break

        if "monster" in rooms[current_room]:
            combat(rooms=rooms, player=player, current_room=current_room)


if __name__ == "__main__":
    main()
