import math
import random
from board import Board


def evaluate_window(window, piece):
    """Add score based on how many pieces are in a line."""
    score = 0
    opponent_piece = "X" if piece == "O" else "O"

    if window.count(piece) == 4:
        score += 1000
    elif window.count(piece) == 3 and window.count(" ") == 1:
        score += 10
    elif window.count(piece) == 2 and window.count(" ") == 2:
        score += 5

    if window.count(opponent_piece) == 3 and window.count(" ") == 1:
        score -= 80

    return score

def score_position(board, piece):
    """Manual weights to help computer decide on a move."""
    score = 0

    # Score center column - favors playing in the center
    center_array = [row[3] for row in board.grid]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score horizontal
    for r in range(6):
        row_array = board.grid[r]
        for c in range(4):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Score vertical
    for c in range(7):
        col_array = [board.grid[r][c] for r in range(6)]
        for r in range(3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    # Score positive diagonal
    for r in range(3):
        for c in range(4):
            window = [board.grid[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Score negative diagonal
    for r in range(3, 6):
        for c in range(4):
            window = [board.grid[r-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def utility(board, ai_piece, player_piece):
    """Heuristic function returns score of current board state."""
    if board.winning_move(ai_piece):
        return (None, math.inf)
    elif board.winning_move(player_piece):
        return (None, -math.inf)
    else:
        return (None, score_position(board, ai_piece))

def minimax(
    board: Board,
    depth: int,
    alpha: float,
    beta: float,
    maximizing_player: bool,
    ai_piece: str,
    player_piece: str
) -> tuple[int, float]:
    """Determines the best column to place a piece.

    Develops an implicit tree through recursion, starting from the leaf nodes (the end of the game)
    and working up to the root (the current move) in order to determine the best move based on the simulation.

    board: The hypothetical game board.
    depth: Depth of the game tree, with zero being the leaves (the end of the game).
    alpha: The best score that the maximizing player can achieve thus far.
    beta: The best score that the minimizing player can achieve thus far.
    maximizing_player: True if ...

    """
    valid_locations = [c for c in range(7) if board.is_valid_move(c)]
    is_terminal = board.winning_move(ai_piece) or board.winning_move(
        player_piece) or board.is_full()

    if is_terminal or depth == 0:
        return utility(board, ai_piece, player_piece)

    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            temp_board = board.copy()
            row = temp_board.get_next_open_row(col)
            temp_board.drop_piece(row, col, ai_piece)
            new_score = minimax(temp_board, depth - 1, alpha,
                                beta, False, ai_piece, player_piece)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            # Alpha-Beta Pruning
            if alpha >= beta:
                break
        return column, value
    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            temp_board = board.copy()
            row = temp_board.get_next_open_row(col)
            temp_board.drop_piece(row, col, player_piece)
            new_score = minimax(temp_board, depth - 1, alpha,
                                beta, True, ai_piece, player_piece)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            # Alpha-Beta Pruning
            if alpha >= beta:
                break
        return column, value
