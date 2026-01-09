import os


def story_prompt() -> str:
    """
    Display the opening story prompt for the game.

    Introduces the player character and sets the scene.
    """
    intro_text: str = (
        "You jolt awake to the creak of wood and the soft clatter of hooves.\n\n"
        "Your horse-drawn carriage slows as it rolls into the sleepy town of "
        "Dusk Hollow, its lanterns flickering weakly against the encroaching dusk.\n\n"
        "Your name is Kael. A monster hunter of local renown. Steel and silver "
        "have earned you coin before, but this job is different.\n\n"
        "A single, unsigned letter summoned you here. Its message was brief, "
        "its warning unmistakable:\n\n"
        "“The old threat has returned.”\n"
    )

    return intro_text


def clear_terminal() -> None:
    """
    Clears the terminal of any text

    Designed for both Window and Unix systems
    """
    os.system('cls' if os.name == 'NT' else "clear")


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
    """)


def status(currentRoom: str, inventory: list[str], rooms) -> None:
    print("------------------")
    print(f"Current Room: {currentRoom}")
    print(f"Inventory: {inventory}")

    if "item" in rooms[currentRoom] and rooms[currentRoom]["item"]:
        room_item = rooms[currentRoom]["item"]
        print(f"You see a {room_item}")

    if "monster" in rooms[currentRoom] and rooms[currentRoom]["monster"]:
        room_monster = rooms[currentRoom]["monster"]
        print(f"You see a {room_monster}")

    print("------------------")


def main() -> None:
    inventory = []
    currentRoom = "Hall"

    rooms = {
        "Garden": {"north": "Dining Room", "item": "Golden sword"},
        "Dining Room": {"south": "Garden", "west": "Hall", "item": "potion"},
        "Hall": {"south": "Kitchen", "east": "Dining Room", "item": "key"},
        "Kitchen": {"north": "Hall", "item": "Bread", "monster": "Skeleton"},
    }

    print(story_prompt())
    showInstructions()

    while True:
        status(currentRoom, inventory, rooms)
        move: str = input(">")
        move: list[str] = move.split(" ", 1)

        clear_terminal()

        if move[0] == "get":
            if move[1] == rooms[currentRoom]["item"]:
                print(f"You got {move[1]}")
                inventory.append(move[1])
                rooms[currentRoom]["item"] = ""
            else:
                print(f"You don't see any {move[1]} here")
        elif move[0] == "go":
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print(f"You can't go {move[1]}")

        # Win Condition 1: Escape through the garden
        if "key" in inventory and "potion" in inventory and currentRoom == "Garden":
            print("You Win")
            break

        # Loss Condition: Defeated by the monsters
        if "monster" in rooms[currentRoom]:
            if "Golden sword" in inventory:
                print(f"You defeated the {rooms[currentRoom]['monster']}")
                print("You Win")
                break
            else:
                print(f"You have been slain by the {rooms[currentRoom]['monster']}")
                print("Game Over")
                break


if __name__ == "__main__":
    main()
