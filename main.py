import pygame
from game import Game
from player import Player
from ai import AIPlayer

def main():
    game = Game(Player("X", "Player"), AIPlayer("O", "medium"))
    game.run()

if __name__ == "__main__":
    main()