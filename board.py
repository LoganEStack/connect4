class Board:
    """
    Handles game board and display logic.

    Attributes:
        grid (List[List[str]]): The game board.

    Methods:
        print_board(): Prints the current grid state.
        is_valid_move(): Returns True if a column is in bounds and not full.
        get_next_open_row(): Finds the next open level in a given column.
        drop_piece(): Places a piece on the grid.
        winning_move(): Returns True if a move wins the game.
        is_full(): Returns True if the grid is completely full.
    """
    ROWS = 6
    COLUMNS = 7

    def __init__(self):
        self.grid = [[" " for _ in range(Board.COLUMNS)] for _ in range(Board.ROWS)]

    def print_board(self) -> None:
        for row in self.grid:
            print("|" + "|".join(row) + "|")
        print(" " + " ".join(str(i) for i in range(Board.COLUMNS)))
        print()

    def is_valid_move(self, col:int) -> bool:
        if col < 0 or col >= Board.COLUMNS:
            return False
        return self.grid[0][col] == " "

    def get_next_open_row(self, col) -> int | None:
        for row in reversed(range(Board.ROWS)):
            if self.grid[row][col] == " ":
                return row
        return None

    def drop_piece(self, row:int, col:int, piece: str) -> None:
        self.grid[row][col] = piece

    def winning_move(self, piece:str) -> bool:
        # Horizontal
        for c in range(Board.COLUMNS-3):
            for r in range(Board.ROWS):
                if self.grid[r][c] == piece and \
                    self.grid[r][c+1] == piece and \
                    self.grid[r][c+2] == piece and \
                    self.grid[r][c+3] == piece:
                    return True
        # Vertical
        for c in range(Board.COLUMNS):
            for r in range(Board.ROWS-3):
                if self.grid[r][c] == piece and \
                    self.grid[r+1][c] == piece and \
                    self.grid[r+2][c] == piece and \
                    self.grid[r+3][c] == piece:
                    return True

        # Positive diagonal
        for c in range(Board.COLUMNS-3):
            for r in range(Board.ROWS-3):
                if self.grid[r][c] == piece and \
                    self.grid[r+1][c+1] == piece and \
                    self.grid[r+2][c+2] == piece and \
                    self.grid[r+3][c+3] == piece:
                    return True
        # Negative diagonal
        for c in range(Board.COLUMNS-3):
            for r in range(3 ,Board.ROWS):
                if self.grid[r][c] == piece and \
                    self.grid[r-1][c+1] == piece and \
                    self.grid[r-2][c+2] == piece and \
                    self.grid[r-3][c+3] == piece:
                    return True
        return False

    def is_full(self) -> bool:
        return all(self.grid[0][col] != " " for col in range(Board.COLUMNS))
    
    def copy(self) -> object:
        new_board = Board()
        new_board.grid = [row[:] for row in self.grid]
        return new_board