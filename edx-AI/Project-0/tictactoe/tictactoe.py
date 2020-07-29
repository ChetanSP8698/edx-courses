"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    no_of_X = 0
    no_of_O = 0
    if board == initial_state():
        no_of_X += 1
        return X

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                no_of_X += 1
            elif board[i][j] == O:
                no_of_O += 1
            else:
                pass

    if no_of_X == no_of_O:
        no_of_X += 1
        return X
    else:
        no_of_O += 1
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                act.add((i, j))

    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    loc_copy = copy.deepcopy(board)

    try:
        if loc_copy[action[0]][action[1]] == EMPTY:
            loc_copy[action[0]][action[1]] = player(loc_copy)
            return loc_copy
        else:
            raise IndexError
    except IndexError:
        print('Space occupied, Play other Move')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    colms = []
    for row in board:
        x_count = row.count(X)
        o_count = row.count(O)
        if x_count == 3:
            return X
        if o_count == 3:
            return O

    for j in range(len(board)):
        col = [row[j] for row in board]
        colms.append(col)

    for j in colms:
        x_count = j.count(X)
        o_count = j.count(O)
        if x_count == 3:
            return X
        if o_count == 3:
            return O

    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    flag = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                flag = 1

    if flag == 1:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        new_val = -math.inf
        for action in actions(board):
            res = min_value(result(board, action))
            if res > new_val:
                new_val = res
                next_move = action
    else:
        new_val = math.inf
        for action in actions(board):
            res = max_value(result(board, action))
            if res < new_val:
                new_val = res
                next_move = action
    return next_move

def max_value(board):
    if terminal(board):
        return utility(board)
    val = -math.inf
    for action in actions(board):
        val = max(val, min_value(result(board, action)))
    return val

def min_value(board):
    if terminal(board):
        return utility(board)
    val = math.inf
    for action in actions(board):
        val = min(val, max_value(result(board, action)))
    return val
