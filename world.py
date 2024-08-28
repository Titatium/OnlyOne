class World:
    def __init__(self, name, towns=None):
        self.name = name
        self.towns = towns or []
        self.starting_room = None
        self.dimensions = (20, 20)  # Estimated world size (20x20 grid)

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
    def __init__(self, name, description, exits=None, objects=None, characters=None, image=None, coordinates=(0, 0), dimensions=(1, 1)):
        self.name = name
        self.description = description
        self.exits = exits or {}  # Dictionary mapping directions to connected rooms
        self.objects = objects or []  # List of Object instances
        self.characters = characters or []  # List of Character instances
        self.image = image  # Optional image filename or path
        self.coordinates = coordinates  # (x, y) coordinates within its parent
        self.dimensions = dimensions  # (width, height) in squares

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

# Define some basic items
bread = Object("Bread", "A fresh loaf of bread.", portable=True)
map_of_the_region = Object("Map", "A map of the region.", portable=True)
healing_potion = Object("Healing Potion", "A vial of clear liquid that glows faintly.", portable=True, usable=True)
antitoxin = Object("Antitoxin", "A vial containing a pungent liquid that can cure poison.", portable=True, usable=True)
glowing_orb = Object("Glowing Orb", "A small orb that emits a soft light, equivalent to a torch.", portable=True, usable=True)
feather_token = Object("Feather Token", "A small token that can be activated to transform into a large feather that can slow a fall from great heights.", portable=True, usable=True)
mystic_charm = Object("Mystic Charm", "A small charm that offers a +1 bonus to a skill check once before losing its magic.", portable=True, usable=True)
elixir_of_health = Object("Elixir of Health", "A vial containing a liquid that cures any disease afflicting the user.", portable=True, usable=True)
cloak_of_billowing = Object("Cloak of Billowing", "A cloak that dramatically billows at the wearer's command.", portable=True, usable=True)

# Define the characters from WhisperwindStory.txt
merchant = Character("Merchant", "A jolly merchant selling his wares.", health=10, strength=2, defense=1, inventory=[bread, map_of_the_region], dialogue=[
    "Welcome, traveler! Need anything?",
    "I've got some fine goods here.",
    "Have you heard of the rumors about the haunted forest?"
])

# Define rooms in The Gilded Tankard (Inn)
gilded_tankard_common_room = Room(
    name="The Gilded Tankard Common Room",
    description="You enter the warm and inviting common room of The Gilded Tankard. The air is filled with the sounds of laughter and conversation, and a roaring fire crackles in the hearth.  A sturdy wooden bar lines one wall, offering a selection of drinks.  A large round table, known as the 'Adventurers' Table', is reserved for those who seek companionship and a chance to share tales.  A bulletin board is filled with notices and advertisements,  a testament to the town's vibrant activity.",
    exits={"out": market_square}, # Exit back to market square
    objects=[
        Object(name="Bar", description="A sturdy wooden bar with a selection of drinks."),
        Object(name="Bulletin Board", description="A board covered with notices and advertisements.", usable=True),
        Object(name="Adventurers' Table", description="A large round table reserved for adventurers to plan and share stories.", usable=True) 
    ],
    characters=[
        Character(name="Mira Stoutheart", description="The innkeeper, a retired human fighter with a warm smile.", health=20, strength=10, defense=5, dialogue=[
            "Welcome to The Gilded Tankard! Let me know if you need anything.",
            "You look weary. A good meal and a warm bed will set you right.",
            "Whisperwind is a friendly town, but always be wary of strangers."
        ])
    ]
)

gilded_tankard_private_room = Room(
    name="The Gilded Tankard Private Room",
    description="You enter a cozy private room with a comfortable bed, a small desk, and a window overlooking the market square.  The room is furnished with a comfortable bed, a small desk with writing materials, and a window that offers a view of the bustling market square.",
    exits={"out": gilded_tankard_common_room},
    objects=[
        Object(name="Bed", description="A comfortable bed with soft blankets."),
        Object(name="Desk", description="A small desk with writing materials.")
    ]
)

gilded_tankard_kitchen = Room(
    name="The Gilded Tankard Kitchen",
    description="You enter the bustling kitchen of The Gilded Tankard.  The aroma of roasting meats and simmering stews fills the air. A large, wood-fired stove is the heart of the kitchen, where Jorah, the cook, works tirelessly to prepare meals for the inn's guests.  A rack filled with spices and herbs sits near the stove, adding to the warm, inviting atmosphere.",
    exits={"out": gilded_tankard_common_room},
    objects=[
        Object(name="Cooking Stove", description="A large, wood-fired stove used for cooking."),
        Object(name="Spice Rack", description="A rack filled with various spices and herbs.")
    ],
    characters=[
        Character(name="Jorah", description="The cook, a burly man with a talent for making simple food taste extraordinary.", health=15, strength=8, defense=3, dialogue=[
            "What can I get for you, traveler?",
            "I've got a variety of dishes to warm your belly.",
            "I learned some of these recipes while sailing the seas."
        ])
    ]
)

# Define the Rootwhistle Apothecary
rootwhistle_apothecary_shop = Room(
    name="Rootwhistle Apothecary",
    description="The apothecary is a cozy, one-story building with a thatched roof. Shelves line the walls, laden with jars and bottles of assorted sizes. The air is filled with the scent of herbs and flowers.  A cabinet filled with dried herbs and spices is a testament to Lily Rootwhistle's extensive knowledge of herbalism, and a shelf filled with glass vials of potions offer a range of remedies for various ailments.",
    exits={"out": market_square},
    objects=[
        Object(name="Herb Cabinet", description="A cabinet filled with dried herbs and spices.", usable=True),
        Object(name="Potion Shelf", description="A shelf filled with glass vials of potions.", usable=True)
    ],
    characters=[
        Character(name="Lily Rootwhistle", description="The halfling proprietor, known for her extensive knowledge of herbalism and a gentle bedside manner.", health=12, strength=1, defense=3, dialogue=[
            "Welcome to the apothecary! What can I help you with?",
            "I've got a wide selection of remedies for any ailment.",
            "If you're venturing into the Feywood, be sure to stock up on antitoxins."
        ])
    ]
)

# Define the Whisperwind Chapel
whisperwind_chapel_main_hall = Room(
    name="Whisperwind Chapel",
    description="The chapel is a modest stone building with stained glass windows depicting various deities. Inside, it is serene and filled with the gentle light of candles.  An altar dedicated to Eldath, the goddess of peace, stands at the front of the chapel, while pews are arranged for worshippers. The chapel is a testament to the town's spiritual diversity and the importance of faith in its residents.",
    exits={"out": market_square},
    objects=[
        Object(name="Altar", description="An altar dedicated to Eldath, the goddess of peace."),
        Object(name="Donation Box", description="A wooden box for donations to the chapel.", usable=True)
    ],
    characters=[
        Character(name="Priestess Elara Dawnblessed", description="An elven cleric who leads the chapel with grace and compassion.", health=15, strength=2, defense=4, dialogue=[
            "Peace be with you, traveler.",
            "The chapel is a place of solace and healing for all.",
            "May the blessings of Eldath guide you on your journey."
        ])
    ]
)

# Define the Ironhand Smithy
ironhand_smithy_forge = Room(
    name="Ironhand Smithy",
    description="The smithy is a sturdy stone building with a large, open forge.  The rhythmic clang of hammer on an anvil rings out from dawn till dusk. The air is thick with the scent of coal and hot metal, a testament to the hard work of Durnan Ironhand, the master blacksmith.  A large anvil stands in the center of the forge, and the forge itself roars with heat, ready to shape metal into tools, weapons, and armor.",
    exits={"out": market_square},
    objects=[
        Object(name="Anvil", description="A large anvil used for shaping metal."),
        Object(name="Forge", description="A roaring forge used to heat metal.", usable=True)
    ],
    characters=[
        Character(name="Durnan Ironhand", description="The master blacksmith, a dwarf known for his skill and no-nonsense attitude.", health=25, strength=14, defense=7, dialogue=[
            "What can I craft for you, traveler?",
            "I've got tools, weapons, and armor for any adventure.",
            "Don't forget to keep your weapons sharp!"
        ])
    ]
)

# Define the Town Square
town_square = Room(
    name="Town Square",
    description="You stand in the Town Square, the heart of Whisperwind. A large oak tree stands in the center, providing shade from the sun. The square is a gathering place for the townsfolk, a place where they come to socialize, celebrate, and discuss the affairs of their community. ",
    exits={"west": market_square, "east": farm_road},
    objects=[
        Object(name="Oak Tree", description="A large oak tree with thick branches that provide shade.")
    ],
    characters=[
        Character(name="Bryn Lightfoot", description="A halfling bard who entertains guests with songs and tales.", health=8, strength=1, defense=2, dialogue=[
            "Welcome to Whisperwind! Let me tell you a tale.",
            "I've got some new songs about the Feywood Forest.",
            "There are rumors of a lost city hidden in the hills."
        ])
    ]
)

# Define the Farm Road
farm_road = Room(
    name="Farm Road",
    description="You follow a dirt road that leads out of town towards the surrounding farms. You can see fields of wheat and corn stretching as far as the eye can see.  The road is lined with fields of wheat and corn, a testament to the town's agricultural prosperity. ",
    exits={"west": town_square, "south": forest_edge},
    objects=[
        Object(name="Barleybrew Farm", description="A sprawling farm owned by the Barleybrew family.", usable=True),
        Object(name="Thatcher Farm", description="A smaller farm run by the Thatcher family.", usable=True)
    ]
)

# Define the Forest Edge
forest_edge = Room(
    name="Forest Edge",
    description="You stand at the edge of the Feywood Forest. The air is thick with the scent of pine needles and damp earth. The trees tower above you, their branches reaching towards the sky. The forest's edge is a place of both beauty and danger, where the wild creatures of the Feywood meet the gentle bustle of the town. ",
    exits={"north": farm_road},
    objects=[
        Object(name="Ancient Well", description="An ancient well with a moss-covered stone lid.", usable=True)
    ],
    characters=[
        Character(name="Aelar Nightbreeze", description="An elven hunter who often patrols the forest's edge.", health=18, strength=6, defense=4, dialogue=[
            "Greetings, traveler. Are you venturing into the Feywood?",
            "The forest is a place of both beauty and danger.",
            "Be careful, for the creatures of the Feywild are not always friendly."
        ])
    ]
)

# Define the Castle Entrance
castle_entrance = Room(
    name="Castle Entrance",
    description="You stand before the imposing entrance to the castle. The stone walls are weathered, but the castle's grandeur remains evident. A large, wooden gate with iron bars stands as a formidable barrier, guarded by a human sentinel.",
    exits={"south": market_square, "inside": castle_courtyard},
    objects=[
        Object(name="Castle Gate", description="A large, wooden gate with iron bars.")
    ],
    characters=[
        Character(name="Guard Thomas", description="A human guard standing watch at the castle gate.", health=12, strength=4, defense=3, dialogue=[
            "Halt! State your business.",
            "This is the castle of Whisperwind. Only those with a reason to be here are welcome."
        ])
    ]
)

# Define the Castle Courtyard
castle_courtyard = Room(
    name="Castle Courtyard",
    description="You enter a spacious courtyard surrounded by the castle walls. A well manicured garden lies to the west, and a grand staircase leads to the main entrance. The courtyard is a testament to the castle's history and the town's commitment to order and safety. ",
    exits={"out": castle_entrance},
    objects=[
        Object(name="Well", description="A well in the center of the courtyard, its water clear and inviting."),
        Object(name="Garden", description="A beautifully maintained garden with a variety of flowers and plants.", usable=True),
        Object(name="Staircase", description="A grand staircase leading to the castle's main entrance.", usable=True)
    ],
    characters=[
        Character(name="Elden Rootwhistle", description="The halfling mayor, known for his jovial nature and effective leadership.", health=14, strength=2, defense=3, dialogue=[
            "Welcome to Whisperwind, traveler! I'm Elden Rootwhistle, the mayor.",
            "If you need anything, please don't hesitate to ask.",
            "Whisperwind is a peaceful town, but be mindful of the Feywood Forest."
        ])
    ]
)

# Define the Castle Throne Room
castle_throne_room = Room(
    name="Castle Throne Room",
    description="You enter a grand room with a massive throne at the far end. The walls are adorned with tapestries depicting the history of Whisperwind. The throne room is a symbol of authority, where the mayor and council meet to make decisions that affect the town.",
    exits={"out": castle_courtyard},
    objects=[
        Object(name="Throne", description="A massive throne made of polished oak, adorned with carvings of mythical creatures.")
    ]
)

# Define the Castle Barracks
castle_barracks = Room(
    name="Castle Barracks",
    description="You enter a large, spartan room with rows of beds and a training area. The air is thick with the scent of sweat and leather. The barracks are a place for the town guard to rest and train, preparing for any threats that may come. ",
    exits={"out": castle_courtyard},
    objects=[
        Object(name="Training Dummies", description="Training dummies used for combat practice.")
    ]
)

# Create the buildings
gilded_tankard = Building(
    name="The Gilded Tankard",
    coordinates=(3, 2),
    dimensions=(5, 4),
    rooms=[gilded_tankard_common_room, gilded_tankard_private_room, gilded_tankard_kitchen]
)

rootwhistle_apothecary = Building(
    name="Rootwhistle Apothecary",
    coordinates=(2, 4),
    dimensions=(4, 3),
    rooms=[rootwhistle_apothecary_shop]
)

whisperwind_chapel = Building(
    name="Whisperwind Chapel",
    coordinates=(7, 4),
    dimensions=(4, 3),
    rooms=[whisperwind_chapel_main_hall]
)

ironhand_smithy = Building(
    name="Ironhand Smithy",
    coordinates=(5, 1),
    dimensions=(5, 4),
    rooms=[ironhand_smithy_forge]
)

castle = Building(
    name="Castle",
    coordinates=(5, 5),
    dimensions=(6, 6),
    rooms=[castle_entrance, castle_courtyard, castle_throne_room, castle_barracks]
)

# Create Whisperwind
whisperwind = Town(
    name="Whisperwind",
    coordinates=(10, 15),
    dimensions=(10, 8),
    buildings=[gilded_tankard, rootwhistle_apothecary, whisperwind_chapel, ironhand_smithy, castle],
    outdoor_rooms=[market_square, town_square]
)

# Create the World
my_world = World("My World", [whisperwind])
my_world.starting_room = market_square
