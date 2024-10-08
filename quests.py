class Quest:
    def __init__(self, name, description, objectives, rewards):
        self.name = name
        self.description = description
        self.objectives = objectives  # List of objective descriptions or conditions
        self.rewards = rewards  # List of rewards (items, experience, etc.)
        self.completed = False

def start_quest(game_state, quest):
    """
    Adds a quest to the game state's active quests.

    Args:
        game_state (GameState): The current game state.
        quest (Quest): The quest to start.
    """
    game_state.quest_status[quest.name] = quest
    game_state.output += f"You have started the quest: {quest.name}\n"
    game_state.output += quest.description + "\n"

def update_quest_progress(game_state, event):
    """
    Updates quest progress based on game events.

    Args:
        game_state (GameState): The current game state.
        event (str): A description of the event that occurred.
    """
    for quest_name, quest in game_state.quest_status.items():
        if not quest.completed:
            # Check if the event fulfills any of the quest's objectives
            for objective in quest.objectives:
                if objective in event:
                    quest.objectives.remove(objective)
                    game_state.output += f"Quest objective completed: {objective}\n"
                    if not quest.objectives:  # All objectives completed
                        complete_quest(game_state, quest)
                    break

def complete_quest(game_state, quest):
    """
    Marks a quest as completed and grants rewards.

    Args:
        game_state (GameState): The current game state.
        quest (Quest): The quest to complete.
    """
    quest.completed = True
    game_state.output += f"Quest completed: {quest.name}!\n"
    for reward in quest.rewards:
        # Grant rewards to the player (add items to inventory, increase experience, etc.)
        # ... implementation depends on the type of reward
        game_state.output += f"You received: {reward}\n"
