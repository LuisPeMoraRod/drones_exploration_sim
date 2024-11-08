from map import Map
from robot import Robot
import constants
import pygame
from robots_orchestrator import RobotsOrchestrator
from utils import config_file_data

if __name__ == "__main__":
    # get configuration data
    config_data = config_file_data()

    # Initialize the environment
    environment = Map(constants.MAP_DIMENSIONS, config_data.get("map_file"))

    # Initalize single robot
    orchestrator = RobotsOrchestrator(environment)

    # Fill the map with black color
    environment.map.fill(constants.COLORS["BLACK"])
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

        # Move robots
        orchestrator.move_robots()

        pygame.display.flip()

        # Set the frame rate
        pygame.time.Clock().tick(30)

    pygame.quit()
