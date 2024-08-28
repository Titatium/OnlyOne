import tkinter as tk

class HUD:
    def __init__(self, master, player):
        self.master = master
        self.player = player

        self.frame = tk.Frame(master)
        self.frame.pack()

        # Create labels or other elements to display HUD information
        self.health_label = tk.Label(self.frame, text=f"Health: {self.player.health}")
        self.health_label.pack()
        self.experience_label = tk.Label(self.frame, text=f"Experience: {self.player.experience}")
        self.experience_label.pack()

    def update(self):
        # Update HUD elements with the latest player information
        self.health_label.config(text=f"Health: {self.player.health}")
        self.experience_label.config(text=f"Experience: {self.player.experience}")

class Minimap:
    def __init__(self, master, game_state):
        self.master = master
        self.game_state = game_state

        self.canvas = tk.Canvas(master, width=200, height=200)  # Adjust size as needed
        self.canvas.pack()

    def update(self):
        # Clear the canvas
        self.canvas.delete("all")

        # Get the current context (world, town, building, room)
        current_context = self.game_state.get_current_context()

        # Get the rooms or locations to display based on the context
        locations_to_display = self.game_state.get_locations_for_minimap(current_context)

        # Calculate scale factor and translation based on context and minimap size
        scale_factor, translation = self.calculate_minimap_scaling(current_context, locations_to_display)

        # Draw the map elements (rooms, buildings, etc.) on the canvas
        for location in locations_to_display:
            x, y = location.coordinates  # Assuming each location has coordinates
            x_scaled, y_scaled = x * scale_factor + translation[0], y * scale_factor + translation[1]
            if isinstance(location, Room):
                self.canvas.create_rectangle(x_scaled, y_scaled, x_scaled + scale_factor, y_scaled + scale_factor, fill="gray")  # Example: draw a gray square for each room
            elif isinstance(location, Building):
                self.canvas.create_rectangle(x_scaled, y_scaled, x_scaled + scale_factor * location.dimensions[0], y_scaled + scale_factor * location.dimensions[1], fill="lightblue")  # Example: draw a lightblue rectangle for buildings
            elif isinstance(location, Town):
                self.canvas.create_rectangle(x_scaled, y_scaled, x_scaled + scale_factor * location.dimensions[0], y_scaled + scale_factor * location.dimensions[1], fill="lightgreen")  # Example: draw a lightgreen rectangle for towns

        # Draw the player's location marker
        player_x, player_y = self.game_state.player.coordinates
        player_x_scaled, player_y_scaled = player_x * scale_factor + translation[0], player_y * scale_factor + translation[1]
        self.canvas.create_oval(player_x_scaled - 5, player_y_scaled - 5, player_x_scaled + 5, player_y_scaled + 5, fill="red")  # Example: draw a red circle for the player

    def calculate_minimap_scaling(self, current_context, locations_to_display):
        minimap_width = self.canvas.winfo_width()
        minimap_height = self.canvas.winfo_height()

        # Calculate the maximum dimensions of the locations
        max_x = max(location.coordinates[0] for location in locations_to_display)
        max_y = max(location.coordinates[1] for location in locations_to_display)
        if isinstance(location, Building):
            max_x += location.dimensions[0]
            max_y += location.dimensions[1]
        elif isinstance(location, Town):
            max_x += location.dimensions[0]
            max_y += location.dimensions[1]

        # Determine the scale factor
        if current_context == "world":
            world_width, world_height = self.game_state.world.dimensions
            scale_factor = min(minimap_width / world_width, minimap_height / world_height)
        elif current_context == "town":
            town = self.game_state.current_room.town
            town_width, town_height = town.dimensions
            scale_factor = min(minimap_width / town_width, minimap_height / town_height)
        elif current_context == "building":
            building = self.game_state.current_room.building
            building_width, building_height = building.dimensions
            scale_factor = min(minimap_width / building_width, minimap_height / building_height)
        elif current_context == "room":
            room_width, room_height = self.game_state.current_room.dimensions
            scale_factor = min(minimap_width / room_width, minimap_height / room_height)

        # Calculate translation to center the map (optional)
        translation = (
            (minimap_width - scale_factor * max_x) // 2,
            (minimap_height - scale_factor * max_y) // 2
        )

        return scale_factor, translation

class InventoryDisplay:
    def __init__(self, master, player):
        self.master = master
        self.player = player

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

    def update(self):
        # Clear the listbox
        self.listbox.delete(0, tk.END)

        # Add items from the player's inventory
        for item in self.player.inventory:
            self.listbox.insert(tk.END, item.name)

class DialogueBox:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(master)
        self.frame.pack()

        self.text_label = tk.Label(self.frame, text="")  # Initially empty
        self.text_label.pack()

        self.options_frame = tk.Frame(self.frame)
        self.options_frame.pack()

        self.buttons = []  # List to store option buttons

    def set_text(self, text):
        self.text_label.config(text=text)

    def set_options(self, options):
        # Clear existing buttons
        for button in self.buttons:
            button.destroy()
        self.buttons = []

        # Create new buttons for the given options
        for i, option in options:
            button = tk.Button(self.options_frame, text=option, command=lambda i=i: self.on_option_selected(i))
            button.pack()
            self.buttons.append(button)

    def on_option_selected(self, choice_index):
        # Handle the player's dialogue choice
        # ... (You'll need to pass this information back to your game logic)
        pass
