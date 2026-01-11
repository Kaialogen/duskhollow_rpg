import os, sys, time
from Player import Player
from Monster import Monster
from Weeapon import wooden_club, crossbow


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


def status(currentRoom: str, inventory: list[str], rooms, player) -> None:
    print("------------------")
    player.health_bar.draw()
    print(f"Inventory: {inventory}")
    print(f"Current Room: {currentRoom}")

    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
        room_item: str = rooms[currentRoom]["item"]
        print(f"You see a {room_item}")

    if "monster" in rooms[currentRoom] and rooms[currentRoom]["monster"]:
        room_monster: str = rooms[currentRoom]["monster"]
        print(f"You see a {room_monster}")

    print("------------------")


def main() -> None:
    inventory: list[str] = []
    currentRoom: str = "Hall"
    player = Player()
    skeleton = Monster(name="Skeleton", health=30, damage=10, weapon=wooden_club)

    rooms = {
        "Garden": {"north": "Dining Room", "item": crossbow.name},
        "Dining Room": {"south": "Garden", "west": "Hall", "item": "potion"},
        "Hall": {"south": "Kitchen", "east": "Dining Room", "item": "key"},
        "Kitchen": {"north": "Hall", "item": "Bread", "monster": skeleton},
    }

    typewriter_sliced(story_prompt(), 0.05)
    showInstructions()

    # Gameplay Loop
    while True:
        status(currentRoom, inventory, rooms, player)
        move: list[str] = input(">").split(" ", 1)

        clear_terminal()

        if move[0] == "get":
            if move[1] == rooms[currentRoom]["item"]:
                print(f"You got {move[1]}")
                inventory.append(move[1])
                if rooms[currentRoom]["item"] == "Crossbow":
                    player.equip(crossbow)
                rooms[currentRoom]["item"] = ""
            else:
                print(f"You don't see any {move[1]} here")
        elif move[0] == "go":
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print(f"You can't go {move[1]}")
        elif move[0] == "exit":
            break
        else:
            print("Invalid Command")

        if "key" in inventory and "potion" in inventory and currentRoom == "Garden":
            print("You have escaped through the garden. You Win")
            break

        if "monster" in rooms[currentRoom]:
            while True:
                player.melee_attack(skeleton)
                skeleton.attack(player)
                player.health_bar.draw()
                skeleton.health_bar.draw()
                input()
                if skeleton.health == 0:
                    break
            print(f"You defeated the {rooms[currentRoom]['monster']}")
            print("You Win")
            break


if __name__ == "__main__":
    main()
