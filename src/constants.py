# This file contains the constant values used in the project
# Colors
COLORS: dict = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "GRAY": (128, 128, 128),
}

# Directions
DIRECTIONS: dict = {
    "UP": 0,
    "RIGHT": 1,
    "DOWN": 2,
    "LEFT": 3,
}

# Map dimensions
MAP_DIMENSIONS: tuple = (600, 1200)

# Configuration window dimensions
CONFIG_W = 500
CONFIG_H = 300

# Robot dimensions
ROBOT_DIMENSIONS: tuple = (21, 21)
SPEED: int = 5

# Simulation parameters
RANGE = 100
UNCERTAINTY = (0.5, 0.01)
X0 = 0
Y0 = 0
ANGULAR_SPEED = 4

# Robot initial position
INIT_X = 11
INIT_Y = 11
