"""
Clone of 2048 game.
"""

#import poc_2048_gui
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
        self._grid_height = grid_height
        self._grid_width = grid_width

        # initializes the dict to store the inital tiles
        # for each direction
        self.set_initial_tiles()

        # resets the grid
        self.reset()

    def set_initial_tiles(self):
        """
        For each direction, pre-computes a list of the indices
        for the initial tiles in that direction
        """
        self._initial_tiles_dict = {}

        tiles = []

        # temp dictionary for fetching increment counters
        # for each direction

        temp_offset_dict = {

            UP      : (0, 1),
            DOWN    : (self.get_grid_height() - 1, 1),
            LEFT    : (1, 0),
            RIGHT   : (1, self.get_grid_width() - 1)
        }

        # sets up the initial_tiles_dict for each direction

        for direction in range(1,5):

            # fetches the increment counters from
            # temp_offset_dict dict
            row_increment = temp_offset_dict[direction][0]
            col_increment = temp_offset_dict[direction][1]

            # direction is either UP or DOWN
            if col_increment == 1:
                for col in range(self.get_grid_width()):
                    tiles.append((row_increment, col))


            # direction is either LEFT or RIGHT
            if row_increment == 1:
                for row in range(self.get_grid_height()):
                    tiles.append((row, col_increment))


            self._initial_tiles_dict[direction] = tiles

            tiles = []
        #print 'initial_tiles_dict- '
        #printself._initial_tiles_dict
        #print

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """

        # initialize the grid with all zeroes
        self._grid = [[ 0 for dummy_col in range(self.get_grid_width())]
                         for dummy_row in range(self.get_grid_height())]

        # set two random tiles as 2
        self.new_tile()
        self.new_tile()

    def get_random_tile(self):
        """
        Returns the index of a valid random tile
        """

        x_index = random.randint(0, self.get_grid_height()-1)
        y_index = random.randint(0, self.get_grid_width()-1)

        return [x_index, y_index]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        board = ""
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                board = board + str(self._grid[row][col]) + " "
            board = board + "\n"

        return board

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """

        initial_tiles =self._initial_tiles_dict[direction]

        #print 'direction- ', direction
        #print 'initial_tiles- ', initial_tiles
        #print 'len(initial_tiles)- ', len(initial_tiles)

        # setting up the no of steps to traverse
        if direction == UP or direction == DOWN:
            num_steps = self.get_grid_height()
        else:
            num_steps = self.get_grid_width()


        #print 'num_steps- ', num_steps

        #print
        changed = False
        #print 'changed- ', changed

        for tile_index in range(len(initial_tiles)):

            # form the list with the current initial_tile

            start_cell = initial_tiles[tile_index]

            #print 'start_cell- ', start_cell


            temp_list = []

            x_increment = OFFSETS[direction][0]
            y_increment = OFFSETS[direction][1]

            for step in range(num_steps):
                row = start_cell[0] + step * x_increment
                col = start_cell[1] + step * y_increment

                temp_list.append(self.get_tile(row, col))

            #print 'temp_list- ', temp_list

            # merges the newly formed list

            merged_list = merge(temp_list)
            #print 'merged_list- ', merged_list
            #print


            # replaces the list with the merged list
            for step in range(num_steps):
                row = start_cell[0] + step * x_increment
                col = start_cell[1] + step * y_increment

                self.set_tile(row, col, merged_list[step])


            if(merged_list != temp_list):
                changed = True

        if changed:
            self.new_tile()


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # for setting the tile to be 2 90% of the time and
        # 4 10% of the time

        rand_list = [2 for dummy_count in range(10)]
        rand_list.append(4)

        tile = self.get_random_tile()

        # makes sure we are chosing an empty random tile
        while(self.get_tile(tile[0], tile[1]) != 0):
            tile = self.get_random_tile()

        # set the value of the tile
        self.set_tile(tile[0], tile[1],random.choice(rand_list))

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

    def is_game_won(self):
        """
        Returns if the game is won or not
        by checking if the maximum element is 2048 or not
        """

        # calculate the maximum element
        max_element = 0

        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                if self.get_tile(row, col) > max_element:
                    max_element =  self.get_tile(row, col)

        if max_element == 2048:
            return True
        else:
            return False





def test():
    """
    tests the TwentyFortyEight implementation
    """
    new_game = TwentyFortyEight(4, 5)
    print new_game

    new_game.move(UP)
    print new_game

def play():
    print
    print "2048!"
    print "====="

    raw_input("Press any key to start a new game!")
    print
    print "Enter the board size."
    height, width = raw_input("format : height[space]width- ").split()

    new_game = TwentyFortyEight(int(height), int(width))
    print
    print "Directions-."
    print "You would be asked to enter the direction with 'direction-> ' prompt."
    print "Format would be-"
    print "u for UP"
    print "d for DOWN"
    print "l for LEFT"
    print "r for RIGHT"
    print "Any other key to exit.."

    print
    raw_input("Press any key to start the adrenaline rush!")

    dir = {
            'u' : 1,
            'd' : 2,
            'l' : 3,
            'r' : 4,
    }

    direction = 'u'
    print
    print "board"
    print "------"
    print new_game

    while(True):
        print
        direction = raw_input("direction-> ")

        try:
            new_game.move(dir[direction])
        except KeyError:
            print
            print "Good Bye!"
            break

        print
        print "board"
        print "------"
        print new_game

        if new_game.is_game_won():
            print
            print "WOW! You have won the game! Contratulations!"
            break

    print
    print "Thanks for stopping by. Bye!"



play()

#test()
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
