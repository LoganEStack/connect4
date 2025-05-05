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
