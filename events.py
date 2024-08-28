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
        game_state.player.move(direction, game_state)
        game_state.update_gui()  # Update the GUI after movement
        game_state.update_directional_buttons()  # Update directional buttons

    # Interaction commands
    elif player_input.startswith("take ") or player_input.startswith("pick up "):
        item_name = player_input.split(" ", 1)[1]
        game_state.player.pickup(item_name, game_state)

    elif player_input.startswith("drop "):
        item_name = player_input[5:]
        game_state.player.drop(item_name, game_state)

    elif player_input.startswith("use "):
        item_name = player_input[4:]
        game_state.player.use(item_name, game_state)

    elif player_input.startswith("talk to "):
        character_name = player_input[8:]
        game_state.player.talk(character_name, game_state)

    # Combat commands
    elif player_input.startswith("attack "):
        opponent_name = player_input[7:]
        opponent = next((char for char in game_state.current_room.characters if char.name.lower() == opponent_name), None)
        if opponent:
            game_state.combat_target = opponent
            game_state.output += f"You engage in combat with the {opponent.name}!\n"
        else:
            game_state.output += "There's no one here to attack.\n"

    # Dialogue choices during active conversation
    elif game_state.active_dialogue:
        game_state.active_dialogue = dialogue.handle_player_choice(game_state.active_dialogue, player_input)

    # Other commands (look, inventory, etc.)
    elif player_input == "look":
        game_state.output += game_state.current_room.description + "\n"
        if game_state.current_room.objects:
            game_state.output += "You see:\n"
            for obj in game_state.current_room.objects:
                game_state.output += f"- {obj.name}\n"
        if game_state.current_room.characters:
            game_state.output += "You see:\n"
            for char in game_state.current_room.characters:
                game_state.output += f"- {char.name}\n"

    elif player_input == "inventory":
        inventory.display_inventory(game_state.player)

    # End the turn and trigger any turn-based events
    game_state.end_turn()
