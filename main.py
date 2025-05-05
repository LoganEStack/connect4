import pygame
from game import Game
from menu import Menu
from player import Player
from ai import AIPlayer

def main():
    pygame.init()
    pygame.display.set_caption('Connect 4')
    menu = Menu()
    game_mode, ai_difficulty = menu.run()

    if game_mode == 'pvp':
        game = Game(Player("X", "Player 1"), Player("O", "Player 2"))
    else:
        game = Game(Player("X", "Player"), AIPlayer("O", ai_difficulty))

    game.run()

if __name__ == "__main__":
    main()