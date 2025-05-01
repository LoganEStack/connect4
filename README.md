<!-- INTRODUCTION -->
<h1 align="center">Connect 4</h1>
  <p align="center">
    A game of connect 4 versus an artificial intelligence using the Minimax algorithm.
    <br />
  </p>
</div>


<!-- ABOUT -->
## About the Project
This program implements a playable version of Connect 4 in a console window. Players can verse each other
or an AI opponent. The opponent has multiple levels of difficulty and relies on the Minimax algorithm 
in order to decide its moves.

### Built With

[![Python][Python]][python-url]


<!-- HOW TO PLAY -->
## Rules of Connect 4
Connect 4 is a two-player strategy game where the goal is to be the first to get four of your colored discs in a row—horizontally, vertically, or diagonally. Players take turns dropping one disc at a time into a 7-column, 6-row grid. Discs fall to the lowest available space in the chosen column. The game ends when one player connects four in a row or when the grid is full with no winner, resulting in a draw.

### How to Play
Currently this game is played in the console window. Run main.py to start the game. 
Either the player or the computer is chosen at random to start. When it's the player's turn, 
enter a number to select a column in which to drop your piece. Press ctrl+c to quit at any time. 
Replace the AIPlayer object with another HumanPlayer object in main.py to play two player. 
Adjust the difficulty by changing the difficulty parameter in the AIPlayer instantiation to
"easy", "medium", "hard", or "very hard".

<!-- MINIMAX -->
## Minimax Algorithm

### Heuristic Function

### Alpha-beta Pruning

### On Connect 4 Being Solved

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Requires Python3 to run.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/LoganEStack/connect4.git
   ```
2. Install packages with pip
   ```sh
   pip install -r requirements.txt
   ```


<!-- FILES -->
## Files

### main.py
Entry point to the program.

### ai.py
Computer player logic.

### player.py
Logic for the human player to make a move.

### board.py
Data and logic for the board state.

### minimax.py
Logic for the Minimax algorithm.


<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/