from map import Map
from robot import Robot
import constants
import pygame
from sensors import LaserSensor

if __name__ == "__main__":
    # Initialize the environment
    environment = Map(constants.MAP_DIMENSIONS)

    originalMap = environment.map.copy()
    laser = LaserSensor(
        constants.RANGE,
        originalMap,
        constants.UNCERTAINTY,
        constants.ANGULAR_SPEED,
        constants.X0,
        constants.Y0,
    )
    # environment.map.fill(constants.COLORS["BLACK"])
    environment.resultMap = environment.map.copy()

    # Initalize single robot
    robot = Robot(environment, (300, 300), constants.COLORS["GREEN"])

    # Initialize Pygame
    pygame.init()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        position = robot.position
        laser.position = position
        sensorData = laser.sense()
        environment.storeData(sensorData)
        environment.showData()

        # environment.map.fill(constants.COLORS["BLACK"])

        environment.map.blit(environment.resultMap, (0, 0))

        robot.move()
        robot.draw(environment.map)

        pygame.display.flip()

        # Set the frame rate
        pygame.time.Clock().tick(30)

    pygame.quit()
