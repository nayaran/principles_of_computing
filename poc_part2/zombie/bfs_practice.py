
import queue
import random

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

    def is_full(self, row, col):
        """
        Checks whether cell with index (row, col) is full
        """
        return self._cells[row][col] == FULL


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

    def setCell(self, value, row, col):
        """
        Sets the row, col to value
        """
        self._cells[row][col] = value

    def getCell(self, row, col):
        """
        Returns the value at row, col
        """
        return self._cells[row][col]

class customGrid(Grid):
      """
      A custom Grid class to set arbitrary values in the grid
      """

      def __init__(self, width, height):
            Grid.__init__(self, width, height)
            self._boundary = queue.Queue()
            self._boundary.enqueue((0, 0))



      def getBoundary(self):
            return self._boundary

      def bfs(self, toSearch):
            #print
            #print 'bfs at work............'
            found = False
            print self
            while len(self.getBoundary()) > 0:

                  #ch = raw_input("")
                  #print 'boundary- ', self.getBoundary()
                  #print 'dequeuing first element'
                  current_index = self.getBoundary().dequeue()
                  #print 'current_index- ', current_index
                  current_value = self.getCell(current_index[0], current_index[1])
                  #print 'current_value- ', current_value

                  if current_value == toSearch:
                        #print 'found!!'
                        found = True
                        break
                  #else:
                        #print 'not the no. we need'
                        #print 'continuing search'


                  neighbors = Grid.four_neighbors(self, current_index[0], current_index[1])
                  #print 'neighbors of ', current_index, '- ', neighbors
                  for neighbor in neighbors:
                        current_value =  self.getCell(neighbor[0], neighbor[1])
                        #print 'at neighbor- ', neighbor, ' value- ', current_value


                        if not Grid.is_full(self, neighbor[0], neighbor[1]):

                              #if Grid.is_empty(self, neighbor[0], neighbor[1]):
                              Grid.set_full(self, neighbor[0], neighbor[1])

                              #if neighbor not in self.getBoundary():
                              self.getBoundary().enqueue(neighbor)

                        #else:
                            #print 'not the no. we need'
                            #print 'continuing search'


                        #print self
                        #print 'boundary- ', self.getBoundary()
                        #print '-------------------------------------'


            ##print 'done searching............'
            ##print self
            if found:
                  print 'found!!'
            else:
                  print 'not found!!'
            print
            print self


def test():
      print
      print '-----------------------bfs-----------------------------'
      new_grid = customGrid(10 , 10)
      #print new_grid

      # set 10 numbers in random places in the grid

      for num in range(2, 10):
            x = random.randrange(0, new_grid.get_grid_height())
            y = random.randrange(0, new_grid.get_grid_width())

            while not new_grid.is_empty(x, y):
                  x = random.randrange(0, new_grid.get_grid_height())
                  y = random.randrange(0, new_grid.get_grid_width())


 #           print 'num- ', num, ' at ', x, y
            new_grid.setCell(num, x, y)

      print

      #print 'testing bfs with harcoding 8 at (2,0)................................'

      #new_grid.setCell(6, 1, 0)
      #new_grid.setCell(8, 0, 1)
      #new_grid.setCell(11, 3,4)

     #print new_grid
      toFind = 13
      print 'searching for - ', toFind, ' in the following grid'
      new_grid.bfs(toFind)


test()
