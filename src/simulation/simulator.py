from map import Map
import pygame
import constants
import sensors
import robot


class Simulator:
    def __init__(self):
        environment = Map(constants.MAP_DIMENSIONS)
        originalMap = environment.map.copy()
        laser = sensors.LaserSensor(
            constants.RANGE,
            originalMap,
            constants.UNCERTAINTY,
            constants.ANGULAR_SPEED,
            constants.X0,
            constants.Y0,
        )
        environment.map.fill(constants.COLORS["BLACK"])
        environment.resultMap = environment.map.copy()

        # Initalize single robot
        robot = robot.Robot(environment.map, environment.mapImage, (300, 300))

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

            environment.map.fill(constants.COLORS["BLACK"])

            environment.map.blit(environment.resultMap, (0, 0))

            robot.move()
            robot.draw(environment.map)

            pygame.display.flip()

            # Set the frame rate
            pygame.time.Clock().tick(30)

        pygame.quit()
