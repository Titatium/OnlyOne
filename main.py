main.py
import tkinter as tk
from PIL import Image, ImageTk  # Use Pillow (PIL fork) for image handling

# Import your game logic modules
import world
import player
import game_state
import events
import combat
import quests
import inventory
import dialogue
import gui_elements
import image_loader
import utils  # Optional, for helper functions

class GameApp:

    def load_game_data(self):
    # ...
    self.game_state.console = self.console
    self.game_state.hud = self.hud
    self.game_state.minimap = self.minimap
    self.game_state.inventory_display = self.inventory_display
    # ...
    
    def __init__(self, master):
        self.master = master
        master.title("MUD-Like Game")

        # Initialize game state
        self.game_state = game_state.GameState()

        # Create GUI elements
        self.create_console_area()
        self.create_image_area()
        self.create_minimap()
        self.create_hud()
        self.create_inventory_display()
        self.create_directional_buttons()

        # Load initial game data (world, player, etc.)
        self.load_game_data()

        # Start the game loop
        self.game_loop()

    def create_console_area(self):
        # Create a text widget or similar element to display game output
        self.console = tk.Text(self.master)
        self.console.pack()

    def create_image_area(self):
        # Create a label or canvas to display images
        self.image_label = tk.Label(self.master)
        self.image_label.pack()

    def create_minimap(self):
        # Create a canvas for the minimap
        self.minimap_canvas = tk.Canvas(self.master, width=200, height=200)  # Adjust size as needed
        self.minimap_canvas.pack()

    def create_hud(self):
        # Create labels or other elements to display HUD information
        self.hud_frame = tk.Frame(self.master)
        self.hud_frame.pack()
        self.hud = gui_elements.HUD(self.hud_frame, self.game_state.player)

    def create_inventory_display(self):
        # Create a listbox or similar element to display inventory items
        self.inventory_listbox = tk.Listbox(self.master)
        self.inventory_listbox.pack()
        self.inventory_display = gui_elements.InventoryDisplay(self.master, self.game_state.player)

    def load_game_data(self):
        # Load world data from world.py
        self.game_state.world = world.my_world

        # Create player character
        self.game_state.player = player.Player()

        # Set initial room
        self.game_state.current_room = self.game_state.world.starting_room
        self.game_state.player.coordinates = self.game_state.current_room.coordinates  # Initialize player coordinates

        # Update GUI elements with initial game state
        self.update_gui()
        self.update_minimap()
        self.update_directional_buttons()
        
    def game_loop(self):
        # Handle player input and game events
        self.handle_input()

        # Update game state based on events
        self.game_state.update()

        # Update GUI elements to reflect changes
        self.update_gui()

        # Schedule the next game loop iteration
        self.master.after(100, self.game_loop)  # Adjust delay as needed

    def handle_input(self):
        # Get player input from console or other input elements
        player_input = self.console.get("1.0", tk.END).strip()

        # Process input using events.py
        events.handle_events(player_input, self.game_state)

    def update_gui(self):
        # Update console area with game output
        self.console.insert(tk.END, self.game_state.get_output())

        # Update image area if needed
        if self.game_state.current_room.image:
            image = image_loader.load_image(self.game_state.current_room.image)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def update_minimap(self):
        # Clear the minimap canvas
        self.minimap_canvas.delete("all")

        # Determine the current context (world, town, building, room)
        current_context = self.game_state.get_current_context() 

        # Get the rooms or locations to display based on the context
        locations_to_display = self.game_state.get_locations_for_minimap(current_context)

        # Calculate scale factor and translation based on context and minimap size
        scale_factor, translation = self.calculate_minimap_scaling(current_context)

        if current_context == "room":
            room = self.game_state.current_room
            room_width, room_height = room.dimensions

            # Draw the room grid
            for x in range(room_width):
                for y in range(room_height):
                    x_scaled, y_scaled = x * scale_factor + translation[0], y * scale_factor + translation[1]
                    self.minimap_canvas.create_rectangle(x_scaled, y_scaled, x_scaled + scale_factor, y_scaled + scale_factor, fill="gray") 

        else:
        
        # Draw the map elements (rooms, buildings, etc.) on the canvas
        for location in locations_to_display:
            x, y = location.coordinates  # Assuming each location has coordinates
            x_scaled, y_scaled = x * scale_factor + translation[0], y * scale_factor + translation[1]
            self.minimap_canvas.create_rectangle(x_scaled, y_scaled, x_scaled + scale_factor, y_scaled + scale_factor, fill="gray")  # Example: draw a gray square for each location

        # Draw the player's location marker
        player_x, player_y = self.game_state.player.coordinates
        player_x_scaled, player_y_scaled = player_x * scale_factor + translation[0], player_y * scale_factor + translation[1]
        self.minimap_canvas.create_oval(player_x_scaled - 5, player_y_scaled - 5, player_x_scaled + 5, player_y_scaled + 5, fill="red")  # Example: draw a red circle for the player

        # Update HUD
        self.update_hud()

        # Update inventory display
        self.update_inventory()

    def calculate_minimap_scaling(self, current_context):
        minimap_width = self.minimap_canvas.winfo_width()
        minimap_height = self.minimap_canvas.winfo_height()

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
            (minimap_width - scale_factor * world_width) // 2,
            (minimap_height - scale_factor * world_height) // 2
        )

        return scale_factor, translation

    def update_directional_buttons(self):
        # Enable/disable buttons based on available exits in the current room
        for direction, button in self.direction_buttons.items():
            if direction in self.game_state.current_room.exits and self.game_state.current_room.exits[direction]:
                button.config(state=tk.NORMAL)
            else:
                button.config(state=tk.DISABLED)

    def handle_direction_click(self, direction):
        command = f"move {direction}"
        events.handle_events(command, self.game_state)
    
    def update_hud(self):
        # Update HUD elements with player information
        # ... (Implementation depends on your HUD design)

    def update_inventory(self):
        # Clear the inventory listbox
        self.inventory_listbox.delete(0, tk.END)

        # Add items from player's inventory
        for item in self.game_state.player.inventory:
            self.inventory_listbox.insert(tk.END, item.name)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
