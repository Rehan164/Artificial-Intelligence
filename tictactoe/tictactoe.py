"""
Tic Tac Toe Player
"""

import math
import copy
import sys

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
    
    if board == initial_state():
        return X
    
    countO = 0
    countX = 0

    for i in range(len(board)):
        for j in range(3):
            if board[i][j] == X:
                countX = countX + 1
            elif board[i][j] == O:
                countO = countO + 1
    
    if countX > countO:
        return O
    else:
        return X


def actions(board):
    
    result = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result.add((i,j))

    return result

def result(board, action):

    i = action[0]
    j = action[1]

    if board[i][j] != EMPTY:
        raise Exception("Invalid Move")

    nextTurn = player(board)
    newBoard = copy.deepcopy(board)
    newBoard[i][j] = nextTurn
    return newBoard

def winner(board):
    
    for i in range(3):
    
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]

    
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != EMPTY:
            return board[0][i]

    
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) and board[1][1] != EMPTY:
        return board[1][1]

    return None
    
def terminal(board):
    
    if winner(board) != None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    
    return True

def utility(board):

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

    if terminal(board):
        return None
    
    currentPlayer = player(board)
    if currentPlayer == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]


def max_value(board):
    if terminal(board):
        return (utility(board), None)

    value = -sys.maxsize-1
    optimalAction = None
    for action in actions(board):
        possibleResult = min_value(result(board, action))
        if possibleResult[0] > value:
            value = possibleResult[0]
            optimalAction = action

        
        if value == 1:
            break

    return (value, optimalAction)


def min_value(board):
    if terminal(board):
        return (utility(board), None)

    value = sys.maxsize
    optimalAction = None
    for action in actions(board):
        possibleResult = max_value(result(board, action))
        if possibleResult[0] < value:
            value = possibleResult[0]
            optimalAction = action

        
        if value == -1:
            break

    return (value, optimalAction)

