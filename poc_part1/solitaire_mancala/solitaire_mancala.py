"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """

    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.__config = [0]


    def set_board(self, __config):
        """
        Take the list __config of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.__config = list(__config)
        # print "__config - " + str(self.__config)

    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self.__config[::-1])

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        # print
        # print "inside get_num_seeds..."
        # print "house_num - ", house_num
        # print "seeds - ", self.__config[house_num]

        return self.__config[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        # print "inside is_game_won..."

        for index in range(len(self.__config)-1):
            if self.__config[index+1] != 0:
                # print str(self.__config)
                # print "game lost!"
                return False

        # print "game won!"
        return True


    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        # print
        # print "inside is_legal_move..."
        # print "house_num - ", house_num,

        if house_num == 0 or self.__config[house_num] != house_num:
            # print False
            return False

        # print True
        return True


    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        # print
        # print "inside apply_move..."
        # print "move chosen - ", house_num

        # print "before move - "
        # print self.__config

        if not self.is_legal_move(house_num):
            return
        if self.__config[house_num] == 0:
            return

        self.__config[house_num] = 0

        # print self.__config[house_num]

        # print range(house_num, 0, -1)
        for index in range(house_num-1, 0, -1):
            self.__config[index] = self.__config[index] + 1

        self.__config[0] = self.__config[0] + 1
        # print "after move - "
        # print self.__config

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        # print
        # print "inside choose_move..."
        legal_moves = []

        for index in range(len(self.__config)):

            if index != 0:
                if self.is_legal_move(index):
                    legal_moves.append(index)

        # print "legal_moves - ", legal_moves
        # print "move chosen - ", min(legal_moves)
        if legal_moves:
            return min(legal_moves)
        else:
            return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
        After each move, move the seeds in the house closest to the store
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        # print
        # print "inside plan_moves..."

        backup = self.__config

        print "current __config - ", self.__config
        ideal_moves = []

        while(not self.is_game_won()):
            current_move = self.choose_move()
            # print
            # print "current_move - ", current_move
            if not current_move:
                return ideal_moves

            self.apply_move(current_move)
            ideal_moves.append(current_move)

        print "ideal moves - ", ideal_moves

        self.__config = backup
        return ideal_moves


# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """

    my_game = SolitaireMancala()
    # print "Testing init - Computed:", my_game, "Expected: [0]"

    __config1 = [0, 0, 1, 1, 3, 5, 0]
    #__config1 = [0, 0, 0, 0]
    my_game.set_board(__config1)

#    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
#    # print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", __config1[1]
#    # print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", __config1[3]
#    # print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", __config1[5]

    print "playing the game....."
    my_game.plan_moves()
    my_game.is_game_won()

    # add more tests here

#test_mancala()


# Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())


