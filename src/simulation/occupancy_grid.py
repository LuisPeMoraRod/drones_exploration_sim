import pygame
from constants import GRID_DIMENTIONS, GRID_VALUES


class OccupancyGrid:
    """
    This class abstracts the occupancy grid used by the robot to navigate the environment.
    It stores the grid that is composed of a linear structure that represents the cell of the map.

    The grid will consist of a 2D array where each cell can have the possible values: unknown, free, obstacle, frontier, goal.

    Also, it will store a list of frontiers.
    The frontiers are the cells adjacent to unknown cells and they represent the potential areas to explore.
    """

    def __init__(self, map: pygame.Surface) -> None:
        self.map = map  # pygame surface that represents the map
        self.grid = self.setGrid(map)

    def setGrid(self, map: pygame.Surface) -> list:
        """
        Create occupancy grid that is going to be used as a graph for the A* algorithm to find the path to the goal of every frontier (centroid)

        The grid will consist of a 2D array where each cell can have the possible values: unknown, free, obstacle, frontier, goal

        The cells will represent a 5x5 pixel area of the map. So the grid will have the same dimensions as the map but divided by 5.
        For example, for a map of 640x1280 pixels, the grid will have 128x256 cells.

        At the beginning, all cells will be unknown. The robot will update the cells as it explores the map.
        """
        grid = []
        for i in range(0, map.get_height(), GRID_DIMENTIONS[1]):
            row = []
            for j in range(0, map.get_width(), GRID_DIMENTIONS[0]):
                row.append(GRID_VALUES["UNKNOWN"])
            grid.append(row)
        return grid
