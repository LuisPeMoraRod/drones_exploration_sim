import pygame
from math import pi, cos, sin, sqrt
import numpy as np
from constants import COLORS, DIRECTIONS, GRID_VALUES


class LaserSensor:
    def __init__(
        self,
        range: int,
        map: pygame.Surface,
        uncertainty: tuple,
        speed: int,
        x: int,
        y: int,
        grid: list,
        direction: int = DIRECTIONS["RIGHT"],
    ) -> None:
        self.range = range
        self.speed = speed  # rounds per second
        self.sigma = np.array([uncertainty[0], uncertainty[1]])
        self.position = (x, y)  # initial position
        self.w, self.h = pygame.display.get_surface().get_size()
        self.obstacles = []  # sensed obstacles
        self.map = map
        self.direction = direction
        self.grid = grid

    def sense(self):
        """
        Simulate the laser sensor by casting rays in all directions and detecting obstacles.
        The sensor returns the distance and angle of the detected obstacles relative to the robot position.
        Also, it updates the grid with the cells that are detected as obstacles, and the cells that are free.
        """
        data = []
        x1, y1 = self.position[0], self.position[1]  # current position of the robot

        phi_start = (
            (pi / 2 * self.direction) - pi / 4 + 2 * pi
        )  # stating angle based on direction

        phi_end = (
            phi_start + pi / 2
        )  # ending angle is 90 degrees from the starting angle

        for angle in np.linspace(
            phi_start, phi_end, 15, False
        ):  # 15 rays distributed over 90 degrees
            # calculate the end point of the ray
            x2 = x1 + self.range * cos(angle)
            y2 = y1 - self.range * sin(angle)

            # simulates laser beam
            for i in range(0, self.range):
                # interpolate between the start and end points of the ray
                u = i / self.range
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if (
                    0 < x < self.w and 0 < y < self.h
                ):  # check if the point is within the map
                    color = self.map.get_at((x, y))
                    if color != COLORS["WHITE"]:
                        distance = self.euclideanDistance((x, y))
                        output = self.addNoise(distance, angle, self.sigma)
                        output.append(self.position)
                        data.append(output)
                        self.updateCell(x, y, GRID_VALUES["OBSTACLE"])
                        break
                    else:
                        self.updateCell(x, y, GRID_VALUES["FREE"])
        if len(data) > 0:
            return data
        return False

    def updateCell(self, x: int, y: int, value: int) -> None:
        """
        Update the value of the cell in the grid.
        """
        i = y // 5
        j = x // 5
        self.grid[i][j] = value

    def euclideanDistance(self, obstaclePosition: tuple) -> float:
        """
        Calculate the Euclidean distance between the robot and the obstacle.
        """
        px = (obstaclePosition[0] - self.position[0]) ** 2
        py = (obstaclePosition[1] - self.position[1]) ** 2
        return sqrt(px + py)

    def addNoise(self, distance: float, angle: float, sigma: np.array) -> list:
        """
        Add noise to the measurement by taking a random value in the vicinity of the actual measurement.
        """
        mean = np.array([distance, angle])
        covariance = np.diag(sigma**2)
        distance, angle = np.random.multivariate_normal(mean, covariance)
        distance = max(distance, 0)
        angle = max(angle, 0)
        return [distance, angle]
