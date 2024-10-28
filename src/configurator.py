import tkinter as tk
from tkinter import filedialog
from constants import CONFIG_W, CONFIG_H


class Configurator:
    """
    This class is responsible for creating the configuration window
    """

    def __init__(self, root):
        self.root = root
        # Set up the main window
        root.title("Configuration")
        root.geometry(f"{CONFIG_W}x{CONFIG_H}")

        # Configure grid layout for responsiveness
        root.grid_columnconfigure(1, weight=1)  # Entry field column expands
        root.grid_rowconfigure(0, weight=1)  # Adjusts to window resizing

        # Label for the file selection
        self.label = tk.Label(root, text="Reference map:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="e")  # Aligns right

        # Entry field to display the selected file path
        self.file_path = tk.Entry(root)
        self.file_path.grid(
            row=0, column=1, padx=10, pady=10, sticky="ew"
        )  # Expands horizontally

        # Browse button
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # Initialize agents variable
        self.agents = 1
        self.agent_rows = []  # List to track dynamically added rows

        # Label for the amount of agents
        self.agents_label = tk.Label(root, text=f"Amount of agents: {self.agents}")
        self.agents_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        # Increment and decrement buttons for agents
        self.decrement_button = tk.Button(root, text="-", command=self.decrement_agents)
        self.decrement_button.grid(row=1, column=1, padx=5, pady=10, sticky="w")

        self.increment_button = tk.Button(root, text="+", command=self.increment_agents)
        self.increment_button.grid(row=1, column=1, padx=55, pady=10, sticky="w")

        # Initial row for agent 1
        self.add_agent_row()

    def browse_file(self):
        # Open file dialog and update the file_path entry with the selected file
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.delete(0, tk.END)
            self.file_path.insert(0, file_path)

    def increment_agents(self):
        # Increment agents up to a maximum of 5 and add a new row
        if self.agents < 5:
            self.agents += 1
            self.update_agents_label()
            self.add_agent_row()

    def decrement_agents(self):
        # Decrement agents if greater than 1 and remove the last row
        if self.agents > 1:
            self.agents -= 1
            self.update_agents_label()
            self.remove_agent_row()

    def add_agent_row(self):
        # Create a new row for the agent's initial position with two integer inputs
        row_index = len(self.agent_rows) + 2  # Start after the agents label and buttons

        # Label for agent position
        position_label = tk.Label(
            self.root, text=f"Initial position of agent {self.agents}:"
        )
        position_label.grid(row=row_index, column=0, padx=10, pady=5, sticky="e")

        # Entry fields for X and Y positions
        x_label = tk.Label(self.root, text="X:")
        x_label.grid(row=row_index, column=1, padx=5, pady=5, sticky="w")
        x_entry = tk.Entry(self.root, width=5)
        x_entry.grid(row=row_index, column=1, padx=20, pady=5, sticky="w")

        y_label = tk.Label(self.root, text="Y:")
        y_label.grid(row=row_index, column=1, padx=55, pady=5, sticky="w")
        y_entry = tk.Entry(self.root, width=5)
        y_entry.grid(row=row_index, column=1, padx=70, pady=5, sticky="w")

        # Append to agent_rows for tracking
        self.agent_rows.append((position_label, x_label, x_entry, y_label, y_entry))

    def remove_agent_row(self):
        # Remove the last added row (label and entry fields)
        if self.agent_rows:
            position_label, x_label, x_entry, y_label, y_entry = self.agent_rows.pop()
            position_label.grid_forget()
            x_label.grid_forget()
            x_entry.grid_forget()
            y_label.grid_forget()
            y_entry.grid_forget()

    def update_agents_label(self):
        # Update the label text with the current number of agents
        self.agents_label.config(text=f"Amount of agents: {self.agents}")
