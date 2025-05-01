class Player:
    """
    Human player.

    Attributes:
        piece (str): The player's game piece token.
        name (str): The player's name.

    Methods:
        get_move(): Gets the column selected by the player.
    """
    def __init__(self, piece, name="Player 1"):
        self.piece = piece
        self.name = name

    def get_move(self, board: object) -> int:
        while True:
            try:
                column = int(input(f"{self.name}'s turn ({self.piece}): Choose column (0-6): "))
            except ValueError:
                print("Invalid move. Please enter an integer between 0 and 6 inclusive.")
                continue
            except KeyboardInterrupt:
                raise KeyboardInterrupt("Exiting the game.")
                
            if board.is_valid_move(column):
                break
            print("Invalid move. Please enter an integer between 0 and 6 inclusive.")
        return column
    