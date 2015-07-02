"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None,
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)

        self._zombie_list = []
        self._human_list = []


    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human


    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use entity_type distances
        """

        height = self.get_grid_height()
        width = self.get_grid_width()

        # keeps track of the visited cells without disturbing the current grid
        visited = poc_grid.Grid(height, width)


        # stores the actualy distances from the nearest entity_type
        distance_field = [[ width*height for dummy_col in range(width)]
                       for dummy_row in range(height)]

        # boundary of the bfs
        boundary = poc_queue.Queue()

        # initializes the boundary with the locations of the enitity_type
        if entity_type == HUMAN:
            for human in self.humans():
                boundary.enqueue(human)
        else:
            for zombie in self.zombies():
                boundary.enqueue(zombie)

        # initializes visited and distance_field
        for cell in boundary:

            visited.set_full(cell[0], cell[1])
            # miniumn distance to the nearest entity should be zero
            # at the location of the entity
            distance_field[cell[0]][cell[1]] = 0


        print 'visited- '
        print visited

        print 'distance_field'
        for distance in distance_field:
            print distance

        # bfs algorithm

        while len(boundary) > 0:
            # examine the first cell in the boundary
            cell = boundary.dequeue()

            # find its neighbors
            neighbors = self.four_neighbors(cell[0], cell[1])

            # for each neighbor, update the visited and
            # distance_field
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1])\
                 and self.is_empty(neighbor[0], neighbor[1]):
                    # enter here only if neighbor has not been visited
                    # and it is not occupied by a obstacle

                    # make the entry in the visited corresponding to this
                    # neighbor
                    visited.set_full(neighbor[0], neighbor[1])

                    # update the distance of this neighbor to be one
                    # greater than the distance of the current cell
                    # under examination - that's how bfs work!
                    distance_field[neighbor[0]][neighbor[1]] =\
                        distance_field[cell[0]][cell[1]] + 1

                    # add the neighbor to the boundary list for progressing
                    # in bfs
                    boundary.enqueue(neighbor)
        print
        print 'after bfs for ', entity_type, '......'
        print
        print 'visited- '
        print visited

        print 'distance_field'
        for distance in distance_field:
            print distance


        return distance_field


    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        updated_human_list = []

        # iterate over each human and update its location
        # so that it is one step farther from the nearest zombie
        for human in self.humans():

            print
            print 'for human- ', human

            row = human[0]
            col = human[1]

            # find the neighbors
            neighbors = self.eight_neighbors(row, col)

            print 'neighbors are- ', neighbors

            # stores the details of each neighbor as the value and its
            # distance from the nearest zombie as the key

            distance_dict = {}

            for neighbor in neighbors:
                    distance = zombie_distance_field[neighbor[0]][neighbor[1]]
                    if distance == self.get_grid_width()*self.get_grid_height():
                        distance = -1
                    distance_dict[distance] = neighbor

            print 'distance_dict- '

            for key in distance_dict:
                print 'neighbor at - ', distance_dict[key], ' is at distance- ',key

            # retrieves the best neighbor
            # i.e. the neighbor which is at maximume distance from the
            # nearest zombie
            best_neighbor = distance_dict[max(distance_dict.keys())]

            print 'best neighbor- ', best_neighbor

            # updates the human list
            updated_human_list.append(best_neighbor)

        # install the movement of the humans
        self._human_list = updated_human_list

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """

        print self
        updated_zombie_list = []

        # iterate over each zombie and update its location
        # so that it is one step farther from the nearest zombie
        for zombie in self.zombies():

            print
            print 'for zombie- ', zombie

            row = zombie[0]
            col = zombie[1]

            # find the neighbors
            neighbors = self.four_neighbors(row, col)

            print 'neighbors are- ', neighbors

            # stores the details of each neighbor as the value and its
            # distance from the nearest human as the key

            distance_dict = {}


            # also find the current_distance
            current_distance = human_distance_field[zombie[0]][zombie[1]]

            print 'current distance from nearest human- ', current_distance
            for neighbor in neighbors:

                    distance = human_distance_field[neighbor[0]][neighbor[1]]
                    if distance == self.get_grid_width()*self.get_grid_height():
                        distance = 100
                    print neighbor, distance
                    distance_dict[distance] = neighbor

            print 'distance_dict- '

            for key in distance_dict:
                print 'neighbor at - ', distance_dict[key], ' is at distance- ',key

            # retrieves the best neighbor
            # i.e. the neighbor which is at minimum distance from the
            # nearest human

            min_distance = min(distance_dict.keys())

            # update the best neighbor only if it actually at a better
            # position than our current position
            if min_distance < current_distance:
                best_neighbor = distance_dict[min_distance]
            else:
                best_neighbor = zombie
            print 'best neighbor- ', best_neighbor

            # updates the zombie list
            updated_zombie_list.append(best_neighbor)

        # install the movement of the zombies
        self._zombie_list = updated_zombie_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

def test():
    """
    implements basic testing for the game
    """

    obstacle_list = [(0,3), (0, 4), (3, 3), (1,1), (2, 2)]
    zombie_list = [(1,2), (2, 4)]
    human_list = [(3,4), (1, 4)]

    game = Apocalypse(5, 5, obstacle_list, zombie_list, human_list)

    #game.add_human(3,3)
    game.add_human(1,2)
    game.add_human(4,4)

    print 'humans......'
    print 'count- ', game.num_humans()
    for human in game.humans():
        print human

    print
    print
    print 'zombies.....'
    print 'count- ', game.num_zombies()
    for zombie in game.zombies():
        print zombie
    print
    print 'grid looks like this.........'
    print game
    print
    print '------compute_distance----------'
    print
    distance_field = game.compute_distance_field(ZOMBIE)
    print
    print 'testing movements.......'
    print
    print 'humans-'
    print
    print 'grid looks like this...'
    print game
    game.move_humans(distance_field)



#test()
#obj = Apocalypse(3, 3, [], [(2, 2)], [(1, 1)])
#dist = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]
#obj.move_humans(dist)
#obj.humans()
#poc_zombie_gui.run_gui(Apocalypse(30, 40))

#obj = Apocalypse(3, 3, [], [(1, 1)], [(1, 1)])
#print obj
#dist = [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
#obj.move_zombies(dist)
#obj.zombies() expected location to be one of [(1, 1)] but received (1, 2)
