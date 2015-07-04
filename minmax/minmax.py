"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided
import user40_wQSjFTIMLo_0 as poc_tree
import user40_jZkWuMeHIs_1 as stack
import random
# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

class ttt_tree(poc_tree.Tree):
    """
    Custom implementation of Tree suitable for TTT game.
    Value at each node is a TTT board
    """


    def __init__(self, value, children):
        poc_tree.Tree.__init__(self, value, children)
        self._visited = False
        self._score = 0

    def push_child(self, value):
        self._children.insert(0, value)

    def pop_child(self):
        return self._children.pop(len(self._children) - 1)

    def is_visited(self):
        return self._visited

    def visit(self):
        self._visited = True

    def score_the_board(self, winner):
        self._score = SCORES[winner]

    def get_score(self):
        return self._score

    def print_current_board(self):
        return self._value.__str__()


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
        return -1,-1

def dfs(boundary, level):
    print
    print 'inside dfs level - ', level

    # check whose turn it is
    if level % 2 == 0:
        player = provided.PLAYERX
        print "X's turn, maximize level"
    else:
        player = provided.PLAYERO
        print "0's turn, minimize level"

    # pop the curent board from the stack to examine
    board_tree = boundary.pop()

    # create a copy of the current board
    current_board = ttt_tree(board_tree.get_value().clone(), [])

    # check if we are at the leaf or not
    winner = current_board.get_value().check_win()
    print board_tree.print_current_board()

    if winner != None:
        # game finished, score the current board and return

        if winner == 4:
            print 'Game Drawn!!!'
        elif winner == 2:
            print 'X Wins!!!'
        else:
            print 'O Wins!!!'

        print 'score- ', SCORES[winner]
        return SCORES[winner]



    # add children
    # get the actual board
    board = board_tree.get_value()
    children = 0
    moves = []
    score_dict = {}
    while True:
        # get a move for the temp board
        move = get_random_move(board)
        #print move

        # exit if board is full
        if move == (-1, -1):
            break


        moves.append(move)
        # update the temp board
        board.move(move[0], move[1], player)

        # create a new tree object
        child = ttt_tree(current_board.get_value().clone(), [])

        # implement the move
        child.get_value().move(move[0], move[1], player)

        # adds the child to the current board
        current_board.push_child(child)

        #print board.print_current_board()
        # updates the count of the children
        children += 1

        # add the move to the score dict

        score_dict[move] = 0

    print 'added - ', children, ' children...'

    print 'the current board, after updates, looks like this-'
    print moves
    print current_board

    scores = []

    # execute dfs
    for child in current_board._children:
        if not child.is_visited():
            child.visit()

            boundary.push(child)
            scores.insert(0, dfs(boundary, level + 1))



    counter = 0

    # associate moves with scores
    for moves in score_dict.keys():
        score_dict[moves] = scores[counter]
        counter += 1



    best_score = 0

    if player == provided.PLAYERX:
        best_score = max(scores)
        #print 'maximum- ', score

    else:
        best_score = min(scores)
        #current_board.
        #print 'minimum- ', score

    best_move = (-1,-1)


    for move in score_dict:
        if score_dict[move] == best_score:
            best_move = move

    print 'score at level- ', level, 'is ', scores
    print 'moves- ', score_dict
    print 'best move being- ', best_move

    return best_score



def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """

    #root = poc_tree.Tree(board, [])

    return 0, (-1, -1)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)


def test_ttt_tree():


    #my_tree = ttt_tree("a", [ttt_tree("b", [ttt_tree("c", []), ttt_tree("d", [])]),
    #                     ttt_tree("e", [ttt_tree("f", [ttt_tree("g", [])]), ttt_tree("h", []), ttt_tree("i", [])])])
    #print "Tree with nine nodes", my_tree

    #print "The tree has", my_tree.num_nodes(), "nodes,",
    #print my_tree.num_leaves(), "leaves and height",
    #print my_tree.height()

    #import poc_draw_tree
    #poc_draw_tree.TreeDisplay(my_tree)

    #my_tree.push_child(ttt_tree("x", []))

    #my_tree.push_child(ttt_tree("y", []))
    #my_tree.push_child(ttt_tree("z", []))

    #poc_draw_tree.TreeDisplay(my_tree)

    #my_tree.pop_child()
    #my_tree.pop_child()

    dim = 3
    board1 = provided.TTTBoard(dim, False)
    board1.move(1, 1, provided.PLAYERX)

    board2 = provided.TTTBoard(dim, False)
    board2.move(0, 0, provided.PLAYERO)


    board3 = provided.TTTBoard(dim, False)
    board3.move(2, 0, provided.PLAYERO)


    tree_board1 = ttt_tree(board1, [])
    tree_board2 = ttt_tree(board2, [])
    tree_board3 = ttt_tree(board3, [])

    #print 'board1 - '
    #print tree_board1.print_current_board()

    #print 'board2 - '
    #print tree_board2.print_current_board()

    #print 'board3 - '
    #print tree_board3.print_current_board()
    print

    board3 = ttt_tree(board1, [])
    #print 'main board - '
    #print board3

    # testing dfs

    board4 = ttt_tree(board1, [tree_board3, tree_board2])
    #print 'board4- '
    #print board4

    board3.push_child(tree_board2)
    board3.push_child(tree_board3)

    #print 'board3- '
    #print board3


    #board5 = ttt_tree(board1, [board4])
    #print 'board5- '
    #print board5


    print 'testing dfs traversal.........'

    board6 = provided.TTTBoard(dim, False)
    board6.move(1, 1, provided.PLAYERX)
    #board6.move(2, 2, provided.PLAYERX)
    board6.move(0, 2, provided.PLAYERX)
    board6.move(0, 1, provided.PLAYERO)
    board6.move(1, 2, provided.PLAYERO)
    board6.move(2, 1, provided.PLAYERO)
    board6.move(0, 0, provided.PLAYERO)
    tree_board6 = ttt_tree(board6, [])

    print '----------------------'
    print board6
    print '----------------------'
    boundary = stack.Stack()

    boundary.push(tree_board6)

    dfs(boundary, 0)



    #print
    #print 'testing pushing and popping....'
    #print
    #print 'pushing board2- '
    #board3.push_child(tree_board2)
    #print board3

    #print 'pushing board3- '
    #board3.push_child(tree_board3)
    #print board3
    #print '------------------------'
    #print 'popping a child'
    #board3.pop_child()
    #print board3

    #print
    #print 'testing visiting...'
    #print
    #print 'board3.is_visited()- ', board3.is_visited()
    #print 'visiting board3...'
    #board3.visit()
    #print 'board3.is_visited()- ', board3.is_visited()

    #print
    #print 'testing scoring...'
    #print
    #print 'board score- ', board3.get_score()
    #print 'scoring the board...'
    #board3.score_board()
    #print 'board score- ', board3.get_score()



test_ttt_tree()




