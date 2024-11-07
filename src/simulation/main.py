from map import Map
from robot import Robot
import constants
import pygame

if __name__ == "__main__":
    # Initialize the environment
    environment = Map(constants.MAP_DIMENSIONS)

    # Initalize single robot
    robot = Robot(
        environment, (300, 300), constants.COLORS["GREEN"], constants.COLORS["BLUE"]
    )

    # Fill the map with black color
    # environment.map.fill(constants.COLORS["BLACK"])
    environment.resultMap = environment.map.copy()

    # Initialize Pygame
    pygame.init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the sensed points
        environment.showSensorData()

        # Display the map with the updated data
        environment.map.blit(environment.resultMap, (0, 0))

        # Move robot on key press
        robot.move()
        robot.draw(environment.map)

        pygame.display.flip()

        # Set the frame rate
        pygame.time.Clock().tick(30)

    pygame.quit()
