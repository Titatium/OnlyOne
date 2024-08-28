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

    def update(self):
        """
        Updates the game state based on player actions and events.
        """
        pass  # Implement update logic here

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
        pass  # Implement quest completion check here

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
