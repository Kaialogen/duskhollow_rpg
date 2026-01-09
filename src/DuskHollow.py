import os


def showInstructions() -> None:
    """
    Prints a main menu and the commands
    """
    print("""
    RPG Game
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

    showInstructions()

    while True:
        status(currentRoom, inventory, rooms)
        move: str = input(">")
        move: list[str] = move.split(" ", 1)

        os.system("clear")

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
