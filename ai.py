import random
import math
from minimax import minimax


class AIPlayer:
    """
    Computer player.

    Attributes:
        piece (str): The player's game piece token.
        opponent_piece (str): The opposing player's piece.
        difficulty (str): The difficulty level of the computer, affecting depth of simulation.
        name (str): Name of the computer.
    """
    
    def __init__(self, piece, difficulty="hard"):
        self.piece = piece
        self.opponent_piece = "X" if piece == "O" else "O"
        self.difficulty = difficulty.lower()
        self.name="Computer"

    def get_move(self, board: object) -> int:
        if self.difficulty == "easy":
            depth = 1
        elif self.difficulty == "medium":
            depth = 2
        elif self.difficulty == "hard":
            depth = 4
        elif self.difficulty == "very hard":
            depth = 6
        else:
            raise ValueError("Difficulty of AI opponent must be set to either easy, medium, or hard.")

        column, _ = minimax(
            board,
            depth=depth,
            alpha=-math.inf,
            beta=math.inf,
            maximizing_player=True,
            ai_piece=self.piece,
            player_piece=self.opponent_piece
        )
        print("Computer's turn:", column)
        return column
