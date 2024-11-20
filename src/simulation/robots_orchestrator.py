from robot import Robot
from map import Map
from constants import COLORS, MAX_AGENTS
from utils import config_file_data
import json


class RobotsOrchestrator:
    """
    Orchestrates the robots movement for the distributed frontier-based exploration
    """

    def __init__(self, environment: Map) -> None:
        self.environment = environment
        self.robots = self.create_robots()

    def create_robots(self):
        """
        Create robots instances based on configuration file data
        """
        colors = [
            COLORS["YELLOW"],
            COLORS["WHITE"],
            COLORS["BLUE"],
            COLORS["GREEN"],
        ]
        config_data = config_file_data()
        initial_positions = config_data.get("agents_initial_pos")

        robots = []
        if config_data:
            for i in range(len(initial_positions)):

                robot = Robot(
                    self.environment,
                    (
                        int(config_data.get("agents_initial_pos")[i][0]),
                        int(config_data.get("agents_initial_pos")[i][1]),
                    ),
                    colors[i % MAX_AGENTS],
                    COLORS["BLACK"],
                )
                robots.append(robot)
        return robots

    def move_robots(self):
        """
        Orchestrates the robots movement
        """
        self.robots[0].move()  # change this later. For now, only one robot is moving
        for robot in self.robots:
            robot.draw(self.environment.map)
