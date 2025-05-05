class Player:
    """
    Human player.

    Attributes:
        piece (str): The player's game piece token.
        name (str): The player's name.
    """
    
    def __init__(self, piece, name="Player 1"):
        self.piece = piece
        self.name = name

    def get_move(self, board: object) -> int:
        # This method is not used for GUI input
        # Input is handled in the Game class's handle_events() method
        # This is kept for compatibility with the AI class
        pass