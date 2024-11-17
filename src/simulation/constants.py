# This file contains the constant values used in the project
# Colors
COLORS: dict = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "GRAY": (128, 128, 128),
}

# Directions
DIRECTIONS: dict = {
    "RIGHT": 0,
    "UP": 1,
    "LEFT": 2,
    "DOWN": 3,
}

# Map dimensions
MAP_DIMENSIONS: tuple = (1280, 640)

# Robot dimensions
ROBOT_DIMENSIONS: tuple = (21, 21)
SPEED: int = 5

# Simulation parameters
RANGE = 100
UNCERTAINTY = (0.5, 0.01)
ANGULAR_SPEED = 4
RAYS_AMOUNT = 50

# Robot initial position
INIT_X = 11
INIT_Y = 11

# Grid cell values
GRID_VALUES: dict = {
    "UNKNOWN": -1,
    "FREE": 0,
    "OBSTACLE": 1,
    "FRONTIER": 2,
    "GOAL": 3,
}

GRID_CELL_DIMENTIONS: tuple = (5, 5)

MAX_AGENTS = 4
