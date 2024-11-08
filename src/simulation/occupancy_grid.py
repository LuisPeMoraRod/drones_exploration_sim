import pygame
from constants import GRID_CELL_DIMENTIONS, GRID_VALUES
from collections import deque
from map import Map


class OccupancyGrid:
    """
    This class abstracts the occupancy grid used by the robot to navigate the environment.
    It stores the grid that is composed of a linear structure that represents the cell of the map.

    The grid will consist of a 2D array where each cell can have the possible values: unknown, free, obstacle, frontier, goal.

    Also, it will store a list of frontiers.
    The frontiers are the cells adjacent to unknown cells and they represent the potential areas to explore.
    """

    def __init__(self, map: pygame.Surface, environment: Map) -> None:
        self.map = map  # pygame surface that represents the map
        self.grid = self.initGrid(map)
        self.frontiers = []
        self.environment = environment

    def setGrid(self, grid: list) -> None:
        """
        Set the grid of the occupancy grid
        """
        self.grid = grid

    def getGrid(self) -> list:
        """
        Get the grid of the occupancy grid
        """
        return self.grid

    def initGrid(self, map: pygame.Surface) -> list:
        """
        Create occupancy grid that is going to be used as a graph for the A* algorithm to find the path to the goal of every frontier (centroid)

        The grid will consist of a 2D array where each cell can have the possible values: unknown, free, obstacle, frontier, goal

        The cells will represent a 5x5 pixel area of the map. So the grid will have the same dimensions as the map but divided by 5.
        For example, for a map of 640x1280 pixels, the grid will have 128x256 cells.

        At the beginning, all cells will be unknown. The robot will update the cells as it explores the map.
        """
        grid = []
        for i in range(0, map.get_height(), GRID_CELL_DIMENTIONS[1]):
            row = []
            for j in range(0, map.get_width(), GRID_CELL_DIMENTIONS[0]):
                row.append(GRID_VALUES["UNKNOWN"])
            grid.append(row)
        return grid

    def breadthFirstSearch(self, start: list) -> None:
        """
        Performs a BFS to explore the ocuppancy grid and find the frontiers
        """
        # adapt robot position to grid position
        startGrid = (
            start[0] // GRID_CELL_DIMENTIONS[0],
            start[1] // GRID_CELL_DIMENTIONS[1],
        )

        # add current position to flood fill and set as reached
        flood_fill = deque()
        flood_fill.append(startGrid)
        reached = set()
        reached.add(startGrid)

        while len(flood_fill) > 0:
            current = flood_fill.popleft()  # get the first element of the queue
            if self.isFrontier(current):  # handle frontier cell
                self.grid[current[1]][current[0]] = GRID_VALUES["FRONTIER"]
            for neighbor in self.getNeighbors(current):
                if neighbor not in reached:
                    if (
                        self.grid[neighbor[1]][neighbor[0]] == GRID_VALUES["FREE"]
                    ):  # only add free cells to the queue
                        reached.add(neighbor)
                        flood_fill.append(neighbor)

    def getNeighbors(self, cell: tuple) -> list:
        """
        Get the neighbors of a cell in the grid
        """
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                x = cell[0] + i
                y = cell[1] + j
                if x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(self.grid):
                    neighbors.append((x, y))
        return neighbors

    def isFrontier(self, cell: tuple) -> bool:
        """
        Check if a cell is a frontier
        """
        for neighbor in self.getNeighbors(cell):
            if self.grid[neighbor[1]][neighbor[0]] == GRID_VALUES["UNKNOWN"]:
                return True
        return False
