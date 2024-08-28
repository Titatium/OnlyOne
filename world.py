class Room:
    def __init__(self, name, description, exits=None, objects=None, characters=None, image=None):
        self.name = name
        self.description = description
        self.exits = exits or {}  # Dictionary mapping directions to connected rooms
        self.objects = objects or []  # List of Object instances
        self.characters = characters or []  # List of Character instances
        self.image = image  # Optional image filename or path

class Object:
    def __init__(self, name, description, portable=False, usable=False, use_effect=None):
        self.name = name
        self.description = description
        self.portable = portable
        self.usable = usable
        self.use_effect = use_effect  # Function to execute when used

class Character:
    def __init__(self, name, description, health, strength, defense, inventory=None, dialogue=None):
        self.name = name
        self.description = description
        self.health = health
        self.strength = strength
        self.defense = defense
        self.inventory = inventory or []  # List of Object instances
        self.dialogue = dialogue  # List of dialogue lines or reference to a dialogue tree

    def attack(self, target):
        # Implement attack logic here
        pass

    def defend(self):
        # Implement defense logic here
        pass

    def talk(self):
        # Implement conversation logic here
        pass

# Example of creating a simple world
def create_world():
    # Create rooms
    forest_path = Room("Forest Path", "A winding path through a dense forest.",
                       exits={"north": "Clearing", "south": "Cabin"})
    clearing = Room("Clearing", "A sunlit clearing in the forest.",
                    exits={"south": "Forest Path"})
    cabin = Room("Cabin", "A small, cozy cabin in the woods.",
                 exits={"north": "Forest Path"})

    # Create objects
    sword = Object("Sword", "A sharp, gleaming sword.", portable=True)
    key = Object("Key", "A rusty old key.", portable=True)

    # Create characters
    goblin = Character("Goblin", "A snarling green goblin.", health=20, strength=5, defense=2)

    # Place objects and characters in rooms
    forest_path.objects.append(sword)
    cabin.objects.append(key)
    forest_path.characters.append(goblin)

    # Return the starting room (or a reference to the entire world map)
    return forest_path

# Function to load the world from a file or other data source (if needed)
def load_world():
    # Implement loading logic here (if not using create_world)
    pass