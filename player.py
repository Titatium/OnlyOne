from world import Character

class Player(Character):
    def __init__(self, name="Player", description="You are an adventurer, ready to explore the world.", health=10, strength=2, defense=1, inventory=None, dialogue=None, coordinates=(0, 0)):
        super().__init__(name, description, health, strength, defense, inventory, dialogue)
        self.experience = 0
        self.level = 1
        self.skills = {}  # Dictionary to store player skills (e.g., "sword fighting": 5)
        self.coordinates = coordinates  # Initialize player coordinates

    def move(self, direction, game_state):
        """
        Moves the player in the specified direction.

        Args:
            direction (str): The direction the player wants to move (e.g., "north", "south").
            game_state (GameState): The current game state.
        """
        if direction in game_state.current_room.exits:
            new_room = game_state.current_room.exits[direction]
            if new_room:
                game_state.current_room = new_room
                game_state.player.coordinates = game_state.current_room.coordinates
                print(game_state.current_room.description)
            else:
                print("You can't go that way.")
        else:
            print("Invalid direction.")

    def pickup(self, item_name, game_state):
        """
        Picks up an item from the current room and adds it to the player's inventory.

        Args:
            item_name (str): The name of the item to pick up.
            game_state (GameState): The current game state.
        """
        item = next((obj for obj in game_state.current_room.objects if obj.name.lower() == item_name), None)
        if item and item.portable:
            inventory.add_to_inventory(self, item)
            game_state.current_room.objects.remove(item)
            print(f"You picked up the {item.name}.")
        else:
            print("You can't take that.")

    def drop(self, item_name, game_state):
        """
        Drops an item from the player's inventory into the current room.

        Args:
            item_name (str): The name of the item to drop.
            game_state (GameState): The current game state.
        """
        item = next((obj for obj in self.inventory if obj.name.lower() == item_name), None)
        if item:
            inventory.remove_from_inventory(self, item)
            game_state.current_room.objects.append(item)
            print(f"You dropped the {item.name}.")
        else:
            print("You don't have that.")

    def use(self, item_name, game_state):
        """
        Uses an item from the player's inventory.

        Args:
            item_name (str): The name of the item to use.
            game_state (GameState): The current game state.
        """
        item = next((obj for obj in self.inventory if obj.name.lower() == item_name), None)
        if item and item.usable:
            if item.use_effect:
                item.use_effect(game_state)
            else:
                print(f"You use the {item.name}, but nothing happens.")
        else:
            print("You can't use that.")

    def talk(self, character_name, game_state):
        """
        Initiates a conversation with a character in the current room.

        Args:
            character_name (str): The name of the character to talk to.
            game_state (GameState): The current game state.
        """
        character = next((char for char in game_state.current_room.characters if char.name.lower() == character_name), None)
        if character:
            dialogue_tree = dialogue.initiate_dialogue(character)
            if dialogue_tree:
                game_state.active_dialogue = dialogue_tree
        else:
            print("There's no one here by that name.")

    # Add other player-specific methods here (e.g., attack, defend, etc.)
