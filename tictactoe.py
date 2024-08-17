import math

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []

    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible_actions.append((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if board[i][j] is not EMPTY:
        raise ValueError("Invalid move")

    dummy = [row[:] for row in board]
    dummy[i][j] = player(board)

    return dummy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    player_turn = player(board)

    if player_turn == X:
        best_value = -math.inf
        best_move = None

        for move in actions(board):
            move_value = min_value(result(board, move))

            if move_value > best_value:
                best_value = move_value
                best_move = move

        return best_move

    else:
        best_value = math.inf
        best_move = None

        for move in actions(board):
            move_value = max_value(result(board, move))

            if move_value < best_value:
                best_value = move_value
                best_move = move

        return best_move
    

def max_value(board):
    """
    Finds the maximum value for player X after a move.
    """
    if terminal(board):  
        return utility(board)
    
    max_score = -math.inf

    for move in actions(board):
        score = min_value(result(board, move))

        if score > max_score:
            max_score = score

    return max_score


def min_value(board):
    """
    Finds the minimum value for player O after a move.
    """
    if terminal(board):  
        return utility(board)
     
    min_score = math.inf

    for move in actions(board):
        score = max_value(result(board, move))

        if score < min_score:
            min_score = score

    return min_score
