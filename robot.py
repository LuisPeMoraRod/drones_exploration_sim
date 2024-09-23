from constants import ROBOT_DIMENSIONS, COLORS, SPEED
import math
import pygame


class Robot:
    def __init__(
        self,
        surface: pygame.Surface,
        initialPos: tuple,
        color: str = COLORS["BLUE"],
        speed: int = SPEED,
    ) -> None:
        self.dimensions = ROBOT_DIMENSIONS
        self.position = [
            initialPos[0] + self.dimensions[0] // 2,
            initialPos[1] + self.dimensions[1] // 2,
        ]
        self.color = color
        self.direction = 0
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
                self.position[0],
                self.position[1],
                self.dimensions[0],
                self.dimensions[1],
            ),
        )

    def move(self):
        # Get the state of the keys
        keys = pygame.key.get_pressed()

        # Move the square
        if keys[pygame.K_LEFT]:
            self.position[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            self.position[0] += self.speed
        if keys[pygame.K_UP]:
            self.position[1] -= self.speed
        if keys[pygame.K_DOWN]:
            self.position[1] += self.speed
