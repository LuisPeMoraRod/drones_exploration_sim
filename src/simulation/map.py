import math
import pygame
from constants import COLORS, GRID_CELL_DIMENTIONS


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

    def showGrid(self, grid: list) -> None:
        """
        Display the grid on the map.

        The grid is a 2D list containing the value of every cell.
        If the value is 0, the cell is unknown and the color is gray.
        If the value is 1, the cell is free and the color is white.
        If the value is 2, the cell is an obstacle and the color is black.
        If the value is 3, the cell is a frontier and the color is green.
        If the value is 4, the cell is the goal and the color is blue.

        The position of the grid cell is the top left corner of the cell which is a 5 x 5 square.
        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                x = j * GRID_CELL_DIMENTIONS[0]
                y = i * GRID_CELL_DIMENTIONS[1]
                cell = grid[i][j]
                if cell == 0:
                    color = COLORS["GRAY"]
                elif cell == 1:
                    color = COLORS["WHITE"]
                elif cell == 2:
                    color = COLORS["BLACK"]
                elif cell == 3:
                    color = COLORS["BLUE"]
                elif cell == 4:
                    color = COLORS["RED"]
                pygame.draw.rect(
                    self.resultMap,
                    color,
                    (x, y, GRID_CELL_DIMENTIONS[0], GRID_CELL_DIMENTIONS[1]),
                )
