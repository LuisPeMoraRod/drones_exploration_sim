class Frontier:
    """
    Abstracts the occupancy grid's frontiers used by robot to choose the next exploration point.

    The Frontier class contains the following attributes:
    - id: int
    - cells: tuple[] (list of cells position that compose the frontier)
    - size: int (amount of cells in the frontier)
    - distance: int (euclidean distance from the robot's position to the centroid)
    - centroid: tuple
    - cost: int
    """

    def __init__(self, id: int, cost=0):
        self.id = id
        self.cells = []
        self.size = 0  # amount of cells in the frontier
        self.distance = (
            0  # euclidean distance from the robot's position to the frontier's centroid
        )
        self.cost = cost
