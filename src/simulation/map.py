import math
import pygame
from constants import COLORS, GRID_CELL_DIMENTIONS, GRID_VALUES
import numpy as np


class Map:
    def __init__(self, MapDimensions: tuple, mapFile: str) -> None:
        pygame.init()
        self.pointsCloud = []  # List of points to be displayed on the map
        self.mapImage = pygame.image.load(mapFile)  # Load the reference map image
        self.map_w, self.map_h = MapDimensions
        self.map = None
        self.displayMap()

    def displayMap(self):
        """
        Display reference map image
        """
        pygame.display.set_caption("Simulation map")
        self.map = pygame.display.set_mode((self.map_w, self.map_h))
        self.map.blit(self.mapImage, (0, 0))  # Display the reference map image on top
        self.resultMap = self.map.copy()

    def polarToCartesian(self, r: float, theta: float, robotPosition: tuple) -> tuple:
        """
        Convert polar coordinates to Cartesian coordinates.
        """
        x = robotPosition[0] + r * math.cos(theta)
        y = robotPosition[1] + -r * math.sin(theta)
        return int(x), int(y)

    def storeData(self, data: list) -> None:
        """
        Store the data to be displayed on the map.
        """
        if data != False:
            for element in data:
                point = self.polarToCartesian(
                    element[0], element[1], element[2]
                )  # Convert polar to Cartesian
                if point not in self.pointsCloud:
                    self.pointsCloud.append(point)

    def showSensorData(self) -> None:
        """
        Display the sensed data on the map.
        """
        for point in self.pointsCloud:
            self.resultMap.set_at(point, COLORS["RED"])

    def showGrid(self, grid: np.array) -> None:
        """
        Display the grid on the map.

        The grid is a 2D list containing the value of every cell.
        If the value of the cell is UNKNOWN, the color is gray.
        If the value of the cell is FREE, the color is white.
        If the value of the cell is OBSTACLE, the color is black.
        If the value of the cell is FRONTIER, the color is blue.
        If the value of the cell is GOAL, the color is green.

        The position of the grid cell is the top left corner of the cell which is a 5 x 5 square.
        """
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                x = i * GRID_CELL_DIMENTIONS[0]
                y = j * GRID_CELL_DIMENTIONS[1]

                cell = grid[i, j]

                if cell == GRID_VALUES["UNKNOWN"]:
                    color = COLORS["GRAY"]
                elif cell == GRID_VALUES["FREE"]:
                    color = COLORS["WHITE"]
                elif cell == GRID_VALUES["OBSTACLE"]:
                    color = COLORS["BLACK"]
                elif cell == GRID_VALUES["FRONTIER"]:
                    color = COLORS["BLUE"]
                elif cell == GRID_VALUES["GOAL"]:
                    color = COLORS["RED"]
                pygame.draw.rect(
                    self.resultMap,
                    color,
                    (x, y, GRID_CELL_DIMENTIONS[0], GRID_CELL_DIMENTIONS[1]),
                )
