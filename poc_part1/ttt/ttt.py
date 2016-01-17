"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
#import user40_xwPsYGoWjO_5 as provided
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 6         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.


def get_random_move(board):
    """
    This function takes a current board and returns a random move
    for the player
    """

    # Get the list of empty cells
    empty_cells = board.get_empty_squares()

    # Return a random tuple from the empty cells list

    try:
        return random.choice(empty_cells)
    except IndexError:
        print 'no empty cells present!'
        return -1,-1

def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player
    by making random moves, alternating between players.
    The function should return when the game is over.
    The modified board will contain the state of the game,
    so the function does not return anything.
    In other words, the function should modify the board input.
    """
    winner = None

    while winner == None:
        # Move
        row, col = get_random_move(board)
        board.move(row, col, player)

        # Update state
        winner = board.check_win()

        # Switch turns
        player = provided.switch_player(player)




def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the
    same dimensions as the Tic-Tac-Toe board, a board from a completed
    game, and which player the machine player is.
    The function should score the completed board and update the
    scores grid.
    As the function updates the scores grid directly,
    it does not return anything,
    """

    #print 'inside mc_update_scores'
    #print 'score board before updation - '
    #print_score_board(scores, board)

    #print 'board - '
    #print board
    # Get the dimension
    dim = board.get_dim()

    # Get the winner
    winner = board.check_win()

    # Score the board and update the score board accordingly
    for row in range(dim):
        for col in range(dim):
            if board.square(row, col) == provided.EMPTY or winner == provided.DRAW:
                scores[row][col] += 0
            elif board.square(row, col) == winner:
                scores[row][col] += SCORE_CURRENT
            else:
                scores[row][col] += -SCORE_OTHER
    #print 'score board after updation - '
    #print_score_board(scores, board)

def print_score_board(scores, board):

    """
    Prints the current score board nicely
    """

    dim = board.get_dim()

    rep = ""
    for row in range(dim):
        for col in range(dim):
            rep += str(int(scores[row][col]))
            if col == dim - 1:
                rep += "\n"
            else:
                rep += " | "
        if row != dim - 1:
            rep += "-" * (4 * dim - 3)
            rep += "\n"
    print rep


def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores.
    The function should find all of the empty squares with the
    maximum score and randomly return one of them as a (row, column)
    tuple.
    It is an error to call this function with a board that has
    no empty squares (there is no possible next move),
    so your function may do whatever it wants in that case.
    The case where the board is full will not be tested.
    """
    print 'board - '
    print board
    print 'score_board - '
    print_score_board(scores, board)

    # Get the list of empty cells
    empty_cells = board.get_empty_squares()

    print 'empty cells - ',
    print empty_cells

    choices = dict()

    max_score = 0

    # Get the available choices of empty cells
    # along with their points

    for square in empty_cells:
        #print square,
        #print scores[square[0]][square[1]]
        choices[square] = scores[square[0]][square[1]]

    print 'choices - ',
    print choices

    # Select the one with the maximum points
    try:
        max_score = max(choices.values())

        print 'max_score - ', max_score

        better_choices = [key for key in choices.keys() if choices[key] == max_score]

        print 'possible moves - ',
        print better_choices

        print 'best move would be - ',
        print random.choice(better_choices)

        return random.choice(better_choices)

    except ValueError:
        print 'No empty squares'



def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player
    is, and the number of trials to run.
    The function should use the Monte Carlo simulation described above
    to return a move for the machine player in the form of
    a (row, column) tuple.
    Be sure to use the other functions you have written!
    """
    # Get the dimension
    dim = board.get_dim()

    score_board = [[0 for dummycol in range(dim)]
                           for dummyrow in range(dim)]


    print '---choosing best move - monte carlo simulation----'
    for ntrials in range(trials):
        temp_board = board.clone()
        print
        print 'trial - ', ntrials
        print
        print 'board before trial - ', ntrials
        print temp_board

        # Play a random game
        mc_trial(temp_board, player)

        print 'board after trial - ', ntrials
        print temp_board

        # Update the score
        print 'score before updation - '
        print_score_board(score_board, temp_board)

        mc_update_scores(score_board, temp_board, player)

        print 'score after updation - '
        print_score_board(score_board, temp_board)

    print '---simulation done----'
    return get_best_move(board, score_board)


def test():
    """
    A simple sanity test for the game
    """

    dim = 3
    board = provided.TTTBoard(dim, False)

    print 'new board - '
    print board

    print 'playing one game...... '
    mc_trial(board, provided.PLAYERX)

    print 'final board after the game - '
    print board

    print 'winner - ', provided.STRMAP[board.check_win()]


    score_board = [[0 for dummycol in range(dim)]
                               for dummyrow in range(dim)]

    score_board = [[2, 3, 6],[1, 0, 6],[6, 7, 9]]

    mc_update_scores(score_board, board, provided.PLAYERX)

    print_score_board(score_board, board)

    get_best_move(board, score_board)



#test()
# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
