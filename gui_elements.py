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

        # Add more labels for other HUD elements as needed (e.g., mana, experience, etc.)

    def update(self):
        # Update HUD elements with the latest player information
        self.health_label.config(text=f"Health: {self.player.health}")
        # Update other labels as needed

class Minimap:
    def __init__(self, master, game_state):
        self.master = master
        self.game_state = game_state

        self.canvas = tk.Canvas(master, width=200, height=200)  # Adjust size as needed
        self.canvas.pack()

    def update(self):
        # Clear the canvas
        self.canvas.delete("all")

        # Draw the map and player location
        # ... (Implementation depends on your map data structure and how you want to represent it visually)

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