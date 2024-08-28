class World:
    def __init__(self, name, towns=None):
        self.name = name
        self.towns = towns or []
        self.starting_room = None

class Town:
    def __init__(self, name, coordinates, dimensions, buildings=None, outdoor_rooms=None):
        self.name = name
        self.coordinates = coordinates  # (x, y)
        self.dimensions = dimensions  # (width, height) in squares
        self.buildings = buildings or []
        self.outdoor_rooms = outdoor_rooms or []

class Building:
    def __init__(self, name, coordinates, dimensions, rooms=None):
        self.name = name
        self.coordinates = coordinates  # (x, y)
        self.dimensions = dimensions  # (width, height) in squares
        self.rooms = rooms or []

class Room:
    def __init__(self, name, description, exits=None, objects=None, characters=None, image=None):
        self.name = name
        self.description = description
        self.coordinates = coordinates  # (x, y) coordinates within its parent
        self.exits = exits or {}  # Dictionary mapping directions to connected rooms
        self.objects = objects or []  # List of Object instances
        self.characters = characters or []  # List of Character instances
        self.image = image  # Optional image filename or path
        self.coordinates = coordinates  # (x, y) coordinates within its parent
        self.dimensions = dimensions or (1, 1)  # Default to a 1x1 room if dimensions are not provided

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
    # Create rooms within a building
    entrance_hall = Room("Entrance Hall", "...", coordinates=(1, 1)) 
    library = Room("Library", "...", coordinates=(2, 1))
    # ... (set exits for rooms)

    # Create a building
    castle = Building("Castle", (5, 3), (5, 4), [entrance_hall, library])

    # Create outdoor rooms within a town
    market_square = Room("Market Square", "...", coordinates=(3, 2))
    town_square = Room("Town Square", "...", coordinates=(7, 5))

    # Create a town
    smallville = Town("Smallville", (10, 15), (10, 8), [castle], [market_square, town_square])

    # Create the world
    my_world = World("My World", [smallville])
    my_world.starting_room = market_square

    return my_world

# Function to load the world from a file or other data source (if needed)
def load_world():
    # Implement loading logic here (if not using create_world)
    pass
