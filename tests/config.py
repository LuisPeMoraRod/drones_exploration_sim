import tkinter as tk
from tkinter import filedialog, messagebox

# Function to open file dialog to select map file
def select_map_file():
    filepath = filedialog.askopenfilename(title="Seleccione el archivo del mapa", filetypes=(("DWG Files", "*.dwg"), ("All Files", "*.*")))
    if filepath:
        map_file_entry.delete(0, tk.END)
        map_file_entry.insert(0, filepath)

# Function to capture and print the form data when "Iniciar" button is pressed
def start_simulation():
    try:
        num_agents = int(agents_entry.get())
        positions = []
        for i in range(num_agents):
            x = int(positions_entries[i][0].get())
            y = int(positions_entries[i][1].get())
            positions.append((x, y))
        map_file = map_file_entry.get()
        # Here you can add the logic to initiate the simulation with the form inputs
        print(f"Archivo del mapa: {map_file}")
        print(f"Número de agentes: {num_agents}")
        for idx, pos in enumerate(positions):
            print(f"Posición inicial agente {idx + 1}: x = {pos[0]}, y = {pos[1]}")
        messagebox.showinfo("Información", "Simulación iniciada.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos para las posiciones y el número de agentes.")

# Initialize the main window
root = tk.Tk()
root.title("Configuración de la simulación")

# Map file selection
tk.Label(root, text="Archivo del mapa:").grid(row=0, column=0, sticky="e")
map_file_entry = tk.Entry(root)
map_file_entry.grid(row=0, column=1)
tk.Button(root, text="Seleccionar", command=select_map_file).grid(row=0, column=2)

# Number of agents
tk.Label(root, text="Número de agentes:").grid(row=1, column=0, sticky="e")
agents_entry = tk.Entry(root)
agents_entry.grid(row=1, column=1)
agents_entry.insert(0, "4")  # Default value for number of agents

# Agent positions
positions_entries = []
for i in range(4):
    tk.Label(root, text=f"Posición inicial agente {i + 1}:").grid(row=i + 2, column=0, sticky="e")
    x_entry = tk.Entry(root)
    x_entry.grid(row=i + 2, column=1)
    y_entry = tk.Entry(root)
    y_entry.grid(row=i + 2, column=2)
    positions_entries.append((x_entry, y_entry))

# Default positions for agents (you can modify or remove these)
positions_entries[0][0].insert(0, "10")
positions_entries[0][1].insert(0, "15")
positions_entries[1][0].insert(0, "55")
positions_entries[1][1].insert(0, "20")
positions_entries[2][0].insert(0, "80")
positions_entries[2][1].insert(0, "5")
positions_entries[3][0].insert(0, "20")
positions_entries[3][1].insert(0, "65")

# Start button
start_button = tk.Button(root, text="Iniciar", command=start_simulation)
start_button.grid(row=6, column=1)

# Run the Tkinter event loop
root.mainloop()

