<!-- INTRODUCTION -->
# Connect 4
A game of connect 4 versus an artificial intelligence using the Minimax algorithm.


<!-- ABOUT -->
## About the Project
This program implements a playable version of Connect 4 in a console window. Players can verse each other
or an AI opponent. The opponent has multiple levels of difficulty and relies on the Minimax algorithm 
in order to decide its moves.

### Built With
[![Python][Python]][python-url]


<!-- HOW TO PLAY -->
## How to Play

### Rules of Connect 4
Connect 4 is a two-player strategy game where the goal is to be the first to get four of your colored discs in a row—horizontally, vertically, or diagonally. Players take turns dropping one disc at a time into a 7-column, 6-row grid. Discs fall to the lowest available space in the chosen column. The game ends when one player connects four in a row or when the grid is full with no winner, resulting in a draw.

### How to Run
1. Run the game using python main.py
2. In the main menu, select your game mode:
   - Player vs Player
   - Player vs AI
3. If playing against AI, select the difficulty level:
   - Easy (depth 1)
   - Medium (depth 2)
   - Hard (depth 4)
   - Very Hard (depth 6)
4. Click "Start Game" to begin
5. In the game:
   - Move your mouse left and right to position your piece
   - Click to drop your piece
   - First player to connect 4 pieces in a row, column, or diagonally wins
   - Press 'R' to restart the game
   - Press 'ESC' or 'Q' to quit


<!-- MINIMAX -->
## Minimax Algorithm
Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. It is widely used in two player turn-based games such as Tic-Tac-Toe, Backgammon, Mancala, Chess, etc.
In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible.
Every board state has a value associated with it. In a given state if the maximizer has upper hand then, the score of the board will tend to be some positive value. If the minimizer has the upper hand in that board state then it will tend to be some negative value. The values of the board are calculated by some heuristics which are unique for every type of game.
[Source](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)

### Heuristic Function
The heuristic function for this game involves a series of manual weights that increase a score based on how beneficial a move seems. The weights favor playing moves in the center, as that is a more optimal strategy than playing towards the edges. For each space, the surrounding spaces are analyzed to see if a player can potentially make 2, 3, or 4 in a row, and weighs those options accordingly. An oppportunity to make 4 in a row will always have the highest weight possible, as that is considered a win. The same simulation is run on potential moves for the opposing (human) player to assume what the next board state will be, so that the computer can make the computation once more. Each cycle of hypothetical AI and Human move is considered going one more layer down in depth. The game difficulty is just how far into the future (how deep) the algorithm searches. 

### Alpha-beta Pruning
Alpha-beta pruning is an optimization technique that is introduced in an effort to reduce runtime. Alpha is the best value that the maximizer currently can guarantee at that level or above. Beta is the best value that the minimizer currently can guarantee at that level or below. The pruning involves skipping entire branches of the decision tree where alpha is greater than beta which will never result in an optimal play and therefore never be chosen.

### On Connect 4 Being Solved
Connect 4 is a strongly solved game. This means that an an algorithm exists that can determine the optimal move (or optimal series of moves) for each player from any given position in the game, assuming both players are playing perfectly. Technically, the first player is guarenteed a win if played perfectly, and the second player is guarenteed at least a tie. Unfortunately, Connect 4 has roughly 4.5 trillion possible board states. This would require incredibly deep searches, or a massive table of solved moves in order to properly implement. Therefore, it is computationally unrealistic, and a depth-limited minimax algorithm with alpha-beta pruning is better suited for our purposes. While not mathematically perfect, it's still plenty capable of beating users (me) on higher difficulty settings.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
- Python 3.6+
- Pygame

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/LoganEStack/connect4.git
   ```
2. Install packages with pip
   ```sh
   pip install -r requirements.txt
   ```
3. Run the game
   ```sh
   python main.py
   ```


<!-- STRUCTURE -->
## Project Structure
| File        | Description
| ----------- | ------------------------
| main.py     | Entry point to the program.
| menu.py     | GUI and logic for menu.
| game.py     | GUI and logic for game.
| ai.py       | Computer player.
| player.py   | Human player.
| board.py    | Data and logic for the board state.
| minimax.py  | Logic for the Minimax algorithm.


<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/