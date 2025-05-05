import pygame
import sys

class Menu:
    """
    Main menu for the game.
    
    Attributes:
        bg_color: Background color.
        text_color: Text color.
        button_color: Button color.
        button_hover_color: Button color on mouse hover.
        button_text_color: Button text color.
        title_font: Font of the title text.
        button_font: Font of the button text.
        small_font: 
        buttons: List of all menu buttons.
        game_mode: Determines if player is versing another player or a computer.
        ai_difficulty: If versing a computer, determines the computer's difficulty.
    """

    WINDOW_WIDTH = 700
    WINDOW_HEIGHT = 700
    
    def __init__(self):
        self.screen = pygame.display.set_mode((Menu.WINDOW_WIDTH, Menu.WINDOW_HEIGHT))
        
        # Colors
        self.bg_color = (255, 200, 0)  # Yellow
        self.text_color = (0, 0, 0)  # Black
        self.button_color = (255, 215, 105)  # Light Yellow
        self.button_hover_color = (255, 230, 160)  # Lighter Yellow
        self.button_text_color = (0, 0, 0)  # Black
        self.button_selected_color = (240, 235, 230)  # Off-white
        
        # Fonts
        self.title_font = pygame.font.SysFont('Arial', 60, bold=True)
        self.button_font = pygame.font.SysFont('Arial', 32)
        
        # Buttons
        self.buttons = []
        self.create_buttons()
        
        # Game options
        self.game_mode = "pvc"
        self.ai_difficulty = "medium"

    def create_buttons(self):
        """Create the buttons for the menu GUI."""
        # Button dimensions
        button_width = 600
        button_height = 50
        button_spacing = 20
        
        # Y position for the first button
        y_position = 200
        
        # Player vs AI button
        self.buttons.append({
            'rect': pygame.Rect((Menu.WINDOW_WIDTH - button_width) // 2, y_position, button_width, button_height),
            'text': 'Computer',
            'action': 'pvc'
        })
        
        # Player vs Player button
        y_position += button_height + button_spacing
        self.buttons.append({
            'rect': pygame.Rect((Menu.WINDOW_WIDTH - button_width) // 2, y_position, button_width, button_height),
            'text': '2 Player',
            'action': 'pvp'
        })
        
        # AI Difficulty buttons
        y_position += button_height + button_spacing + 20
        difficulties = ["easy", "medium", "hard", "very hard"]
        small_button_width = (button_width - (len(difficulties) - 1) * button_spacing) // len(difficulties)
        
        for i, difficulty in enumerate(difficulties):
            x_position = (Menu.WINDOW_WIDTH - button_width) // 2 + i * (small_button_width + button_spacing)
            self.buttons.append({
                'rect': pygame.Rect(x_position, y_position, small_button_width, button_height),
                'text': difficulty.capitalize(),
                'action': f'difficulty_{difficulty}',
                'difficulty': difficulty
            })
        
        # Start game button
        y_position += button_height + button_spacing + 30
        self.buttons.append({
            'rect': pygame.Rect((Menu.WINDOW_WIDTH - button_width) // 2, y_position, button_width, button_height),
            'text': 'Start Game',
            'action': 'start'
        })
        
        # Quit button
        y_position += button_height + button_spacing
        self.buttons.append({
            'rect': pygame.Rect((Menu.WINDOW_WIDTH - button_width) // 2, y_position, button_width, button_height),
            'text': 'Quit',
            'action': 'quit'
        })

    def run(self):
        """Run the menu loop and return the selected options."""
        while True:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        for button in self.buttons:
                            if button['rect'].collidepoint(mouse_pos):
                                if button['action'] == 'pvp':
                                    self.game_mode = 'pvp'
                                elif button['action'] == 'pvc':
                                    self.game_mode = 'pvc'
                                elif button['action'].startswith('difficulty_'):
                                    self.ai_difficulty = button['difficulty']
                                elif button['action'] == 'start':
                                    if self.game_mode:
                                        return self.game_mode, self.ai_difficulty
                                elif button['action'] == 'quit':
                                    pygame.quit()
                                    sys.exit()
            self.draw(mouse_pos)
            pygame.display.update()

    def draw(self, mouse_pos):
        """Draw the elements to the screen."""
        self.screen.fill(self.bg_color)
        
        # Draw title
        title_surface = self.title_font.render('Connect 4', True, self.text_color)
        title_rect = title_surface.get_rect(center=(Menu.WINDOW_WIDTH // 2, 100))
        self.screen.blit(title_surface, title_rect)
        
        # Draw buttons
        for button in self.buttons:
            # Highlight button on hover
            color = self.button_hover_color if button['rect'].collidepoint(mouse_pos) else self.button_color
            
            if (button['action'] == 'pvp' and self.game_mode == 'pvp') or \
               (button['action'] == 'pvc' and self.game_mode == 'pvc') or \
               (button['action'].startswith('difficulty_') and button['difficulty'] == self.ai_difficulty):
                color = self.button_selected_color
            
            pygame.draw.rect(self.screen, color, button['rect'])
            pygame.draw.rect(self.screen, self.text_color, button['rect'], 2)  # Button border
            
            text_surface = self.button_font.render(button['text'], True, self.button_text_color)
            text_rect = text_surface.get_rect(center=button['rect'].center)
            self.screen.blit(text_surface, text_rect)