import pygame
import math
import numpy as np
from constants import COLORS


class LaserSensor:
    def __init__(
        self,
        range: int,
        map: pygame.Surface,
        uncertainty: tuple,
        speed: int,
        x: int,
        y: int,
    ) -> None:
        self.range = range
        self.speed = speed  # rounds per second
        self.sigma = np.array([uncertainty[0], uncertainty[1]])
        self.position = (x, y)  # initial position
        self.w, self.h = pygame.display.get_surface().get_size()
        self.obstacles = []  # sensed obstacles
        self.map = map

    def sense(self):
        """
        Simulate the laser sensor by casting rays in all directions and detecting obstacles.
        The sensor returns the distance and angle of the detected obstacles relative to the robot position.
        """
        data = []
        x1, y1 = self.position[0], self.position[1]  # current position of the robot
        for angle in np.linspace(
            0, 2 * math.pi, 60, False
        ):  # 60 rays distributed over 360 degrees
            # calculate the end point of the ray
            x2 = x1 + self.range * math.cos(angle)
            y2 = y1 - self.range * math.sin(angle)

            # simulates laser beam
            for i in range(0, 100):
                # interpolate between the start and end points of the ray
                u = i / 100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if (
                    0 < x < self.w and 0 < y < self.h
                ):  # check if the point is within the map
                    color = self.map.get_at((x, y))
                    if color == COLORS["BLACK"]:
                        distance = self.euclideanDistance((x, y))
                        output = self.addNoise(distance, angle, self.sigma)
                        output.append(self.position)
                        data.append(output)
                        break
        if len(data) > 0:
            return data
        return False

    def euclideanDistance(self, obstaclePosition: tuple) -> float:
        """
        Calculate the Euclidean distance between the robot and the obstacle.
        """
        px = (obstaclePosition[0] - self.position[0]) ** 2
        py = (obstaclePosition[1] - self.position[1]) ** 2
        return math.sqrt(px + py)

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
