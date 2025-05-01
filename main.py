from game import Game
from player import Player
from ai import AIPlayer


def main():
    game = Game(Player("X"), AIPlayer("O", "easy"))
    game.play()

if __name__ == "__main__":
    main()