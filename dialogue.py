class DialogueNode:
    def __init__(self, text, options=None):
        self.text = text
        self.options = options or []  # List of tuples: (option_text, next_node)

class DialogueTree:
    def __init__(self, root_node):
        self.current_node = root_node

    def get_current_text(self):
        return self.current_node.text

    def get_options(self):
        return [(i + 1, option_text) for i, (option_text, _) in enumerate(self.current_node.options)]

    def make_choice(self, choice_index):
        if 0 <= choice_index < len(self.current_node.options):
            _, next_node = self.current_node.options[choice_index]
            self.current_node = next_node
            return True  # Choice was valid
        else:
            return False  # Invalid choice

# Example dialogue tree
def create_example_dialogue():
    node3 = DialogueNode("Goodbye!")
    node2b = DialogueNode("Interesting...", options=[("Tell me more", node3)])
    node2a = DialogueNode("That's great!", options=[("Thanks!", node3)])
    node1 = DialogueNode("Hello there! How are you?",
                        options=[("I'm doing well", node2a), ("Not so good", node2b)])
    return DialogueTree(node1)

def initiate_dialogue(character):
    """Starts a conversation with the given character."""
    if character.dialogue:
        dialogue_tree = character.dialogue
        print(dialogue_tree.get_current_text())
        options = dialogue_tree.get_options()
        for i, option in options:
            print(f"{i}. {option}")
        return dialogue_tree
    else:
        print(f"{character.name} has nothing to say.")
        return None

def handle_player_choice(dialogue_tree, choice):
    """Processes the player's dialogue choice."""
    try:
        choice_index = int(choice) - 1
        if dialogue_tree.make_choice(choice_index):
            print(dialogue_tree.get_current_text())
            options = dialogue_tree.get_options()
            if options:
                for i, option in options:
                    print(f"{i}. {option}")
            else:
                return None  # Dialogue ended
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    return dialogue_tree