"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # creates a copy of the line

    row = list(line)
    result = [0] * len(line)

    # result line
    dest_index = 0

    # flag to make sure that we merge a tile only once
    can_merge = True


    # iterate over the given row and
    # if found non_zero value,
    # either merge it with the previous
    # value in the result or put it as it is

    for source_index in range(len(row)):

        if row[source_index]:

            # if non_zero value found
            if result[dest_index-1] == row[source_index] and can_merge:
                # merge can be done
                # hence merge
                result[dest_index-1] *= 2

                # disable merging for the merged tile
                can_merge = False

            else:

                # no merging can be done
                # hence copy the value as it is
                result[dest_index] = row[source_index]
                dest_index += 1

                # enable merging
                can_merge = True

    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Initializes the game.
        Sets the height and width of the grid.
        """
        self.GRID_HEIGHT = grid_height
        self.GRID_WIDTH = grid_width

        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """

        # initialize the grid with all zeroes
        self.grid = [[ 0 for col in range(self.GRID_WIDTH)]
                         for row in range(self.GRID_HEIGHT)]

        # set two random tiles as 2
        self.new_tile()
        self.new_tile()

    def getRandomTile(self):
        """
        Returns the index of a valid random tile
        """

        x = random.randint(0, self.GRID_HEIGHT-1)
        y = random.randint(0, self.GRID_WIDTH-1)

        return [x, y]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        board = ""
        for row in range(self.GRID_HEIGHT):
            for col in range(self.GRID_WIDTH):
                board = board + str(self.grid[row][col]) + " "
            board = board + "\n"

        return board


    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.GRID_HEIGHT

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.GRID_WIDTH

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # for setting the tile to be 2 90% of the time and
        # 4 10% of the time

        rand_list = [2 for count in range(10)]
        rand_list.append(4)

        tile = self.getRandomTile()

        # makes sure we are chosing an empty random tile
        while(self.get_tile(tile[0], tile[1]) != 0):
            tile = self.getRandomTile()

        # set the value of the tile
        self.set_tile(tile[0], tile[1],random.choice(rand_list))



    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]


def test():

    new_game = TwentyFortyEight(4, 4)
    print new_game


test()
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
