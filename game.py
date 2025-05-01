from board import Board
import random

class Game:
    """
    Handles game flow and rules.

    Attributes:
        board (Board): The game board.
        players (List[Player]): The players, human or AI. Limited to 2.
        turn (int): Determines which player's turn it is.

    Methods:
        play(): Starts the game.
    """

    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.turn = random.randint(0, 1)

    def play(self):
        game_over = False
        while not game_over:
            current_player = self.players[self.turn]
            self.board.print_board()

            # Make a move
            move = current_player.get_move(self.board)
            row = self.board.get_next_open_row(move)
            self.board.drop_piece(row, move, current_player.piece)

            # Determine if game is over
            if self.board.winning_move(current_player.piece):
                self.board.print_board()
                print(f"{current_player.name} wins!")
                game_over = True
            elif self.board.is_full():
                self.board.print_board()
                print("It's a draw!")
                game_over = True

            self.turn = (self.turn + 1) % 2
