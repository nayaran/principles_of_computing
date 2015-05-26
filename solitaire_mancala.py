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
        self.configuration = [0]

    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.configuration = configuration
        printS("config - " + str(self.configuration))
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self.configuration[::-1])
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        printS
        printS ("inside get_num_seeds...")
        printS ("house_num - ", house_num)
        printS ("seeds - ", self.configuration[house_num])
        
        return self.configuration[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        printS ("inside is_game_won...")
        
        for i in range(len(self.configuration)-1):
            if self.configuration[i+1] != 0:
                printS (str(self.configuration))
                printS ("game lost!")
                return False
            
        printS ("game won!")
        return True
    
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        printS("")
        printS ("inside is_legal_move...")
        printS ('"house_num - ", house_num')
        
        if house_num == 0 or self.configuration[house_num] != house_num:
            printS ("False")
            return False
    
        printS ("True")
        return True

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        printS("")
        printS ("inside apply_move...")
        printS ('"move chosen - ", house_num')
        
        printS ("before move - ")
        printS ('self.configuration')
        
        self.configuration[house_num] = 0
        
        printS ('self.configuration[house_num]')
        

        for i in range(house_num-1, 0, -1):
            self.configuration[i] = self.configuration[i] + 1
        
        self.configuration[0] = self.configuration[0] + 1
        printS ("after move - ")
        printS ('self.configuration')
            
    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        printS("")
        printS ("inside choose_move...")
        legal_moves = []
        
        for i in range(len(self.configuration)):
            
            if i != 0:
                if self.is_legal_move(i):
                    legal_moves.append(i)
                    
        printS ('"legal_moves - ", legal_moves')
        printS ('"move chosen - ", min(legal_moves)')
        return min(legal_moves)
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        printS("")
        printS ("inside plan_moves...")
        ideal_moves = []
        
        while(not self.is_game_won()):
            current_move = self.choose_move()
            printS("")
            printS ('"current_move - ", current_move')
            self.apply_move(current_move)
            ideal_moves.append(current_move)

        printS ('"ideal moves - ", ideal_moves')
        return ideal_moves

def printS(string):
    enabled = True
    
    if(enabled):
        print string

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    printS ('"Testing init - Computed:", my_game, "Expected: [0]"')
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    
    printS ('"Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])')
    printS ('"Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]')
#    printS "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
#    printS "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
    printS
    printS ("playing the game.....")
    
    my_game.plan_moves()
    my_game.is_game_won()
    
    # add more tests here
    
test_mancala()



    
    

# Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())

