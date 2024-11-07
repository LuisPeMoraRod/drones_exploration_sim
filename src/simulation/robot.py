from constants import (
    ROBOT_DIMENSIONS,
    COLORS,
    SPEED,
    DIRECTIONS,
    UNCERTAINTY,
    ANGULAR_SPEED,
    RANGE,
    GRID_VALUES,
    GRID_DIMENTIONS,
)
import pygame
from map import Map
from sensors import LaserSensor


class Robot:
    def __init__(
        self,
        environment: Map,
        initialPos: tuple,
        color: tuple = COLORS["WHITE"],
        colorSensor: tuple = COLORS["BLACK"],
        speed: int = SPEED,
    ) -> None:
        self.environment = environment
        self.mapImage = (
            environment.mapImage
        )  # contains the map image used as reference for collision detection
        self.map = environment.map  # contains the map surface to draw the robot

        self.dimensions = ROBOT_DIMENSIONS

        self.position = [
            initialPos[0] + self.dimensions[0] // 2,
            initialPos[1] + self.dimensions[1] // 2,
        ]

        self.color = color
        self.colorSensor = colorSensor

        self.direction = DIRECTIONS["RIGHT"]
        self.speed = speed

        # Initialize the grid
        self.grid = self.setGrid()

        # Initialize the laser sensor
        self.laser = LaserSensor(
            RANGE,
            self.map.copy(),
            UNCERTAINTY,
            ANGULAR_SPEED,
            self.position[0],
            self.position[1],
            self.grid,
            self.direction,
        )

    def setGrid(self):
        """
        Create grid that is going to be used as a graph for the A* algorithm to find the path to the goal of every frontier (centroid)

        The grid will consist of a 2D array where each cell can have the possible values: unknown, free, obstacle, frontier, goal

        The cells will represent a 5x5 pixel area of the map. So the grid will have the same dimensions as the map but divided by 5.
        For example, for a map of 640x1280 pixels, the grid will have 128x256 cells.

        At the beginning, all cells will be unknown. The robot will update the cells as it explores the map.
        """
        grid = []
        for i in range(0, self.map.get_height(), GRID_DIMENTIONS[1]):
            row = []
            for j in range(0, self.map.get_width(), GRID_DIMENTIONS[0]):
                row.append(GRID_VALUES["UNKNOWN"])
            grid.append(row)
        return grid

    def sense(self):
        """
        Sense the environment using the laser sensor.
        """
        data = self.laser.sense()
        self.grid = self.laser.grid
        self.environment.showGrid(self.grid)
        return data

    def draw(self, surface: pygame.Surface):
        """
        Draw the robot on the map.
        """
        pygame.draw.rect(
            surface,
            self.color,
            (
                self.position[0] - self.dimensions[0] // 2,
                self.position[1] - self.dimensions[1] // 2,
                self.dimensions[0],
                self.dimensions[1],
            ),
        )
        # Draw a small circle to represent the sensor
        pygame.draw.circle(
            surface, self.colorSensor, self.sensorPosition(), self.dimensions[0] // 4
        )

    def sensorPosition(self):
        """
        Get the position of the sensor based on the direction of the robot.
        """
        if self.direction == DIRECTIONS["RIGHT"]:
            return (self.position[0] + self.dimensions[0] // 3, self.position[1])
        elif self.direction == DIRECTIONS["UP"]:
            return (self.position[0], self.position[1] - self.dimensions[1] // 3)
        elif self.direction == DIRECTIONS["LEFT"]:
            return (self.position[0] - self.dimensions[0] // 3, self.position[1])
        elif self.direction == DIRECTIONS["DOWN"]:
            return (self.position[0], self.position[1] + self.dimensions[1] // 3)

    def move(self):
        # Get the state of the keys
        keys = pygame.key.get_pressed()

        # Move the robot based on the key pressed
        if keys[pygame.K_UP]:
            self.direction = self.laser.direction = DIRECTIONS["UP"]
            if not self.isWallCollision():
                self.moveUp()
        if keys[pygame.K_DOWN]:
            self.direction = self.laser.direction = DIRECTIONS["DOWN"]
            if not self.isWallCollision():
                self.moveDown()
        if keys[pygame.K_LEFT]:
            self.direction = self.laser.direction = DIRECTIONS["LEFT"]
            if not self.isWallCollision():
                self.moveLeft()
        if keys[pygame.K_RIGHT]:
            self.direction = self.laser.direction = DIRECTIONS["RIGHT"]
            if not self.isWallCollision():
                self.moveRight()

        # Update the laser sensor position
        self.laser.position = self.position

    def isWallCollision(self) -> bool:
        """
        Check if the robot hits the wall.
        """
        horizontalCheck = self.dimensions[0] // 2 + self.speed
        verticalCheck = self.dimensions[1] // 2 + self.speed

        if self.direction == DIRECTIONS["UP"]:
            if self.position[1] - verticalCheck <= 0:
                return True
            if self.isCollisionTop():
                return True

        elif self.direction == DIRECTIONS["DOWN"]:
            if self.position[1] + verticalCheck >= self.map.get_height():
                return True
            if self.isCollisionBottom():
                return True

        elif self.direction == DIRECTIONS["LEFT"]:
            if self.position[0] - horizontalCheck <= 0:
                return True
            if self.isCollisionLeft():
                return True

        elif self.direction == DIRECTIONS["RIGHT"]:
            if self.position[0] + horizontalCheck >= self.map.get_width():
                return True
            if self.isCollisionRight():
                return True

        return False

    def isCollisionTop(self):
        """
        Check if the robot's top side collides with a wall
        """
        horizontalBorder = self.dimensions[0] // 2
        verticalBorder = self.dimensions[1] // 2 + self.speed
        return (
            (
                self.mapImage.get_at(
                    (self.position[0], self.position[1] - verticalBorder)
                )
                == COLORS["BLACK"]
            )
            or (
                self.mapImage.get_at(
                    (
                        self.position[0] + horizontalBorder,
                        self.position[1] - verticalBorder,
                    )
                )
                == COLORS["BLACK"]
            )
            or (
                self.mapImage.get_at(
                    (
                        self.position[0] - horizontalBorder,
                        self.position[1] - verticalBorder,
                    )
                )
                == COLORS["BLACK"]
            )
        )

    def isCollisionBottom(self):
        """
        Check if the robot's bottom side collides with a wall
        """
        horizontalBorder = self.dimensions[0] // 2
        verticalBorder = self.dimensions[1] // 2 + self.speed
        return (
            (
                self.mapImage.get_at(
                    (self.position[0], self.position[1] + verticalBorder)
                )
                == COLORS["BLACK"]
            )
            or (
                self.mapImage.get_at(
                    (
                        self.position[0] + horizontalBorder,
                        self.position[1] + verticalBorder,
                    )
                )
                == COLORS["BLACK"]
            )
            or (
                self.mapImage.get_at(
                    (
                        self.position[0] - horizontalBorder,
                        self.position[1] + verticalBorder,
                    )
                )
                == COLORS["BLACK"]
            )
        )

    def isCollisionLeft(self):
        """
        Check if the robot's left side collides with a wall
        """
        horizontalBorder = self.dimensions[0] // 2 + self.speed
        verticalBorder = self.dimensions[1] // 2
        return (
            (
                self.mapImage.get_at(
                    (self.position[0] - horizontalBorder, self.position[1])
                )
                == COLORS["BLACK"]
            )
            or (
                self.mapImage.get_at(
                    (
                        self.position[0] - horizontalBorder,
                        self.position[1] + verticalBorder,
                    )
                )
                == COLORS["BLACK"]
            )
            or (
                self.mapImage.get_at(
                    (
                        self.position[0] - horizontalBorder,
                        self.position[1] - verticalBorder,
                    )
                )
                == COLORS["BLACK"]
            )
        )

    def isCollisionRight(self):
        """
        Check if the robot's right side collides with a wall
        """
        horizontalBorder = self.dimensions[0] // 2 + self.speed
        verticalBorder = self.dimensions[1] // 2
        return (
            (
                self.mapImage.get_at(
                    (self.position[0] + horizontalBorder, self.position[1])
                )
                == COLORS["BLACK"]
            )
            or (
                self.mapImage.get_at(
                    (
                        self.position[0] + horizontalBorder,
                        self.position[1] + verticalBorder,
                    )
                )
                == COLORS["BLACK"]
            )
            or (
                self.mapImage.get_at(
                    (
                        self.position[0] + horizontalBorder,
                        self.position[1] - verticalBorder,
                    )
                )
                == COLORS["BLACK"]
            )
        )

    def moveUp(self):
        self.position[1] -= self.speed

    def moveDown(self):
        self.position[1] += self.speed

    def moveLeft(self):
        self.position[0] -= self.speed

    def moveRight(self):
        self.position[0] += self.speed
