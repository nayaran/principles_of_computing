"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided
import random

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

class Stack:
    """
    A simple implementation of a LIFO queue.
    """

    def __init__(self):
        """
        Initialize the queue.
        """
        self._items = []

    def __len__(self):
        """
        Return the number of items in the queue.
        """
        return len(self._items)

    def __iter__(self):
        """
        Create an iterator for the queue.
        """
        for item in self._items:
            yield item

    def __str__(self):
        """
        Return a string representation of the queue.
        """
        return str(self._items)

    def push(self, item):
        """
        Add item to the queue.
        """
        self._items.insert(0, item)

    def pop(self):
        """
        Remove and return the least recently inserted item.
        """
        try:
            return self._items.pop(0)
        except IndexError:
            return 'empty'

    def clear(self):
        """
        Remove all items from the queue.
        """
        self._items = []

class TTTTree():
    """
    Custom implementation of Tree suitable for TTT game.
    Value at each node is a TTT board
    """

    def __init__(self, value, children):
        """
        Initilialize the class
        """
        self._value = value
        self._children = children
        self._visited = False
        self._score = 0
        self._parent_move = (-1, -1)

    def get_value(self):
        """
        Getter for node's value
        """
        return self._value

    def children(self):
        """
        Generator to return children
        """
        for child in self._children:
            yield child

    def push_child(self, value):
        """
        Adds child to the left
        """
        self._children.insert(0, value)

    def pop_child(self):
        """
        Removes child from right
        """
        return self._children.pop(0)

    def is_visited(self):
        """
        DFS-
        Marker to check if the board has been visited or not
        """
        return self._visited

    def visit(self):
        """
        DFS-
        Set the visit marker to true
        """
        self._visited = True

    def set_score(self, score):
        """
        Set the score for the current board
        """
        self._score = score

    def get_score(self):
        """
        Get the score for the current board
        """
        return self._score

    def set_parent_move(self, move):
        """
        Set the move that resulted in the present board
        """
        self._parent_move = move

    def get_parent_move(self):
        """
        Get the move that resulted in the present board
        """
        return self._parent_move

    def print_current_board(self):
        """
        Prints the current board residing in the ttt_tree object
        """
        return self._value.__str__()

    def __str__(self):
        """
        Generate a string representation of the tree
        Use an pre-order traversal of the tree
        """

        ans = "[\n"
        ans += str(self._value)

        for child in self._children:
             ans += ", "
             ans += str(child)
        return ans + "\n]"

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
    """
    Core dfs algorithm which calculates the best next move for the
    given player

    boundary: stack for implementing dfs
    move: the move which resulted in the current board
    level: tracks the depth in dfs
    player: the player for which we are determining the next move
    """

    #print
    #print '------------------------------'
    #print 'inside dfs level - ', level
    #print '------------------------------'

    # switch for determining whether to
    # maximize or minimize
    #switch = player == provided.PLAYERX

    # check whose turn it is
    #print 'switch- ', switch
    if level % 2 == 0:
        if player == provided.PLAYERX:
            current_player = provided.PLAYERX
            #print "X's turn, maximize level"
        else:
            current_player = provided.PLAYERO
            #print "0's turn, minimize level"
    else:
        if player == provided.PLAYERX:
            current_player = provided.PLAYERO
            #print "0's turn, minimize level"
        else:
            current_player = provided.PLAYERX
            #print "X's turn, maximize level"

    # pop the curent board from the stack to examine
    board_tree = boundary.pop()

    # create a copy of the current board
    current_board = TTTTree(board_tree.get_value().clone(), [])

    # check if we are at the leaf or not
    winner = current_board.get_value().check_win()

    #print board_tree.#print_current_board()
    #print 'board-move was- ', parent_move

    score_dict = {}

    if winner != None:
        # game finished, score the current board and return

        #if winner == 4:
            #print 'Game Drawn!!!'
        #elif winner == 2:
            #print 'X Wins!!!'
        #else:
            #print 'O Wins!!!'

        score_dict[move] = SCORES[winner]

    else:
        # add children
        # get the actual board
        board = board_tree.get_value()
        #children = 0
        moves = []

        while True:
            # get a move for the temp board
            move = get_random_move(board)
            ##print move

            # exit if board is full
            if move == (-1, -1):
                break

            moves.append(move)
            # update the temp board
            board.move(move[0], move[1], current_player)

            # create a new tree object
            child = TTTTree(current_board.get_value().clone(), [])

            # implement the move
            child.get_value().move(move[0], move[1], current_player)

            # associates the move with the board
            child.set_parent_move(move)

            # adds the child to the current board
            current_board.push_child(child)

            ##print board.#print_current_board()
            # updates the count of the children
            #children += 1

            # add the move to the score dict

        #print 'added- ', children, ' children...'
        #print 'moves- ', moves
        #print 'children added- '
        #print current_board

        # execute dfs
        for child in current_board.children():
            if not child.is_visited():
                child.visit()
                boundary.push(child)
                #print
                #print '.........diving in dfs at level ', level, ' into ', level + 1
                # recurse
                move, score = dfs(boundary, child.get_parent_move(), level + 1, player)
                #print
                #print '.........back to dfs at level', level, ' from level ', level + 1
                #print
                #print 'for child- '
                #print child.#print_current_board()
                #print 'received- '
                #print 'move- ', move
                #print 'score- ', score
                score_dict[child.get_parent_move()] = score
                child.set_score(score)

                # optimize

                # if we are at maximizing level, and we have got a 1 as score
                # return immediately

                if score == 1:
                    if current_player == provided.PLAYERX:
                            #print 'got the best move already'
                            #print 'no need to dive deeper-'
                            ##print 'returning-  ', move, score
                            break
                            #return move, score
                elif score == -1:
                    if current_player == provided.PLAYERO:
                        #print 'got the best move already'
                        #print 'no need to dive deeper-'
                        ##print 'returning-  ', move, score
                        break


    # calculate max_score and best_move
    best_score = 0

    # implement the strategy for the player
    # maximise, if PLAYERX
    # minimize, if PLAYERO
    if current_player == provided.PLAYERX:
        best_score = max(score_dict.values())
    else:
        best_score = min(score_dict.values())

    best_move = (-1,-1)

    for move in score_dict:
        if score_dict[move] == best_score:
            best_move = move

    current_board.set_score(best_score)

    #print 'at level- ', level
    #print 'score_dict- ', score_dict2
    #print 'returning-  ', best_move, best_score
    return best_move, best_score

def dfs_wrapper(boundary, move, level, player):
    """
    Wrapper for the core dfs method
    Because of dfs method returns moves, score
    instead of score, moves
    """
    move = dfs(boundary, move, level, player)
    return move[1], move[0]

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
    boundary = Stack()

    # create ttt_board object from the given board

    new_board = board.clone()
    ttt_board = TTTTree(new_board, [])
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
    best_move = dfs_wrapper(boundary, move, level, player)

    print 'best move- ', best_move[1]
    print 'with score- ', best_move[0]
    return best_move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    move = move[1], move[0]
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"

    return move[0][0], move[0][1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)


def test_ttt_tree():
    """
    Basics testing of the TTTTree class and the game as a whole
    """


    #my_tree = ttt_tree("a", [ttt_tree("b", [ttt_tree("c", []), ttt_tree("d", [])]),
    #                     ttt_tree("e", [ttt_tree("f", [ttt_tree("g", [])]), ttt_tree("h", []), ttt_tree("i", [])])])
    ##print "Tree with nine nodes", my_tree

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
    #board1 = provided.TTTBoard(dim, False)
    #board1.move(1, 1, provided.PLAYERX)

    #board2 = provided.TTTBoard(dim, False)
    #board2.move(0, 0, provided.PLAYERO)


    #board3 = provided.TTTBoard(dim, False)
    #board3.move(2, 0, provided.PLAYERO)


    #tree_board1 = ttt_tree(board1, [])
    #tree_board2 = ttt_tree(board2, [])
    #tree_board3 = ttt_tree(board3, [])

    #print 'board1 - '
    #print tree_board1.print_current_board()

    #print 'board2 - '
    #print tree_board2.print_current_board()

    #print 'board3 - '
    #print tree_board3.print_current_board()
    #print

    #board3 = ttt_tree(board1, [])
    #print 'main board - '
    #print board3

    # testing dfs

    #board4 = ttt_tree(board1, [tree_board3, tree_board2])
    #print 'board4- '
    #print board4

    #board3.push_child(tree_board2)
    #board3.push_child(tree_board3)

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

    print move_wrapper(board6, provided.PLAYERO, 1)

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
#mm_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]), provided.PLAYERX)
#mm_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO)
#mm_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), provided.PLAYERX)
#mm_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.EMPTY, provided.EMPTY]]), provided.PLAYERX)
