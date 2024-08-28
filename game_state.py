import tkinter as tk
from world import Building
from world import Room # Import Room from world.py

class GameState:
    def __init__(self):
        self.player = None  # Will be set to the Player instance
        self.world = None  # Will be set to the World/Map instance
        self.current_room = None  # Will be set to the starting room
        self.turn_counter = 0
        self.quest_status = {}  # Dictionary to track quest progress
        self.combat_target = None  # Character the player is fighting (or None)
        self.active_dialogue = None  # DialogueTree for current conversation (or None)
        self.current_context = "world"  # Initially set to "world"
        self.output = ""
        self.console = None  # Will be set by main.py
        self.hud = None  # Will be set by main.py
        self.minimap = None  # Will be set by main.py
        self.inventory_display = None  # Will be set by main.py
        self.direction_buttons = None  # Will be set by main.py

    def load_game_data(self):
        # Load world data from world.py
        self.world = world.my_world

        # Create player character
        self.player = player.Player()

        # Set initial room
        self.current_room = self.world.starting_room
        self.player.coordinates = self.current_room.coordinates  # Initialize player coordinates

        # Update GUI elements with initial game state
        self.update_gui()
        self.update_minimap()
        self.update_directional_buttons()

    def get_output(self):
        return self.output

    def update_gui(self):
        # Update console area with game output
        self.console.insert(tk.END, self.output)
        self.output = ""

        # Update HUD
        self.hud.update()

        # Update minimap
        self.minimap.update()

        # Update inventory
        self.inventory_display.update()

    def update(self):
        """
        Updates the game state based on player actions and events.
        """
        if self.combat_target:
            victor = combat.handle_combat_round(self.player, self.combat_target)
            if victor:
                if victor == "player":
                    self.output += f"You defeated the {self.combat_target.name}!\n"
                    self.current_room.characters.remove(self.combat_target)
                    # Add any rewards or experience gain here
                else:
                    self.output += f"You were defeated by the {self.combat_target.name}!\n"
                    # Handle player death or game over here
                self.combat_target = None
        self.check_quest_completion()

    def get_current_context(self):
        # Determine the context based on the current_room
        if self.current_room in self.world.starting_room.town.outdoor_rooms:
            return "town"  # Player is in an outdoor room within a town
        elif self.current_room in self.world.starting_room.town.buildings[0].rooms:  # Assuming only one building for now
            return "building"  # Player is inside a building
        elif isinstance(self.current_room.parent, Building):  # Check if the room is inside a building
            return "room"  # Player is inside a room within a building
        else:
            return "world"  # Player is in the open world

    def get_locations_for_minimap(self, context):
        if context == "world":
            return self.world.towns  # Display towns on the minimap
        elif context == "town":
            town = self.world.starting_room.town  # Get the town the player is in
            return town.buildings + town.outdoor_rooms  # Display buildings and outdoor rooms
        elif context == "building":
            building = self.world.starting_room.town.buildings[0]  # Get the building the player is in
            return building.rooms  # Display rooms within the building
        elif context == "room":
            return [self.current_room]  # Only display the current room

    def check_quest_completion(self):
        """
        Checks if any quests have been completed and triggers rewards.
        """
        for quest_name, quest in self.quest_status.items():
            if not quest.completed and not quest.objectives:
                quests.complete_quest(self, quest)

    def handle_combat(self):
        """
        Manages combat interactions between the player and NPCs.
        """
        pass  # Implement combat logic here

    def end_turn(self):
        """
        Advances the turn counter and triggers any turn-based events.
        """
        self.turn_counter += 1
        # Implement turn-based event handling here (e.g., NPC actions)

    def update_directional_buttons(self):
        # Enable/disable buttons based on available exits in the current room
        for direction, button in self.direction_buttons.items():
            if direction in self.current_room.exits and self.current_room.exits[direction]:
                button.config(state=tk.NORMAL)
            else:
                button.config(state=tk.DISABLED)
