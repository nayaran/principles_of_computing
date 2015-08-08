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
        self._parent_move = (-1, -1)

    def push_child(self, value):
        self._children.insert(0, value)

    def pop_child(self):
        return self._children.pop(len(self._children) - 1)

    def is_visited(self):
        return self._visited

    def visit(self):
        self._visited = True

    def set_score(self, score):
        self._score = score

    def get_score(self):
        return self._score

    def set_parent_move(self, move):
        self._parent_move = move

    def get_parent_move(self):
        return self._parent_move

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

def dfs(boundary, move, level, player):
    print
    print '------------------------------'
    print 'inside dfs level - ', level
    print '------------------------------'

    # switch for determining whether to
    # maximize or minimize
    switch = player == provided.PLAYERX

    # check whose turn it is
    if level % 2 == 0:
        if switch:
            player = provided.PLAYERX
            print "X's turn, maximize level"
        else:
            player = provided.PLAYERO
            print "0's turn, minimize level"
    else:
        if switch:
            player = provided.PLAYERO
            print "0's turn, minimize level"
        else:
            player = provided.PLAYERX
            print "X's turn, maximize level"



    # pop the curent board from the stack to examine
    board_tree = boundary.pop()

    # create a copy of the current board
    current_board = ttt_tree(board_tree.get_value().clone(), [])
    parent_move = move

    # check if we are at the leaf or not
    winner = current_board.get_value().check_win()

    print board_tree.print_current_board()
    print 'board-move was- ', parent_move

    score_dict2 = {}

    if winner != None:
        # game finished, score the current board and return

        if winner == 4:
            print 'Game Drawn!!!'
        elif winner == 2:
            print 'X Wins!!!'
        else:
            print 'O Wins!!!'

        score_dict2[move] = SCORES[winner]
        #print 'score- ', SCORES[winner]
        #return SCORES[winner]
        #return move, SCORES[winner]

    else:
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

            # associates the move with the board
            child.set_parent_move(move)

            # adds the child to the current board
            current_board.push_child(child)

            #print board.print_current_board()
            # updates the count of the children
            children += 1

            # add the move to the score dict

            #score_dict[move] = 0


        print 'added- ', children, ' children...'
        print 'moves- ', moves
        print 'children added- '
        print current_board

        scores = []
        score_dict2 = {}

        # execute dfs
        for child in current_board._children:
            if not child.is_visited():
                child.visit()

                boundary.push(child)
                print
                print '.........diving in dfs at level ', level, ' into ', level + 1
                move, score = dfs(boundary, child.get_parent_move(), level + 1, player)
                print
                print '.........back to dfs at level', level, ' from level ', level + 1
                print
                print 'for child- '
                print child.print_current_board()
                print 'received- '
                print 'move- ', move
                print 'score- ', score
                score_dict2[child.get_parent_move()] = score
                child.set_score(score)
                #scores.insert(0, dfs(boundary, child.get_parent_move(), level + 1))


    #SCORES[winner]
    #print 'the current board, at level- ', level, ' after scoring neighbors, looks like this-'
    #print score_dict2
    #print current_board

    # calculate max_score and best_move
    best_score = 0

    # implement the strategy for the player
    # maximise, if PLAYERX
    # minimize, if PLAYERO
    if switch:
        best_score = max(score_dict2.values())
    else:
        best_score = min(score_dict2.values())

    #if player == provided.PLAYERX:
    #    best_score = max(score_dict2.values())
        #print 'maximum- ', score

    #else:
    #    best_score = min(score_dict2.values())
        #current_board.
        #print 'minimum- ', score

    best_move = (-1,-1)


    for move in score_dict2:
        if score_dict2[move] == best_score:
            best_move = move



    current_board.set_score(best_score)

    #print 'score at level- ', level, 'is ', score_dict2.values()
    #print 'moves- ', score_dict
    #print 'best move being- ', best_move
    #if level % 2 == 0:
    #    print "X's turn, maximize level"
    #    print "Among- ", score_dict2
    #    print "X should choose- ", best_move
    #else:
    #    print "O's turn, minimize level"
    #    print "Among- ", score_dict2
    #    print "O should choose- ", best_move

    print 'at level- ', level
    print 'score_dict- ', score_dict2
    print 'returning-  ', best_move, best_score
    return best_move, best_score



def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # initialize
    level = 0
    move = (-1, -1)
    # get a stack implementation for dfs
    boundary = stack.Stack()

    # create ttt_board object from the given board
    ttt_board = ttt_tree(board, [])
    print 'running minmax strategy on this board- '
    print '----------------------'
    print ttt_board
    print '----------------------'
    print 'to find the best move for ',

    # determine the current player
    if player == provided.PLAYERX:
        print 'PLAYERX'
    else:
        print 'PLAYERO'

    # initialize the boundary for dfs
    boundary.push(ttt_board)

    return dfs(boundary, move, level, player)
    #return 0, (-1, -1)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    move = move[1], move[0]
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


    #print 'testing dfs traversal for initial board-'

    board6 = provided.TTTBoard(dim, False)
    #board6.move(1, 1, provided.PLAYERX)
    board6.move(2, 0, provided.PLAYERO)
    board6.move(0, 2, provided.PLAYERO)
    board6.move(0, 1, provided.PLAYERX)
    board6.move(1, 0, provided.PLAYERX)
    board6.move(2, 1, provided.PLAYERO)
    board6.move(0, 0, provided.PLAYERO)
    board6.move(2, 2, provided.PLAYERX)
    #tree_board6 = ttt_tree(board6, [])

    #print '----------------------'
    #print board6
    #print '----------------------'
    #boundary = stack.Stack()

    #boundary.push(tree_board6)

    #print dfs(boundary, (-1, -1), 0, provided.PLAYERX)
    #print mm_move(board6, provided.PLAYERO)

    print move_wrapper(board6, provided.PLAYERX, 1)
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



#test_ttt_tree()




