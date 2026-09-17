# Python-Minesweeper

A small Python implementation of the classic Minesweeper game. The project follows a simple board-and-tile structure and runs from the terminal.

## Directory

```text
Python-Minesweeper/
├── LICENSE
├── README.md
└── src/
    ├── Tile.py
    └── main.py
```

- `src/Tile.py`: contains the Tile model used by the board.
- `src/main.py`: contains the game logic, matrix creation, reveal rules, board rendering, and input handling.

## Deploy to play a game

1. Open a terminal in the project folder.
2. Go to the `src` directory.
3. Run the game:

```bash
python main.py
```

If you are using Windows and `python` is not recognized, try:

```bash
py main.py
```

The game is currently configured with a small board and a limited number of mines:

- board size: 3 x 3
- mines: 2

## Documentation

### Tile class
File: `src/Tile.py`

The `Tile` class represents each cell on the board.

Methods:

- `__init__(self, Value)`
  - creates a tile with a numeric value and a visited flag
- `get_value()`
  - returns the tile value
- `set_value(value)`
  - updates the tile value and sets safety status
- `check_safety()`
  - returns whether the tile is safe
- `is_visited()`
  - checks if the tile has already been revealed
- `Visited()`
  - marks the tile as visited
- `is_safe()`
  - returns whether the tile is not a mine

### Main game functions
File: `src/main.py`

- `main()`
  - runs the game loop and decides win/lose conditions
- `check_Matrix(game_table, posX, posY)`
  - checks if the selected tile is a mine and reveals safe neighbors when needed
- `reveal_Neighbours(game_table, posX, posY)`
  - recursively expands zero-value cells around the selected tile
- `Create_Matrix(size, num_Bombs)`
  - builds the board and initializes bombs + proximity values
- `Bombing(game_Tableboard, num_Bombs, size)`
  - places mines randomly on the board
- `Proximity(game_Tableboard)`
  - counts adjacent bombs for each non-mine tile
- `show_matrix(game_table)`
  - prints the current visible board in the terminal
- `show_all(game_table, posX, posY)`
  - prints the full board for the end of the game
- `check_rest(game_table)`
  - counts remaining hidden safe tiles
- `readKB(size)`
  - reads the selected row and column from the user

## Next steps

### Improve QoL

- add difficulty levels (easy, medium, hard)
- validate the board size and mine count more robustly
- show clearer messages for win/loss and invalid input
- allow replay without restarting the program
- add a proper board reset option

### GUI

- create a desktop version with Tkinter
- add a graphical board with clickable tiles
- show flags, win/loss screens, and score tracking
- migrate to a richer UI such as PyQt or Pygame for better interaction

## Notes

This is a lightweight terminal-based version intended to practice board logic, recursion, and object-oriented design in Python. It can be expanded into a more complete game with better interface and gameplay polish.
