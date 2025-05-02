import random
import pygame
import sys
import math
from board import Board

class Game:
    """
    Handles game flow and rules.

    Attributes:
        board: The game board.
        players: The players, human or AI. Limited to 2.
        turn: Determines which player's turn it is.
        game_over: True if the game is over, either from a win or a draw.
        winner: Name of the winner.
    """

    # Constants for the game
    FPS = 60
    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 700
    BOARD_COLOR = (0, 0, 255)  # Blue
    EMPTY_COLOR = (0, 0, 0)    # Black
    PLAYER1_COLOR = (255, 0, 0)  # Red
    PLAYER2_COLOR = (255, 255, 0)  # Yellow
    SQUARE_SIZE = 100
    RADIUS = int(SQUARE_SIZE/2 - 5)
    
    # Board position
    BOARD_OFFSET_X = 0
    BOARD_OFFSET_Y = SQUARE_SIZE  # Leave space at top for piece dropping animation

    def __init__(self, player1: object, player2: object):
        self.board = Board()
        self.players = [player1, player2]
        self.turn = random.randint(0, 1)
        self.game_over = False
        self.winner = None
        
        # Store the piece colors
        self.piece_colors = {
            "X": Game.PLAYER1_COLOR,
            "O": Game.PLAYER2_COLOR,
            " ": Game.EMPTY_COLOR
        }

    def run(self):
        """Start the game."""
        pygame.init()
        pygame.display.set_caption('Connect 4')
        self.screen = pygame.display.set_mode((Game.WINDOW_WIDTH, Game.WINDOW_HEIGHT))
        self.font = pygame.font.SysFont('Arial', 32)
        self.clock = pygame.time.Clock()
        
        # Main game loop
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(Game.FPS)

    def handle_events(self):
        """Handle player input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                # Only handle mouse events for human player
                if self.players[self.turn].__class__.__name__ == "Player":
                    self.handle_player_move(event.pos[0])
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reset game with 'r' key
                    self.reset_game()
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:  # Quit with 'q' or ESC
                    pygame.quit()
                    sys.exit()

    def update(self):
        """Handle computer's move."""
        if not self.game_over and self.players[self.turn].__class__.__name__ == "AIPlayer":
            self.handle_ai_move()

    def draw(self):
        """Draw elements to screen."""
        self.screen.fill((0, 0, 0)) # Clear screen with black
        self.draw_board()
        
        # Draw current player's piece at mouse position if it's player's turn and game is not over
        if not self.game_over and self.players[self.turn].__class__.__name__ == "Player":
            self.draw_hover_piece()
        
        if self.game_over:
            self.draw_game_over_message()
            
        pygame.display.update()

    def draw_board(self):
        """Draws game board to screen."""
        board_width = Game.SQUARE_SIZE * Board.COLUMNS
        board_height = Game.SQUARE_SIZE * Board.ROWS
        pygame.draw.rect(
            self.screen, 
            Game.BOARD_COLOR, 
            (Game.BOARD_OFFSET_X, Game.BOARD_OFFSET_Y, board_width, board_height)
        )
        
        # Draw the grid and pieces
        for row in range(Board.ROWS):
            for col in range(Board.COLUMNS):
                # Calculate position for this grid cell
                x = col * Game.SQUARE_SIZE + Game.SQUARE_SIZE // 2 + Game.BOARD_OFFSET_X
                y = row * Game.SQUARE_SIZE + Game.SQUARE_SIZE // 2 + Game.BOARD_OFFSET_Y
                
                # Draw the empty circle
                pygame.draw.circle(
                    self.screen,
                    self.piece_colors[self.board.grid[row][col]],
                    (x, y),
                    Game.RADIUS
                )

    def draw_hover_piece(self):
        """Draw the piece at the mouse x-position when it's the player's turn"""
        x = pygame.mouse.get_pos()[0]
        color = self.piece_colors[self.players[self.turn].piece]
        pygame.draw.circle(self.screen, color, (x, Game.SQUARE_SIZE // 2), Game.RADIUS)

    def draw_game_over_message(self):
        """Draw a banner for any given end-game state."""
        text = None
        if self.winner == "draw":
            text = "It's a draw!"
        else:
            text = f"{self.winner} wins!"
        
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(Game.WINDOW_WIDTH // 2, Game.SQUARE_SIZE // 2))
        
        # Add background to text for better visibility
        bg_rect = text_rect.copy()
        bg_rect.inflate_ip(20, 10)
        pygame.draw.rect(self.screen, (0, 0, 0), bg_rect)
        pygame.draw.rect(self.screen, (255, 255, 255), bg_rect, 2)
        
        self.screen.blit(text_surface, text_rect)
        
        # Add restart instructions
        restart_text = self.font.render("Press 'R' to restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(Game.WINDOW_WIDTH // 2, text_rect.bottom + 30))
        self.screen.blit(restart_text, restart_rect)

    def handle_player_move(self, mouse_x):
        """Determine which column the player is selecting and make the move."""
        # Convert mouse x position to column
        col = int(mouse_x // Game.SQUARE_SIZE)
        
        if 0 <= col < Board.COLUMNS and self.board.is_valid_move(col):
            self.make_move(col)

    def handle_ai_move(self):
        """Make the computer's move."""
        col = self.players[self.turn].get_move(self.board)
        self.make_move(col)

    def make_move(self, col):
        """Place a piece on the board and determine if that results in a game over."""
        row = self.board.get_next_open_row(col)
        
        if row is not None:
            self.board.drop_piece(row, col, self.players[self.turn].piece)
            
            if self.board.winning_move(self.players[self.turn].piece):
                self.game_over = True
                self.winner = self.players[self.turn].name
            elif self.board.is_full():
                self.game_over = True
                self.winner = "draw"
            else:
                self.turn = (self.turn + 1) % 2

    def reset_game(self):
        """Resets the game."""
        self.board = Board()
        self.turn = random.randint(0, 1)
        self.game_over = False
        self.winner = None