from constants import ROBOT_DIMENSIONS, COLORS, SPEED, DIRECTIONS
import math
import pygame


class Robot:
    def __init__(
        self,
        surface: pygame.Surface,
        map: pygame.Surface,
        initialPos: tuple,
        color: str = COLORS["WHITE"],
        speed: int = SPEED,
    ) -> None:
        self.map = map
        self.dimensions = ROBOT_DIMENSIONS
        self.position = [
            initialPos[0] + self.dimensions[0] // 2,
            initialPos[1] + self.dimensions[1] // 2,
        ]
        self.color = color
        self.direction = DIRECTIONS["RIGHT"]
        self.surface = surface
        self.speed = speed

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

    def move(self):
        # Get the state of the keys
        keys = pygame.key.get_pressed()

        # Move the square
        if keys[pygame.K_UP]:
            self.direction = DIRECTIONS["UP"]
            if not self.isWall():
                self.moveUp()
        if keys[pygame.K_DOWN]:
            self.direction = DIRECTIONS["DOWN"]
            if not self.isWall():
                self.moveDown()
        if keys[pygame.K_LEFT]:
            self.direction = DIRECTIONS["LEFT"]
            if not self.isWall():
                self.moveLeft()
        if keys[pygame.K_RIGHT]:
            self.direction = DIRECTIONS["RIGHT"]
            if not self.isWall():
                self.moveRight()

    def isWall(self) -> bool:
        """
        Check if the robot hits the wall.
        """
        horizontalCheck = self.dimensions[0] // 2 + self.speed
        verticalCheck = self.dimensions[1] // 2 + self.speed

        if self.direction == DIRECTIONS["UP"]:
            if self.position[1] - verticalCheck <= 0:
                return True
            if (
                self.map.get_at((self.position[0], self.position[1] - verticalCheck))
                == COLORS["BLACK"]
            ):
                return True
        elif self.direction == DIRECTIONS["DOWN"]:
            if self.position[1] + verticalCheck >= self.surface.get_height():
                return True
            if (
                self.map.get_at((self.position[0], self.position[1] + verticalCheck))
                == COLORS["BLACK"]
            ):
                return True
        elif self.direction == DIRECTIONS["LEFT"]:
            if self.position[0] - horizontalCheck <= 0:
                return True
            if (
                self.map.get_at((self.position[0] - horizontalCheck, self.position[1]))
                == COLORS["BLACK"]
            ):
                return True
        elif self.direction == DIRECTIONS["RIGHT"]:
            if self.position[0] + horizontalCheck >= self.surface.get_width():
                return True
            if (
                self.map.get_at((self.position[0] + horizontalCheck, self.position[1]))
                == COLORS["BLACK"]
            ):
                return True

        return False

    def moveUp(self):
        self.position[1] -= self.speed

    def moveDown(self):
        self.position[1] += self.speed

    def moveLeft(self):
        self.position[0] -= self.speed

    def moveRight(self):
        self.position[0] += self.speed
