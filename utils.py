import random
import pickle  # For saving/loading game state

def validate_input(player_input):
    """
    Checks if the player's input is valid (non-empty and alphanumeric).

    Args:
        player_input (str): The player's input.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    return player_input.strip() and player_input.isalnum()

def generate_random_number(start, end):
    """
    Generates a random integer within the specified range.

    Args:
        start (int): The lower bound of the range (inclusive).
        end (int): The upper bound of the range (inclusive).

    Returns:
        int: A random integer between start and end.
    """
    return random.randint(start, end)

def save_game(game_state, filename="save_game.dat"):
    """
    Saves the current game state to a file using pickle.

    Args:
        game_state (GameState): The game state object to save.
        filename (str, optional): The name of the file to save to. Defaults to "save_game.dat".
    """
    try:
        with open(filename, "wb") as f:
            pickle.dump(game_state, f)
        print("Game saved successfully!")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game(filename="save_game.dat"):
    """
    Loads a saved game state from a file using pickle.

    Args:
        filename (str, optional): The name of the file to load from. Defaults to "save_game.dat".

    Returns:
        GameState: The loaded game state object, or None if there was an error.
    """
    try:
        with open(filename, "rb") as f:
            game_state = pickle.load(f)
        print("Game loaded successfully!")
        return game_state
    except FileNotFoundError:
        print(f"Error: Save file not found: {filename}")
        return None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None
