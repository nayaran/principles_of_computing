"""
Grid class
"""

EMPTY = 0
FULL = 1

class Grid:
    """
    Implementation of 2D grid of cells
    Includes boundary handling
    """

    def __init__(self, grid_height, grid_width):
        """
        Initializes grid to be empty, take height and width of grid as parameters
        Indexed by rows (left to right), then by columns (top to bottom)
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._cells = [[EMPTY for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]

    def __str__(self):
        """
        Return multi-line string represenation for grid
        """
        ans = ""
        for row in range(self._grid_height):
            ans += str(self._cells[row])
            ans += "\n"
        return ans

    def get_grid_height(self):
        """
        Return the height of the grid for use in the GUI
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Return the width of the grid for use in the GUI
        """
        return self._grid_width


    def clear(self):
        """
        Clears grid to be empty
        """
        self._cells = [[EMPTY for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]

    def set_empty(self, row, col):
        """
        Set cell with index (row, col) to be empty
        """
        self._cells[row][col] = EMPTY

    def set_full(self, row, col):
        """
        Set cell with index (row, col) to be full
        """
        self._cells[row][col] = FULL

    def is_empty(self, row, col):
        """
        Checks whether cell with index (row, col) is empty
        """
        return self._cells[row][col] == EMPTY

    def four_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col)
        """
        ans = []
        # NORTH
        if row > 0:
            ans.append((row - 1, col))

        # SOUTH
        if row < self._grid_height - 1:
            ans.append((row + 1, col))

        # WEST
        if col > 0:
            ans.append((row, col - 1))

        # EAST
        if col < self._grid_width - 1:
            ans.append((row, col + 1))

        return ans

    def eight_neighbors(self, row, col):
        """
        Returns horiz/vert neighbors of cell (row, col) as well as
        diagonal neighbors
        """
        ans = []

        # NORTH
        if row > 0:
            ans.append((row - 1, col))

        # SOUTH
        if row < self._grid_height - 1:
            ans.append((row + 1, col))

        # WEST
        if col > 0:
            ans.append((row, col - 1))

        # EAST
        if col < self._grid_width - 1:
            ans.append((row, col + 1))

        # NORTH-WEST
        if (row > 0) and (col > 0):
            ans.append((row - 1, col - 1))

        # NORTH-EAST
        if (row > 0) and (col < self._grid_width - 1):
            ans.append((row - 1, col + 1))

        # SOUTH-WEST
        if (row < self._grid_height - 1) and (col > 0):
            ans.append((row + 1, col - 1))

        # SOUTH-EAST
        if (row < self._grid_height - 1) and (col < self._grid_width - 1):
            ans.append((row + 1, col + 1))
        return ans

    def get_index(self, point, cell_size):
        """
        Takes point in screen coordinates and returns index of
        containing cell
        """
        return (point[1] / cell_size, point[0] / cell_size)

#new_grid = Grid(5, 10)
#print new_grid
