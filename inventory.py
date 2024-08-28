def add_to_inventory(player, item):
    """
    Adds an item to the player's inventory.

    Args:
        player (Player): The player object.
        item (Object): The item to add.
    """
    player.inventory.append(item)
    print(f"You added {item.name} to your inventory.")

def remove_from_inventory(player, item):
    """
    Removes an item from the player's inventory.

    Args:
        player (Player): The player object.
        item (Object): The item to remove.
    """
    if item in player.inventory:
        player.inventory.remove(item)
        print(f"You removed {item.name} from your inventory.")
    else:
        print(f"You don't have {item.name} in your inventory.")

def display_inventory(player):
    """
    Displays the contents of the player's inventory.

    Args:
        player (Player): The player object.
    """
    if player.inventory:
        print("Your inventory:")
        for item in player.inventory:
            print(f"- {item.name}: {item.description}")
    else:
        print("Your inventory is empty.")
