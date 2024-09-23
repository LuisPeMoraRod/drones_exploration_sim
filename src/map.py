import math
import pygame
from constants import COLORS


class Map:
    def __init__(self, MapDimensions: tuple) -> None:
        pygame.init()
        self.pointsCloud = []  # List of points to be displayed on the map
        self.externalMap = pygame.image.load(
            "images/map.png"
        )  # Load the reference map image
        self.map_h, self.map_w = MapDimensions
        self.winName = "Map"
        self.map = None
        self.displayMap()

    def displayMap(self):
        """
        Display reference map image
        """
        pygame.display.set_caption(self.winName)
        self.map = pygame.display.set_mode((self.map_w, self.map_h))
        self.map.blit(
            self.externalMap, (0, 0)
        )  # Display the reference map image on top
        self.infoMap = self.map.copy()

    def polarToCartesian(self, r: float, theta: float, robotPosition: tuple) -> tuple:
        """
        Convert polar coordinates to Cartesian coordinates.
        """
        x = robotPosition[0] + r * math.cos(theta)
        y = robotPosition[1] + -r * math.sin(theta)
        return int(x), int(y)

    def dataStorage(self, data: list) -> None:
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

    def showData(self) -> None:
        """
        Display the data on the map.
        """
        for point in self.pointsCloud:
            self.infoMap.set_at(point, COLORS["RED"])
