import map
import pygame
import constants
import sensors
import robot

if __name__ == "__main__":
    map = map.Map(constants.MAP_DIMENSIONS)
    originalMap = map.map.copy()
    laser = sensors.LaserSensor(
        constants.RANGE,
        originalMap,
        constants.UNCERTAINTY,
        constants.ANGULAR_SPEED,
        constants.X0,
        constants.Y0,
    )
    map.map.fill(constants.COLORS["BLACK"])
    map.infoMap = map.map.copy()

    # Initalize single robot
    robot = robot.Robot(map.map, map.externalMap, (300, 300))

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
        map.dataStorage(sensorData)
        map.showData()

        map.map.fill(constants.COLORS["BLACK"])

        map.map.blit(map.infoMap, (0, 0))

        robot.move()
        robot.draw(map.map)

        pygame.display.flip()

        # Set the frame rate
        pygame.time.Clock().tick(30)

    pygame.quit()
