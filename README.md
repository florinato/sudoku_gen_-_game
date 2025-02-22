# Sudokan

This project is a Sudoku game implemented in Python. It consists of two main parts:

1.  **Sudoku Generator (`sudoku_gen.py`):** This script generates unique Sudoku puzzles with the additional constraint that the main diagonals (top-left to bottom-right and top-right to bottom-left) also contain unique numbers from 1 to 9. It uses a backtracking algorithm to solve the Sudoku and ensures the generated puzzle is valid. The generated puzzle is saved to `test1.txt`.

2.  **Sudoku Game (`sudokan.py`):** This script provides a graphical user interface (GUI) for playing the Sudoku game. It loads the generated puzzle from `test1.txt` and presents it to the user. The user can interact with the board, inputting numbers and receiving feedback on their moves. The game offers different difficulty levels, which control the number of initially filled cells.

## Dependencies

-   numpy
-   tkinter (usually comes with standard Python installation)

These can be installed using pip:

```bash
pip install -r requirements.txt
```
The `requirements.txt` contains:
```
numpy==2.2.2
```

## How to Run

1.  **Generate a Sudoku:** The `sudoku_gen.py` script generates a Sudoku and saves it in `test1.txt`. This script is executed indirectly when running `sudokan.py`.
2.  **Play the Game:** Run the `sudokan.py` script to start the game:

    ```bash
    python sudokan.py
    ```

    This will open a window displaying the Sudoku board. Use the number buttons (1-9) to input numbers, and the arrow keys and "C" button to navigate and clear cells, respectively.
