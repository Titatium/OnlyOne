import game_state
import combat
import inventory
import dialogue

def handle_events(player_input, game_state):
    """
    Handles player input and triggers corresponding game events.

    Args:
        player_input (str): The player's command.
        game_state (GameState): The current game state.
    """

    # Normalize input for easier parsing
    player_input = player_input.lower()

    # Movement commands
    if player_input.startswith("move "):
        direction = player_input[5:]
        if direction in game_state.current_room.exits:
            new_room = game_state.current_room.exits[direction]
            if new_room:
                game_state.current_room = new_room
                print(game_state.current_room.description)
            else:
                print("You can't go that way.")
        else:
            print("Invalid direction.")

    # Interaction commands
    elif player_input.startswith("take ") or player_input.startswith("pick up "):
        item_name = player_input.split(" ", 1)[1]
        item = next((obj for obj in game_state.current_room.objects if obj.name.lower() == item_name), None)
        if item and item.portable:
            inventory.add_to_inventory(game_state.player, item)
            game_state.current_room.objects.remove(item)
            print(f"You picked up the {item.name}.")
        else:
            print("You can't take that.")

    elif player_input.startswith("drop "):
        item_name = player_input[5:]
        item = next((obj for obj in game_state.player.inventory if obj.name.lower() == item_name), None)
        if item:
            inventory.remove_from_inventory(game_state.player, item)
            game_state.current_room.objects.append(item)
            print(f"You dropped the {item.name}.")
        else:
            print("You don't have that.")

    elif player_input.startswith("use "):
        item_name = player_input[4:]
        item = next((obj for obj in game_state.player.inventory if obj.name.lower() == item_name), None)
        if item and item.usable:
            if item.use_effect:
                item.use_effect(game_state)  # Execute the item's use effect
            else:
                print(f"You use the {item.name}, but nothing happens.")
        else:
            print("You can't use that.")

    elif player_input.startswith("talk to "):
        character_name = player_input[8:]
        character = next((char for char in game_state.current_room.characters if char.name.lower() == character_name), None)
        if character:
            dialogue_tree = dialogue.initiate_dialogue(character)
            if dialogue_tree:
                game_state.active_dialogue = dialogue_tree
        else:
            print("There's no one here by that name.")

    # Combat commands
    elif player_input.startswith("attack "):
        opponent_name = player_input[7:]
        opponent = next((char for char in game_state.current_room.characters if char.name.lower() == opponent_name), None)
        if opponent:
            game_state.combat_target = opponent
            print(f"You engage in combat with the {opponent.name}!")
        else:
            print("There's no one here to attack.")

    # Dialogue choices during active conversation
    elif game_state.active_dialogue:
        game_state.active_dialogue = dialogue.handle_player_choice(game_state.active_dialogue, player_input)

    # Other commands (look, inventory, etc.)
    elif player_input == "look":
        print(game_state.current_room.description)
        if game_state.current_room.objects:
            print("You see:")
            for obj in game_state.current_room.objects:
                print(f"- {obj.name}")
        if game_state.current_room.characters:
            print("You see:")
            for char in game_state.current_room.characters:
                print(f"- {char.name}")

    elif player_input == "inventory":
        inventory.display_inventory(game_state.player)

    # Handle combat if active
    if game_state.combat_target:
        victor = combat.handle_combat_round(game_state.player, game_state.combat_target)
        if victor:
            if victor == "player":
                print(f"You defeated the {game_state.combat_target.name}!")
                game_state.current_room.characters.remove(game_state.combat_target)
                # Add any rewards or experience gain here
            else:
                print(f"You were defeated by the {game_state.combat_target.name}!")
                # Handle player death or game over here
            game_state.combat_target = None

    # End the turn and trigger any turn-based events
    game_state.end_turn()