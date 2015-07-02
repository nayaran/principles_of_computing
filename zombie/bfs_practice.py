import grid
import queue
import random



class customGrid(grid.Grid):
      """
      A custom Grid class to set arbitrary values in the grid
      """

      def __init__(self, width, height):
            grid.Grid.__init__(self, width, height)
            self._boundary = queue.Queue()
            self._boundary.enqueue((0, 0))



      def getBoundary(self):
            return self._boundary

      def bfs(self, toSearch):
            print
            print 'bfs at work............'
            found = False
            while len(self.getBoundary()) > 0:

                  print 'boundary- ', self.getBoundary()
                  print 'dequeuing first element'
                  current_index = self.getBoundary().dequeue()
                  print 'current_index- ', current_index
                  current_value = self.getCell(current_index[0], current_index[1])
                  print 'current_value- ', current_value

                  if current_value == toSearch:
                        print 'found!!'
                        found = True
                        break
                  else:
                        print 'not the no. we need'
                        print 'continuing search'


                  neighbors = grid.Grid.four_neighbors(self, current_index[0], current_index[1])
                  print 'neighbors of ', current_index, '- ', neighbors
                  for neighbor in neighbors:
                        current_value =  self.getCell(neighbor[0], neighbor[1])
                        print 'at neighbor- ', neighbor, ' value- ', current_value


                        if not grid.Grid.is_full(self, neighbor[0], neighbor[1]):

                              if grid.Grid.is_empty(self, neighbor[0], neighbor[1]):
                                    grid.Grid.set_full(self, neighbor[0], neighbor[1])

                              self.getBoundary().enqueue(neighbor)

                        else:

                              #if current_value == toSearch:
                        #            print 'found!!'
                        #            found = True
                        #            break



                              print 'not the no. we need'
                              print 'continuing search'
                              #grid.Grid.set_full(self, neighbor[0], neighbor[1])
                              #self.getBoundary().enqueue(neighbor)

                        print self
                        print 'boundary- ', self.getBoundary()

                  #for neighbor in neighbors:

                  #print 'both neighbors searched.....unable to proceed'

            print 'done searching............'
            return found


def test():
      #print '-----------------------bfs-----------------------------'
      new_grid = customGrid(10 , 10)
      #print new_grid

      # set 10 numbers in random places in the grid
      """
      for num in range(6, 10):
            x = random.randrange(0, new_grid.get_grid_height())
            y = random.randrange(0, new_grid.get_grid_width())

            while not new_grid.is_empty(x, y):
                  x = random.randrange(0, new_grid.get_grid_height())
                  y = random.randrange(0, new_grid.get_grid_width())


 #           print 'num- ', num, ' at ', x, y
            new_grid.setCell(num, x, y)
      """
      print
      print 'testing bfs with harcoding 8 at (2,0)................................'

      new_grid.setCell(6, 1, 0)
      new_grid.setCell(8, 0, 1)
      new_grid.setCell(11, 9, 9)
      print
      print new_grid
      toFind = 11
      print 'searching for - ', toFind
      print new_grid.bfs(toFind)

test()
